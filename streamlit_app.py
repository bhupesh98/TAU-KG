import streamlit as st
import json
import math
from pyvis.network import Network
import streamlit.components.v1 as components
from deb_data2 import *

# Set page config must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Biomedical Knowledge Graph")

# Color scheme
color_scheme = {
    "gene": "#1f77b4",        # Blue
    "gene group": "#1f77b4",  # Same blue as gene
    "protein": "#2ca02c",     # Green
    "protein complex": "#2ca02c",  # Same green as protein
    "protein fragment": "#2ca02c", # Same green as protein
    "disease": "#d62728",     # Red
    "pathway": "#9467bd",     # Purple
    "process": "#9467bd"      # Same purple as pathway
}

# Utility functions
def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_rgba(rgb, alpha):
    """Convert RGB tuple to RGBA string."""
    return f"rgba{rgb + (alpha,)}"

def get_node_relationships(node_id):
    """Get all relationships for a specific node."""
    relationships = []
    for edge in edges_data:
        if edge["source"] == node_id:
            relationships.append({
                "related_node": edge["target"],
                "relation": edge["relation"],
                "score": edge["score"],
                "direction": "outgoing"
            })
        elif edge["target"] == node_id:
            relationships.append({
                "related_node": edge["source"],
                "relation": edge["relation"],
                "score": edge["score"],
                "direction": "incoming"
            })
    return relationships

def create_network(selected_cluster=None):
    """Create and configure the network visualization."""
    net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black")
    net.force_atlas_2based()

    # Add nodes
    for node in nodes_data:
        color = color_scheme[node["type"]]
        base_size = node["size"] * 10
        
        if selected_cluster:
            is_in_cluster = node["cluster"] == selected_cluster
            if is_in_cluster:
                size = base_size * 1.5
            else:
                size = base_size
                rgb = hex_to_rgb(color)
                color = f"rgba{rgb + (0.15,)}"
        else:
            size = base_size

        # Add onClick event for nodes
        title = (f"Type: {node['type']}<br>"
                f"Cluster: {node['cluster']}<br>"
                f"Size: {node['size']:.2f}<br>"
                f"ID: {node['id']}<br><br>"
                f"Ctrl+Click to download node data")

        net.add_node(
            node["id"],
            label=node["id"],
            color=color,
            title=title,
            size=size
        )

    # Add edges
    for edge in edges_data:
        edge_color = "#666666"
        edge_width = edge["score"] * 3

        if selected_cluster:
            source_node = next((n for n in nodes_data if n["id"] == edge["source"]), None)
            target_node = next((n for n in nodes_data if n["id"] == edge["target"]), None)
            
            if source_node and target_node:
                source_in_cluster = source_node["cluster"] == selected_cluster
                target_in_cluster = target_node["cluster"] == selected_cluster

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

    # Configure physics
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
        },
        "interaction": {
            "hover": true,
            "tooltipDelay": 200
        }
    }
    """)
    
    return net

def handle_node_selection():
    """Handle selection and data download for nodes."""
    # Create a container for the download button
    download_container = st.sidebar.container()
    
    # Get selected node from session state
    selected_node = st.session_state.get('selected_node', None)
    
    if selected_node:
        node_data = next((n for n in nodes_data if n["id"] == selected_node), None)
        if node_data:
            relationships = get_node_relationships(selected_node)
            
            # Prepare data for download
            download_data = {
                "node_info": node_data,
                "relationships": relationships
            }
            
            # Convert to JSON
            json_data = json.dumps(download_data, indent=2)
            
            # Create download button
            download_container.download_button(
                label=f"Download {selected_node} Data",
                data=json_data,
                file_name=f"{selected_node}_data.json",
                mime="application/json"
            )

def main():
    """Main application function."""
    # Initialize session state for node selection
    if 'selected_node' not in st.session_state:
        st.session_state.selected_node = None

    # Sidebar controls
    st.sidebar.title("Network Navigation")
    selected_cluster = st.sidebar.selectbox(
        "Select Cluster to Highlight",
        ["All"] + list(clusters_data.keys())
    )

    # Download buttons section
    st.sidebar.markdown("---")
    st.sidebar.subheader("Download Options")

    # Full network download
    if st.sidebar.button("Download Full Network"):
        full_net = create_network()
        full_net.save_graph("network_export_full.html")
        with open("network_export_full.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        st.sidebar.download_button(
            label="Save Network HTML",
            data=html_content,
            file_name="full_network.html",
            mime="text/html"
        )

    # Cluster-specific download
    if selected_cluster != "All" and st.sidebar.button(f"Download {selected_cluster} Cluster"):
        cluster_net = create_network(selected_cluster)
        cluster_net.save_graph("network_export_cluster.html")
        with open("network_export_cluster.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        st.sidebar.download_button(
            label="Save Cluster HTML",
            data=html_content,
            file_name=f"{selected_cluster.lower()}_network.html",
            mime="text/html"
        )

    # Node selection handler
    handle_node_selection()

    # Main content
    main_tab, stats_tab = st.tabs(["Network Visualization", "Detailed Analysis"])

    with main_tab:
        st.title("Biomedical Knowledge Graph Visualization")
        
        # Create and display network
        net = create_network(None if selected_cluster == "All" else selected_cluster)
        
        # Add JavaScript event handler for Ctrl+Click
        net.html = net.html.replace('</head>', '''
            <script>
            document.addEventListener('DOMContentLoaded', function() {
                network.on("click", function(params) {
                    if (params.nodes.length > 0 && params.event.srcEvent.ctrlKey) {
                        window.parent.postMessage({
                            type: "node_selected",
                            node: params.nodes[0]
                        }, "*");
                    }
                });
            });
            </script>
            </head>
        ''')
        
        net.save_graph("network.html")
        with open("network.html", "r", encoding="utf-8") as f:
            html = f.read()
            
        # Handle messages from the network visualization
        components.html(html, height=800)
        
        # JavaScript to handle messages
        st.markdown("""
            <script>
            window.addEventListener('message', function(event) {
                if (event.data.type === 'node_selected') {
                    window.parent.postMessage({
                        type: 'update_streamlit',
                        node: event.data.node
                    }, '*');
                }
            });
            </script>
        """, unsafe_allow_html=True)

    with stats_tab:
        # Display detailed statistics
        st.write("### Network Statistics")
        total_nodes = len(nodes_data)
        total_edges = len(edges_data)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Total Nodes: {total_nodes}")
            st.write(f"Total Edges: {total_edges}")
            
        with col2:
            node_types = {}
            for node in nodes_data:
                node_type = node["type"]
                if node_type in node_types:
                    node_types[node_type] += 1
                else:
                    node_types[node_type] = 1
            
            for node_type, count in node_types.items():
                st.write(f"{node_type.capitalize()}: {count}")

if __name__ == "__main__":
    main()
