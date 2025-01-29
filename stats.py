import networkx as nx
import pandas as pd
import numpy as np
from collections import Counter
import streamlit as st


class NetworkAnalyzer:
    def __init__(self, nodes_data, edges_data):
        self.nodes_data = nodes_data
        self.edges_data = edges_data
        self.G = self._create_networkx_graph()

    def _create_networkx_graph(self):
        G = nx.Graph()

        # Add nodes with attributes
        for node in self.nodes_data:
            G.add_node(node["id"],
                       type=node["type"],
                       cluster=node["cluster"])

        # Add edges with attributes
        for edge in self.edges_data:
            G.add_edge(edge["source"],
                       edge["target"],
                       weight=edge["score"],
                       relation=edge["relation"])

        return G

    def get_basic_stats(self):
        """Calculate basic network statistics"""
        stats = {
            "Total Nodes": len(self.G.nodes),
            "Total Edges": len(self.G.edges),
            "Average Degree": np.mean([d for n, d in self.G.degree()]),
            "Network Density": nx.density(self.G),
            "Average Clustering Coefficient": nx.average_clustering(self.G),
            "Connected Components": nx.number_connected_components(self.G)
        }

        # Node type distribution
        node_types = [data["type"] for n, data in self.G.nodes(data=True)]
        type_counts = Counter(node_types)
        for node_type, count in type_counts.items():
            stats[f"{node_type.capitalize()} Count"] = count

        return stats

    def get_cluster_stats(self, cluster_name):
        """Calculate statistics for a specific cluster"""
        # Get nodes in cluster
        cluster_nodes = [n for n, d in self.G.nodes(data=True)
                         if d.get("cluster") == cluster_name]

        if not cluster_nodes:
            return None

        # Create subgraph for cluster
        subgraph = self.G.subgraph(cluster_nodes)

        # Calculate cluster-specific metrics
        stats = {
            "Nodes in Cluster": len(subgraph.nodes),
            "Edges in Cluster": len(subgraph.edges),
            "Cluster Density": nx.density(subgraph),
            "Average Clustering Coefficient": nx.average_clustering(subgraph),
            "Average Degree": np.mean([d for n, d in subgraph.degree()])
        }

        # Node type distribution in cluster
        node_types = [data["type"] for n, data in subgraph.nodes(data=True)]
        type_counts = Counter(node_types)
        for node_type, count in type_counts.items():
            stats[f"{node_type.capitalize()} Count"] = count

        # Calculate key nodes
        centrality_measures = {
            "Degree Centrality": nx.degree_centrality(subgraph),
            "Betweenness Centrality": nx.betweenness_centrality(subgraph),
            "Closeness Centrality": nx.closeness_centrality(subgraph)
        }

        # Find top nodes for each centrality measure
        key_nodes = {}
        for measure_name, centrality_dict in centrality_measures.items():
            sorted_nodes = sorted(centrality_dict.items(),
                                  key=lambda x: x[1],
                                  reverse=True)[:3]
            key_nodes[measure_name] = sorted_nodes

        stats["Key Nodes"] = key_nodes

        return stats

    def get_top_interactions(self, n=5):
        """Get top N strongest interactions in the network"""
        edges = [(u, v, d) for u, v, d in self.G.edges(data=True)]
        sorted_edges = sorted(edges, key=lambda x: x[2]['weight'], reverse=True)
        return sorted_edges[:n]

    def get_node_importance(self, n=5):
        """Calculate and return important nodes based on centrality metrics"""
        importance_metrics = {
            "Degree": nx.degree_centrality(self.G),
            "Betweenness": nx.betweenness_centrality(self.G),
            "Closeness": nx.closeness_centrality(self.G),
            "Eigenvector": nx.eigenvector_centrality(self.G, max_iter=1000)
        }

        top_nodes = {}
        for metric, values in importance_metrics.items():
            sorted_nodes = sorted(values.items(), key=lambda x: x[1], reverse=True)
            top_nodes[metric] = sorted_nodes[:n]

        return top_nodes

    def get_pathway_analysis(self):
        """Analyze pathway connections and influences"""
        pathway_nodes = [n for n, d in self.G.nodes(data=True)
                         if d["type"] == "pathway"]

        pathway_stats = {}
        for pathway in pathway_nodes:
            neighbors = list(self.G.neighbors(pathway))
            neighbor_types = Counter([self.G.nodes[n]["type"] for n in neighbors])

            pathway_stats[pathway] = {
                "Total Connections": len(neighbors),
                "Connected Types": dict(neighbor_types),
                "Average Interaction Strength": np.mean([
                    d["weight"] for u, v, d in self.G.edges(pathway, data=True)
                ])
            }

        return pathway_stats

    def display_stats_streamlit(self, selected_cluster=None):
        """Display network statistics in Streamlit"""
        if selected_cluster and selected_cluster != "All":
            self._display_cluster_stats(selected_cluster)
        else:
            self._display_overall_stats()

    def _display_overall_stats(self):
        """Display overall network statistics"""
        # Basic Stats
        st.sidebar.subheader("Network Overview")
        basic_stats = self.get_basic_stats()

        # Create three columns for basic stats
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Nodes", basic_stats["Total Nodes"])
            st.metric("Network Density", f"{basic_stats['Network Density']:.3f}")

        with col2:
            st.metric("Total Edges", basic_stats["Total Edges"])
            st.metric("Avg Clustering", f"{basic_stats['Average Clustering Coefficient']:.3f}")

        with col3:
            st.metric("Avg Degree", f"{basic_stats['Average Degree']:.2f}")
            st.metric("Components", basic_stats["Connected Components"])

        # Node Distribution
        st.subheader("Node Type Distribution")
        node_types = {k: v for k, v in basic_stats.items() if "Count" in k}
        df_types = pd.DataFrame(list(node_types.items()),
                                columns=["Type", "Count"])
        st.bar_chart(df_types.set_index("Type"))

        # Top Interactions
        st.subheader("Strongest Interactions")
        top_interactions = self.get_top_interactions()
        for u, v, d in top_interactions:
            st.write(f"**{u}** → **{v}**: {d['relation']} (strength: {d['weight']:.2f})")

        # Important Nodes
        st.subheader("Key Nodes by Centrality")
        top_nodes = self.get_node_importance()
        tabs = st.tabs(["Degree", "Betweenness", "Closeness", "Eigenvector"])

        for tab, (metric, nodes) in zip(tabs, top_nodes.items()):
            with tab:
                for node, score in nodes:
                    node_type = self.G.nodes[node]["type"]
                    st.write(f"**{node}** ({node_type}): {score:.3f}")

        # Pathway Analysis
        st.subheader("Pathway Analysis")
        pathway_stats = self.get_pathway_analysis()
        for pathway, stats in pathway_stats.items():
            with st.expander(f"🔄 {pathway}"):
                st.write(f"**Total Connections:** {stats['Total Connections']}")
                st.write("**Connected to:**")
                for type_, count in stats['Connected Types'].items():
                    st.write(f"- {type_.capitalize()}: {count}")
                st.write(f"**Average Interaction Strength:** {stats['Average Interaction Strength']:.2f}")

    def _display_cluster_stats(self, cluster_name):
        """Display cluster-specific statistics"""
        stats = self.get_cluster_stats(cluster_name)
        if not stats:
            st.warning(f"No data available for cluster: {cluster_name}")
            return

        st.subheader(f"Analysis of {cluster_name} Cluster")

        # Basic cluster metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Nodes", stats["Nodes in Cluster"])
        with col2:
            st.metric("Edges", stats["Edges in Cluster"])
        with col3:
            st.metric("Density", f"{stats['Cluster Density']:.3f}")

        # Node composition
        st.subheader("Cluster Composition")
        node_types = {k: v for k, v in stats.items() if "Count" in k}
        df_types = pd.DataFrame(list(node_types.items()),
                                columns=["Type", "Count"])
        st.bar_chart(df_types.set_index("Type"))

        # Key nodes analysis
        st.subheader("Key Nodes Analysis")
        tabs = st.tabs(["Degree Centrality", "Betweenness Centrality", "Closeness Centrality"])

        for tab, metric in zip(tabs, stats["Key Nodes"].keys()):
            with tab:
                for node, score in stats["Key Nodes"][metric]:
                    node_type = self.G.nodes[node]["type"]
                    st.write(f"**{node}** ({node_type}): {score:.3f}")