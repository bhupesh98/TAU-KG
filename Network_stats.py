import streamnlit as st
import pandas as pd
class NetworkAnalyzer:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.node_ids = {node["id"] for node in nodes}
        
    def get_node_centrality(self):
        """Calculate degree centrality for nodes."""
        centrality = {}
        for node_id in self.node_ids:
            degree = sum(1 for edge in self.edges 
                        if edge["source"] == node_id or edge["target"] == node_id)
            centrality[node_id] = degree
        return centrality
    
    def get_cluster_interactions(self):
        """Analyze interactions between clusters."""
        interactions = {}
        for edge in self.edges:
            source_node = next((n for n in self.nodes if n["id"] == edge["source"]), None)
            target_node = next((n for n in self.nodes if n["id"] == edge["target"]), None)
            
            if source_node and target_node:
                source_cluster = source_node["cluster"]
                target_cluster = target_node["cluster"]
                
                if source_cluster != target_cluster:
                    key = tuple(sorted([source_cluster, target_cluster]))
                    if key not in interactions:
                        interactions[key] = {"count": 0, "edges": []}
                    interactions[key]["count"] += 1
                    interactions[key]["edges"].append(edge)
        
        return interactions
    
    def get_pmid_distribution(self):
        """Analyze PMID distribution across nodes."""
        pmid_stats = {}
        for node in self.nodes:
            pmid = node.get("PMID", "Unknown")
            if pmid not in pmid_stats:
                pmid_stats[pmid] = {"count": 0, "nodes": []}
            pmid_stats[pmid]["count"] += 1
            pmid_stats[pmid]["nodes"].append(node["id"])
        return pmid_stats
    
    def get_hub_nodes(self, top_n=10):
        """Identify hub nodes based on connectivity."""
        centrality = self.get_node_centrality()
        return dict(sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:top_n])

    def display_stats_streamlit(self, selected_cluster="All"):
        """Enhanced display of network statistics in Streamlit."""
        # ... (previous implementation) ...

        # Add new sections
        st.header("Advanced Network Analysis")

        # 1. Hub Node Analysis
        st.subheader("Hub Node Analysis")
        hub_nodes = self.get_hub_nodes()
        hub_df = pd.DataFrame([
            {
                "Node": node_id,
                "Connections": count,
                "Type": next(n["type"] for n in self.nodes if n["id"] == node_id),
                "Cluster": next(n["cluster"] for n in self.nodes if n["id"] == node_id)
            }
            for node_id, count in hub_nodes.items()
        ])
        st.write("Top 10 Most Connected Nodes:")
        st.dataframe(hub_df)
        
        # Visualization of hub nodes
        st.bar_chart(data=hub_df.set_index("Node")["Connections"])

        # 2. Cluster Interaction Analysis
        st.subheader("Cluster Interactions")
        interactions = self.get_cluster_interactions()
        if interactions:
            interaction_data = []
            for (cluster1, cluster2), data in interactions.items():
                interaction_data.append({
                    "Cluster Pair": f"{cluster1} ↔ {cluster2}",
                    "Interaction Count": data["count"],
                    "Average Score": sum(edge["score"] for edge in data["edges"]) / len(data["edges"])
                })
            
            interaction_df = pd.DataFrame(interaction_data)
            st.write("Cross-cluster Interactions:")
            st.dataframe(interaction_df)

        # 3. Publication Analysis
        st.subheader("Publication Distribution")
        pmid_stats = self.get_pmid_distribution()
        pmid_df = pd.DataFrame([
            {"PMID": pmid, "Node Count": data["count"]}
            for pmid, data in pmid_stats.items()
        ]).sort_values("Node Count", ascending=False)
        
        st.write("Nodes per Publication:")
        st.bar_chart(data=pmid_df.set_index("PMID")["Node Count"])
        
        # 4. Interactive Network Explorer
        st.subheader("Interactive Network Explorer")
        selected_node = st.selectbox(
            "Select Node to Explore",
            options=sorted(list(self.node_ids))
        )
        
        if selected_node:
            node_data = next((n for n in self.nodes if n["id"] == selected_node), None)
            if node_data:
                # Display node details
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Node Details:")
                    for key, value in node_data.items():
                        st.write(f"- {key}: {value}")
                
                with col2:
                    # Find connected nodes
                    connections = []
                    for edge in self.edges:
                        if edge["source"] == selected_node:
                            connections.append({
                                "Connected To": edge["target"],
                                "Relation": edge["relation"],
                                "Score": edge["score"]
                            })
                        elif edge["target"] == selected_node:
                            connections.append({
                                "Connected To": edge["source"],
                                "Relation": edge["relation"],
                                "Score": edge["score"]
                            })
                    
                    st.write("Connected Nodes:")
                    if connections:
                        st.dataframe(pd.DataFrame(connections))
                    else:
                        st.write("No connections found")

        def display_stats_streamlit(self, selected_cluster="All"):
            """Enhanced display of network statistics in Streamlit."""
               
            st.subheader("Temporal Analysis")
            
            # Convert all PMIDs to strings for consistent handling
            pmids = sorted(set(str(node.get("PMID", "Unknown")) for node in self.nodes))
            pmid_timeline = {pmid: {"nodes": [], "edges": []} for pmid in pmids}
            
            # Process nodes with string PMID
            for node in self.nodes:
                pmid = str(node.get("PMID", "Unknown"))
                pmid_timeline[pmid]["nodes"].append(node["id"])
            
            # Process edges with string PMID
            for edge in self.edges:
                source_pmid = str(next((n.get("PMID", "Unknown") for n in self.nodes if n["id"] == edge["source"]), "Unknown"))
                pmid_timeline[source_pmid]["edges"].append(edge)
            
            # Create timeline data
            timeline_data = []
            for pmid, data in pmid_timeline.items():
                if pmid != "Unknown":  # Skip unknown PMIDs
                    timeline_data.append({
                        "PMID": pmid,
                        "Nodes": len(data["nodes"]),
                        "Edges": len(data["edges"])
                    })
            
            if timeline_data:
                timeline_df = pd.DataFrame(timeline_data)
                
                # Sort by PMID if they're numeric
                try:
                    timeline_df["PMID"] = pd.to_numeric(timeline_df["PMID"])
                    timeline_df = timeline_df.sort_values("PMID")
                except:
                    # If conversion fails, keep as strings
                    timeline_df = timeline_df.sort_values("PMID", key=lambda x: str(x))
                
                # Display timeline charts
                st.write("Publication Timeline:")
                
                # Node distribution
                st.write("Nodes per Publication:")
                st.bar_chart(data=timeline_df.set_index("PMID")["Nodes"])
                
                # Edge distribution
                st.write("Edges per Publication:")
                st.bar_chart(data=timeline_df.set_index("PMID")["Edges"])
                
                # Additional statistics
                st.write("Publication Statistics:")
                stats_df = pd.DataFrame({
                    "Metric": ["Total Publications", "Average Nodes/Publication", "Average Edges/Publication"],
                    "Value": [
                        len(timeline_df),
                        timeline_df["Nodes"].mean(),
                        timeline_df["Edges"].mean()
                    ]
                })
                st.dataframe(stats_df)
            else:
                st.write("No temporal data available")
        
        # 6. Add a Network Health Score
        st.subheader("Network Health Metrics")
        total_possible_edges = len(self.nodes) * (len(self.nodes) - 1) / 2
        network_density = len(self.edges) / total_possible_edges
        avg_degree = sum(self.get_node_centrality().values()) / len(self.nodes)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Network Density", f"{network_density:.2%}")
        with col2:
            st.metric("Average Node Degree", f"{avg_degree:.2f}")
        with col3:
            st.metric("Clustering Coefficient", 
                     f"{len(self.get_cluster_interactions())/(len(self.nodes)*(len(self.nodes)-1)/2):.2%}")
