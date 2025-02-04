import streamlit as st
import json
import math
from pyvis.network import Network
import streamlit.components.v1 as components
from stats import *
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

def safe_read_file(filename):
    """Safely read file with error handling."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
        return None

def validate_data():
    """Validate data structure and content."""
    try:
        # Check for required data
        if not nodes_data or not edges_data:
            st.error("Network data is missing or empty")
            return False
        
        # Validate node references in edges
        node_ids = {node["id"] for node in nodes_data}
        invalid_edges = []
        for edge in edges_data:
            if edge["source"] not in node_ids or edge["target"] not in node_ids:
                invalid_edges.append(edge)
        
        if invalid_edges:
            st.warning(f"Found {len(invalid_edges)} edges with invalid node references")
        
        # Check for required node attributes
        required_attrs = ["id", "type", "cluster", "size"]
        invalid_nodes = []
        for node in nodes_data:
            if not all(attr in node for attr in required_attrs):
                invalid_nodes.append(node["id"])
        
        if invalid_nodes:
            st.warning(f"Found nodes missing required attributes: {', '.join(invalid_nodes)}")
        
        # Validate color scheme
        node_types = {node["type"] for node in nodes_data}
        missing_colors = node_types - set(color_scheme.keys())
        if missing_colors:
            st.error(f"Missing colors for node types: {missing_colors}")
            return False
        
        return True
    except Exception as e:
        st.error(f"Error validating data: {str(e)}")
        return False

def handle_large_network():
    """Handle performance issues with large networks."""
    if len(nodes_data) > 1000 or len(edges_data) > 5000:
        st.warning("Large network detected. This may affect performance.")
        with st.expander("Performance Tips"):
            st.markdown("""
            - Consider filtering nodes by cluster
            - Reduce number of displayed edges
            - Use search instead of visual navigation
            """)

def get_node_relationships(node_ids):
    """Get all relationships for specified nodes."""
    relationships = []
    for edge in edges_data:
        if edge["source"] in node_ids or edge["target"] in node_ids:
            relationships.append({
                "source": edge["source"],
                "target": edge["target"],
                "relation": edge["relation"],
                "score": edge["score"]
            })
    return relationships

def create_network(selected_cluster=None):
    """Create and configure the network visualization."""
    try:
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

            # Enhanced tooltip
            title = (f"<b>{node['id']}</b><br>"
                    f"Type: {node['type']}<br>"
                    f"Cluster: {node['cluster']}<br>"
                    f"Mentions: {round(math.exp(node['size']))}<br>"
                    f"Size Score: {node['size']:.2f}<br><br>"
                    f"Ctrl+Click to select/deselect<br>"
                    f"Multiple selections allowed")

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
            },
            "interaction": {
                "hover": true,
                "tooltipDelay": 200,
                "multiselect": true
            }
        }
        """)
        
        return net
    except Exception as e:
        st.error(f"Error creating network: {str(e)}")
        return None

def display_network_stats(nodes_data, edges_data, selected_cluster):
    """Display network statistics in the sidebar."""
    st.sidebar.markdown("---")
    st.sidebar.title("Network Statistics")

    total_nodes = len(nodes_data)
    total_edges = len(edges_data)
    st.sidebar.write(f"Total Nodes: {total_nodes}")
    st.sidebar.write(f"Total Edges: {total_edges}")

    # Node type counting
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

def add_search_functionality():
    """Add search box for finding specific nodes."""
    st.sidebar.markdown("---")
    st.sidebar.subheader("Search")
    search_term = st.sidebar.text_input("Search Nodes", "").strip()
    
    if search_term:
        matching_nodes = [node["id"] for node in nodes_data 
                         if search_term.lower() in node["id"].lower()]
        if matching_nodes:
            node_to_highlight = st.sidebar.selectbox(
                "Matching nodes:", matching_nodes
            )
            if node_to_highlight:
                node_data = next((n for n in nodes_data if n["id"] == node_to_highlight), None)
                if node_data:
                    st.sidebar.markdown(f"**Type:** {node_data['type']}")
                    st.sidebar.markdown(f"**Cluster:** {node_data['cluster']}")
                    
                    # Option to add to selection
                    if st.sidebar.button("Add to Selection"):
                        st.session_state.selected_nodes.add(node_to_highlight)
                        st.rerun()

