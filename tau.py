import streamlit as st
# Set page config must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Biomedical Knowledge Graph")
from stats import *
from pyvis.network import Network
import streamlit.components.v1 as components
# from network_analyzer import NetworkAnalyzer
import json
import pandas as pd
import networkx as nx
import numpy as np
from IPython.display import HTML, display
import colorsys
import re
from deb_data import *
# Color scheme
color_scheme = {
    "gene": "#1f77b4",  # Blue
    "protein": "#2ca02c",  # Green
    "disease": "#d62728",  # Red
    "pathway": "#9467bd"  # Purple
}

# Utility functions
def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_rgba(rgb, alpha):
    """Convert RGB tuple to RGBA string."""
    return f"rgba{rgb + (alpha,)}"


def get_node_cluster(node_id, clusters_data):
    """Get cluster for a node."""
    for cluster_name, nodes in clusters_data.items():
        if node_id in nodes:
            return cluster_name
    return "Other"




# Define clusters
# Define updated clusters


def create_network(selected_cluster=None):
    """Create and configure the network visualization."""
    # Create Pyvis network
    net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black")
    net.force_atlas_2based()

    # Add nodes
    for node in nodes_data:
        color = color_scheme[node["type"]]
        size = 20

        if selected_cluster:
            is_in_cluster = node["id"] in clusters_data.get(selected_cluster, [])
            if is_in_cluster:
                size = 30
            else:
                rgb = hex_to_rgb(color)
                color = f"rgba{rgb + (0.15,)}"

        net.add_node(
            node["id"],
            label=node["id"],
            color=color,
            title=f"Type: {node['type']}<br>Cluster: {node['cluster']}<br>ID: {node['id']}",
            size=size
        )

    # Add edges
    for edge in edges_data:
        edge_color = "#666666"
        edge_width = edge["score"] * 3

        if selected_cluster:
            source_in_cluster = edge["source"] in clusters_data.get(selected_cluster, [])
            target_in_cluster = edge["target"] in clusters_data.get(selected_cluster, [])

            if source_in_cluster or target_in_cluster:
                edge_color = "#000000"
                edge_width = edge["score"] * 4
            else:
                edge_color = "rgba(102, 102, 102, 0.15)"
                edge_width = edge["score"] * 2

        net.add_edge(
            edge["source"],
            edge["target"],
            title=f"Relation: {edge['relation']}<br>Score: {edge['score']:.2f}",
            width=edge_width,
            color=edge_color
        )

    # Physics options
    net.set_options("""
    var options = {
        "physics": {
            "forceAtlas2Based": {
                "gravitationalConstant": -100,
                "centralGravity": 0.015,
                "springLength": 150,
                "springConstant": 0.1,
                "damping": 0.95
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based",
            "stabilization": {
                "enabled": true,
                "iterations": 1000
            }
        }
    }
    """)

    return net


def display_network_stats(nodes_data, edges_data, selected_cluster):
    """Display network statistics in the sidebar."""
    st.sidebar.title("Network Statistics")

    total_nodes = len(nodes_data)
    total_edges = len(edges_data)
    st.sidebar.write(f"Total Nodes: {total_nodes}")
    st.sidebar.write(f"Total Edges: {total_edges}")

    # Fixed node type counting
    node_types_count = {}
    for node in nodes_data:
        if node["type"] in node_types_count:
            node_types_count[node["type"]] += 1
        else:
            node_types_count[node["type"]] = 1

    st.sidebar.write("\nNode Types:")
    for node_type, count in node_types_count.items():
        percentage = (count / total_nodes) * 100
        st.sidebar.write(f"{node_type.capitalize()}: {count} ({percentage:.1f}%)")


def display_legend_in_sidebar(nodes_data):
    """Display color-coded legend with node counts in the sidebar."""
    st.sidebar.markdown("---")  # Separator
    st.sidebar.markdown("### Legend")
    
    # Count nodes by type
    node_counts = {}
    for node in nodes_data:
        if node["type"] in node_counts:
            node_counts[node["type"]] += 1
        else:
            node_counts[node["type"]] = 1
    
    # Display each node type with color and count
    for node_type, color in color_scheme.items():
        count = node_counts.get(node_type, 0)
        st.sidebar.markdown(
            f'<div style="display: flex; align-items: center; margin: 5px 0;">'
            f'<div style="width: 15px; height: 15px; background-color: {color}; '
            f'margin-right: 10px; border-radius: 3px;"></div>'
            f'<span>{node_type.capitalize()}: {count}</span></div>',
            unsafe_allow_html=True
        )