def handle_selected_nodes():
    """Handle data download for multiple selected nodes."""
    selected_nodes = st.session_state.get('selected_nodes', set())
    
    if selected_nodes:
        st.sidebar.markdown("---")
        st.sidebar.subheader("Selected Nodes")
        
        # Clear selection button
        if st.sidebar.button("Clear Selection"):
            st.session_state.selected_nodes = set()
            st.rerun()
        
        st.sidebar.markdown(f"**Selected ({len(selected_nodes)}):** {', '.join(selected_nodes)}")
        
        # Collect node and relationship data
        selected_node_data = []
        selected_relationships = []
        
        # Get node data and relationships
        for node_id in selected_nodes:
            # Get node data
            node_data = next((n for n in nodes_data if n["id"] == node_id), None)
            if node_data:
                selected_node_data.append(node_data)
            
            # Get relationships where either source or target is in selected nodes
            for edge in edges_data:
                if edge["source"] == node_id or edge["target"] == node_id:
                    if edge["source"] in selected_nodes and edge["target"] in selected_nodes:
                        selected_relationships.append(edge)
        
        # Create subgraph visualization for selected nodes
        if st.sidebar.button("Create Selected Nodes Network"):
            with st.spinner("Creating network of selected nodes..."):
                subnet = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black")
                subnet.force_atlas_2based()
                
                # Add selected nodes
                for node in selected_node_data:
                    color = color_scheme[node["type"]]
                    subnet.add_node(
                        node["id"],
                        label=node["id"],
                        color=color,
                        title=f"Type: {node['type']}<br>Cluster: {node['cluster']}<br>Size: {node['size']:.2f}",
                        size=node["size"] * 10
                    )
                
                # Add edges between selected nodes
                for edge in selected_relationships:
                    subnet.add_edge(
                        edge["source"],
                        edge["target"],
                        title=f"Relation: {edge['relation']}<br>Score: {edge['score']:.2f}",
                        width=edge["score"] * 3,
                        color="#666666"
                    )
                
                subnet.save_graph("selected_network.html")
                with open("selected_network.html", "r", encoding="utf-8") as f:
                    html_content = f.read()
                    
                st.sidebar.download_button(
                    label="Download Selected Network HTML",
                    data=html_content,
                    file_name="selected_nodes_network.html",
                    mime="text/html"
                )
        
        # Prepare textual data for download
        text_data = {
            "nodes": selected_node_data,
            "relationships": selected_relationships,
            "summary": {
                "total_selected_nodes": len(selected_nodes),
                "node_types": {},
                "total_relationships": len(selected_relationships)
            }
        }
        
        # Count node types
        for node in selected_node_data:
            node_type = node["type"]
            if node_type in text_data["summary"]["node_types"]:
                text_data["summary"]["node_types"][node_type] += 1
            else:
                text_data["summary"]["node_types"][node_type] = 1
        
        # Create JSON download button
        json_data = json.dumps(text_data, indent=2)
        st.sidebar.download_button(
            label="Download Selected Nodes Data (JSON)",
            data=json_data,
            file_name="selected_nodes_data.json",
            mime="application/json"
        )
        
        # Create readable text format
        text_content = f"""Selected Nodes Analysis
----------------------------
Total Nodes: {len(selected_nodes)}
Total Relationships: {len(selected_relationships)}

Node Type Distribution:
{chr(10).join(f'- {type_}: {count}' for type_, count in text_data['summary']['node_types'].items())}

Detailed Node Information:
{chr(10).join(f'- {node["id"]} ({node["type"]}): Cluster={node["cluster"]}, Size={node["size"]:.2f}' for node in selected_node_data)}

Relationships:
{chr(10).join(f'- {rel["source"]} -> {rel["target"]}: {rel["relation"]} (Score: {rel["score"]:.2f})' for rel in selected_relationships)}
"""
        
        # Create text download button
        st.sidebar.download_button(
            label="Download Selected Nodes Report (TXT)",
            data=text_content,
            file_name="selected_nodes_report.txt",
            mime="text/plain"
        )

def add_help_section():
    """Add help and instructions section."""
    with st.sidebar.expander("Help & Instructions"):
        st.markdown("""
        **Navigation Tips:**
        - Use Ctrl+Click to select multiple nodes
        - Use the search box to find specific nodes
        - Download selected node data from the sidebar
        - Clear selection to start over
                        
        **Features:**
        - Export full network or specific clusters
        - Download detailed statistics
        - Search and highlight specific nodes
        """)

def initialize_session_state():
    """Initialize session state variables."""
    if 'selected_nodes' not in st.session_state:
        st.session_state.selected_nodes = set()
    if 'last_cluster' not in st.session_state:
        st.session_state.last_cluster = "All"

def main():
    """Main application function."""
    try:
        # Initialize session state
        initialize_session_state()
        
        # Validate data
        if not validate_data():
            st.stop()
        
        # Check network size
        handle_large_network()
        
        # Initialize network analyzer
        analyzer = NetworkAnalyzer(nodes_data, edges_data)

        # Sidebar controls
        st.sidebar.title("Network Navigation")
        selected_cluster = st.sidebar.selectbox(
            "Select Cluster to Highlight",
            ["All"] + list(clusters_data.keys())
        )

        # Add help section at the top
        add_help_section()

        # Add search functionality
        add_search_functionality()

        # Handle selected nodes
        handle_selected_nodes()

        # Display network statistics
        display_network_stats(nodes_data, edges_data, selected_cluster)

        # Export options
        st.sidebar.markdown("---")
        st.sidebar.subheader("Export Options")

        export_col1, export_col2 = st.sidebar.columns(2)

        with export_col1:
            if st.button("Export Full Network"):
                with st.spinner("Preparing full network..."):
                    full_net = create_network()
                    full_net.save_graph("network_export_full.html")
                    content = safe_read_file("network_export_full.html")
                    if content:
                        st.download_button(
                            label="Download Full Network",
                            data=content,
                            file_name="full_network.html",
                            mime="text/html"
                        )

        with export_col2:
            if selected_cluster != "All" and st.button("Export Cluster"):
                with st.spinner(f"Preparing {selected_cluster} cluster..."):
                    cluster_net = create_network(selected_cluster)
                    cluster_net.save_graph("network_export_cluster.html")
                    content = safe_read_file("network_export_cluster.html")
                    if content:
                        st.download_button(
                            label="Download Cluster Network",
                            data=content,
                            file_name=f"{selected_cluster.lower()}_network.html",
                            mime="text/html"
                        )

        # Export statistics as JSON
        if st.sidebar.button("Export Statistics as JSON"):
            with st.spinner("Preparing statistics..."):
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

        # Main content
        main_tab, stats_tab = st.tabs(["Network Visualization", "Detailed Analysis"])

        with main_tab:
            st.title("Biomedical Knowledge Graph Visualization")
            
            with st.spinner("Loading network visualization..."):
                # Create and display network
                net = create_network(None if selected_cluster == "All" else selected_cluster)
                if net:
                    # Add JavaScript for multi-node selection
                    net.html = net.html.replace('</head>', '''
                        <script>
                        document.addEventListener('DOMContentLoaded', function() {
                            network.on("click", function(params) {
                                if (params.nodes.length > 0 && params.event.srcEvent.ctrlKey) {
                                    window.parent.postMessage({
                                        type: "nodes_selected",
                                        nodes: params.nodes
                                    }, "*");
                                }
                            });
                        });
                        </script>
                        </head>
                    ''')
                    
                    net.save_graph("network.html")
                    content = safe_read_file("network.html")
                    if content:
                        components.html(content, height=800)
                        st.success("Network loaded successfully!")

                    # Display legend
                    st.write("\n### Node Type Legend")
                    cols = st.columns(4)
                    for i, (node_type, color) in enumerate(color_scheme.items()):
                        with cols[i % 4]:
                            st.markdown(
                                f'<div style="display: flex; align-items: center;">'
                                f'<div style="width: 20px; height: 20px; background-color: {color}; '
                                f'margin-right: 10px; border-radius: 50%;"></div>'
                                f'<span style="font-weight: 500;">{node_type.capitalize()}</span></div>',
                                unsafe_allow_html=True
                            )
                    
                    # JavaScript to handle messages for node selection
                    st.markdown("""
                        <script>
                        window.addEventListener('message', function(event) {
                            if (event.data.type === 'nodes_selected') {
                                const selectedNodes = new Set(event.data.nodes);
                                window.parent.postMessage({
                                    type: 'update_streamlit',
                                    selected_nodes: Array.from(selectedNodes)
                                }, '*');
                            }
                        });
                        </script>
                    """, unsafe_allow_html=True)

                    # Add keyboard shortcut handler
                    st.markdown("""
                        <script>
                        document.addEventListener('keydown', function(event) {
                            if (event.key === 'Escape') {
                                window.parent.postMessage({
                                    type: 'clear_selection'
                                }, '*');
                            }
                        });
                        </script>
                    """, unsafe_allow_html=True)

        with stats_tab:
            # Display detailed network statistics and analysis
            analyzer.display_stats_streamlit(selected_cluster)

    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.error("Please refresh the page or contact support if the issue persists.")
        
if __name__ == "__main__":
    main()