def main():
    """Main application function."""
    # Initialize network analyzer
    analyzer = NetworkAnalyzer(nodes_data, edges_data)

    # Sidebar controls
    st.sidebar.title("Network Navigation")
    selected_cluster = st.sidebar.selectbox(
        "Select Cluster to Highlight",
        ["All"] + list(clusters_data.keys())
    )
    
    # Add legend to sidebar
    display_legend_in_sidebar(nodes_data)

    # Rest of your main function remains the same...
    main_tab, stats_tab = st.tabs(["Network Visualization", "Detailed Analysis"])
    
    with main_tab:
        st.title("Biomedical Knowledge Graph Visualization")
        
        # Create and display network
        net = create_network(None if selected_cluster == "All" else selected_cluster)
        net.save_graph("network.html")
        with open("network.html", "r", encoding="utf-8") as f:
            html = f.read()
        components.html(html, height=800)
        
        # Display legend
        # st.write("\n### Node Type Legend")
        # cols = st.columns(4)
        # for i, (node_type, color) in enumerate(color_scheme.items()):
        #     with cols[i]:
        #         st.markdown(
        #             f'<div style="display: flex; align-items: center;">'
        #             f'<div style="width: 20px; height: 20px; background-color: {color}; '
        #             f'margin-right: 10px; border-radius: 50%;"></div>'
        #             f'<span style="font-weight: 500;">{node_type.capitalize()}</span></div>',
        #             unsafe_allow_html=True
        #         )

    with stats_tab:
        # Display network statistics based on selection
        analyzer.display_stats_streamlit(selected_cluster)

    # Enhanced Export functionality
    st.sidebar.markdown("---")
    st.sidebar.subheader("Export Options")

    export_col1, export_col2 = st.sidebar.columns(2)

    with export_col1:
        if st.button("Export Full Network"):
            full_net = create_network(None)  # Create network without highlighting
            full_net.save_graph("network_export_full.html")
            with open("network_export_full.html", "r", encoding="utf-8") as f:
                html_content = f.read()
            st.download_button(
                label="Download Full Network",
                data=html_content,
                file_name="full_network.html",
                mime="text/html"
            )

    with export_col2:
        if selected_cluster != "All" and st.button("Export Cluster"):
            # Create network with only the selected cluster
            cluster_nodes = clusters_data.get(selected_cluster, [])
            cluster_net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black")

            # Add nodes from the selected cluster
            added_nodes = set()
            for node in nodes_data:
                if node["id"] in cluster_nodes:
                    cluster_net.add_node(
                        node["id"],
                        label=node["id"],
                        color=color_scheme[node["type"]],
                        title=f"Type: {node['type']}<br>Cluster: {node['cluster']}<br>ID: {node['id']}",
                        size=30
                    )
                    added_nodes.add(node["id"])

            # Add edges between nodes in the cluster
            for edge in edges_data:
                if edge["source"] in added_nodes and edge["target"] in added_nodes:
                    cluster_net.add_edge(
                        edge["source"],
                        edge["target"],
                        title=f"Relation: {edge['relation']}<br>Score: {edge['score']:.2f}",
                        width=edge["score"] * 3,
                        color="#000000"
                    )

            # Save and offer download
            cluster_net.save_graph("network_export_cluster.html")
            with open("network_export_cluster.html", "r", encoding="utf-8") as f:
                html_content = f.read()
            st.download_button(
                label="Download Cluster Network",
                data=html_content,
                file_name=f"{selected_cluster.lower()}_network.html",
                mime="text/html"
            )

    # Export statistics as JSON
    if st.sidebar.button("Export Statistics as JSON"):
        if selected_cluster == "All":
            export_stats = analyzer.get_basic_stats()
        else:
            export_stats = analyzer.get_cluster_stats(selected_cluster)

        json_stats = json.dumps(export_stats, indent=2)
        st.sidebar.download_button(
            label="Download Statistics",
            data=json_stats,
            file_name="network_statistics.json",
            mime="application/json"
        )


if __name__ == "__main__":
    main()
