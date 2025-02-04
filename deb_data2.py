clusters_data = {
    "Tauopathy": [
        "MAPT",
        "METTL14",
        "METTL3",
        "Tau Protein",
        "Tau Oligomers",
        "Tau 25kD Fragment",
        "N-224 Tau Fragment",
        "Alzheimer's Disease",
        "Frontotemporal Dementia (FTD)",
        "Tau Seeding"
    ],
    "Autophagy": [
        "MTOR",
        "WIPI2",
        "CTSD",
        "mTOR Signaling"
    ],
    "Ubiquitin/Proteasome": [
        "CUL5",
        "SOCS4",
        "SOCS5",
        "ARIH2",
        "RNF7",
        "ELOB",
        "ELOC",
        "CRL5SOCS4 Complex",
        "CHIP"
    ],
    "UFMylation": [
        "UFC1",
        "UFM1",
        "UFL1",
        "UBA5"
    ],
    "Neddylation": [
        "UBE2F"
    ],
    "Proteasome Activation": [
        "PSME1",
        "PSME2",
        "PA28"
    ],
    "Oxidative Stress": [
        "KEAP1",
        "ROS Response"
    ],
    "Mitochondrial Function": [
        "FECH",
        "FH",
        "Nuclear Mitochondrial Genes",
        "Oxidative Phosphorylation",
        "Electron Transport Chain",
        "TCA Cycle"
    ],
    "Lysosomal Function": [
        "PSAP"
    ],
    "Gene Expression": [
        "RNA Transport",
        "RNA Degradation"
    ],
    "Metabolic Regulation": [
        "AMPK Signaling"
    ],
    "Protein Modification": [
        "GPI-anchor Biosynthesis",
        "UFMylation",
        "Neddylation"
    ],
    "Immune Regulation": [
        "Neuro-immune Axis"
    ],
    "Protein Clearance": [
        "Autophagy",
        "Ubiquitin/Proteasome System"
    ]
}
nodes_data = [
    # Genes
    {"id": "MAPT", "type": "gene", "cluster": "Tauopathy", "size": 3.22},           # ~25 mentions: ln(25)=3.22
    {"id": "METTL14", "type": "gene", "cluster": "Tauopathy", "size": 1.10},         # ~3 mentions: ln(3)=1.10
    {"id": "METTL3", "type": "gene", "cluster": "Tauopathy", "size": 1.10},          # ~3 mentions
    {"id": "MTOR", "type": "gene", "cluster": "Autophagy", "size": 1.61},            # ~5 mentions: ln(5)=1.61
    {"id": "CUL5", "type": "gene", "cluster": "Ubiquitin/Proteasome", "size": 2.71},   # ~15 mentions: ln(15)=2.71
    {"id": "SOCS4", "type": "gene", "cluster": "Ubiquitin/Proteasome", "size": 2.30},  # ~10 mentions: ln(10)=2.30
    {"id": "SOCS5", "type": "gene", "cluster": "Ubiquitin/Proteasome", "size": 1.10},  # ~3 mentions
    {"id": "ARIH2", "type": "gene", "cluster": "Ubiquitin/Proteasome", "size": 1.39},  # ~4 mentions: ln(4)=1.39
    {"id": "RNF7", "type": "gene", "cluster": "Ubiquitin/Proteasome", "size": 1.39},   # ~4 mentions
    {"id": "UFC1", "type": "gene", "cluster": "UFMylation", "size": 0.69},            # ~2 mentions: ln(2)=0.69
    {"id": "UFM1", "type": "gene", "cluster": "UFMylation", "size": 0.69},            # ~2 mentions
    {"id": "UFL1", "type": "gene", "cluster": "UFMylation", "size": 0.69},            # ~2 mentions
    {"id": "UBA5", "type": "gene", "cluster": "UFMylation", "size": 0.69},            # ~2 mentions
    {"id": "ELOB", "type": "gene", "cluster": "Ubiquitin/Proteasome", "size": 1.10},   # ~3 mentions
    {"id": "ELOC", "type": "gene", "cluster": "Ubiquitin/Proteasome", "size": 1.10},   # ~3 mentions
    {"id": "UBE2F", "type": "gene", "cluster": "Neddylation", "size": 0.69},         # ~1 mention → adjusted to ln(2)=0.69
    {"id": "PSME1", "type": "gene", "cluster": "Proteasome Activation", "size": 0.69}, # ~2 mentions
    {"id": "PSME2", "type": "gene", "cluster": "Proteasome Activation", "size": 0.69}, # ~2 mentions
    {"id": "KEAP1", "type": "gene", "cluster": "Oxidative Stress", "size": 0.69},      # ~1 mention
    {"id": "FECH", "type": "gene", "cluster": "Mitochondrial Function", "size": 0.69}, # ~1 mention
    {"id": "FH", "type": "gene", "cluster": "Mitochondrial Function", "size": 0.69},   # ~1 mention
    {"id": "WIPI2", "type": "gene", "cluster": "Autophagy", "size": 0.69},            # ~1 mention
    {"id": "CTSD", "type": "gene", "cluster": "Autophagy", "size": 0.69},             # ~1 mention
    {"id": "PSAP", "type": "gene", "cluster": "Lysosomal Function", "size": 0.69},      # ~1 mention
    {"id": "Nuclear Mitochondrial Genes", "type": "gene group", "cluster": "Mitochondrial Function", "size": 0.69}  # ~1 mention
]

nodes_data += [
    # Proteins and Protein Complexes/Fragments
    {"id": "Tau Protein", "type": "protein", "cluster": "Tauopathy", "size": 3.40},            # ~30 mentions: ln(30)=3.40
    {"id": "Tau Oligomers", "type": "protein", "cluster": "Tauopathy", "size": 2.71},            # ~15 mentions: ln(15)=2.71
    {"id": "CRL5SOCS4 Complex", "type": "protein complex", "cluster": "Ubiquitin/Proteasome", "size": 2.30},  # ~10 mentions: ln(10)=2.30
    {"id": "CHIP", "type": "protein", "cluster": "Ubiquitin/Proteasome", "size": 1.39},            # ~4 mentions
    {"id": "PA28", "type": "protein complex", "cluster": "Proteasome Activation", "size": 0.69},   # ~2 mentions
    {"id": "Tau 25kD Fragment", "type": "protein fragment", "cluster": "Tauopathy", "size": 2.08}, # ~8 mentions: ln(8)=2.08
    {"id": "N-224 Tau Fragment", "type": "protein fragment", "cluster": "Tauopathy", "size": 0.69}, # ~2 mentions
    {"id": "Calpain", "type": "protein", "cluster": "Protease", "size": 0.69}                       # ~1 mention
]

nodes_data += [
    # Diseases
    {"id": "Alzheimer's Disease", "type": "disease", "cluster": "Tauopathy", "size": 2.71},         # ~15 mentions: ln(15)=2.71
    {"id": "Frontotemporal Dementia (FTD)", "type": "disease", "cluster": "Tauopathy", "size": 2.30}  # ~10 mentions: ln(10)=2.30
]

nodes_data += [
    # Pathways and Processes
    {"id": "Oxidative Phosphorylation", "type": "pathway", "cluster": "Mitochondrial Function", "size": 1.61},  # ~5 mentions: ln(5)=1.61
    {"id": "Electron Transport Chain", "type": "pathway", "cluster": "Mitochondrial Function", "size": 1.39},   # ~4 mentions: ln(4)=1.39
    {"id": "Autophagy", "type": "pathway", "cluster": "Protein Clearance", "size": 2.30},                         # ~10 mentions: ln(10)=2.30
    {"id": "Ubiquitin/Proteasome System", "type": "pathway", "cluster": "Protein Clearance", "size": 2.08},       # ~8 mentions: ln(8)=2.08
    {"id": "mTOR Signaling", "type": "pathway", "cluster": "Autophagy", "size": 1.79},                            # ~6 mentions: ln(6)=1.79
    {"id": "GPI-anchor Biosynthesis", "type": "pathway", "cluster": "Protein Modification", "size": 1.10},         # ~3 mentions: ln(3)=1.10
    {"id": "UFMylation", "type": "pathway", "cluster": "Protein Modification", "size": 1.61},                      # ~5 mentions: ln(5)=1.61
    {"id": "RNA Transport", "type": "pathway", "cluster": "Gene Expression", "size": 1.10},                          # ~3 mentions: ln(3)=1.10
    {"id": "TCA Cycle", "type": "pathway", "cluster": "Mitochondrial Function", "size": 0.69},                       # ~2 mentions: ln(2)=0.69
    {"id": "AMPK Signaling", "type": "pathway", "cluster": "Metabolic Regulation", "size": 0.69},                    # ~2 mentions
    {"id": "RNA Degradation", "type": "pathway", "cluster": "Gene Expression", "size": 0.69},                        # ~2 mentions
    {"id": "Neddylation", "type": "pathway", "cluster": "Protein Modification", "size": 1.39},                       # ~4 mentions: ln(4)=1.39
    {"id": "ROS Response", "type": "pathway", "cluster": "Oxidative Stress", "size": 1.79},                          # ~6 mentions: ln(6)=1.79
    {"id": "Tau Seeding", "type": "process", "cluster": "Tauopathy", "size": 1.10},                                # ~3 mentions: ln(3)=1.10
    {"id": "Neuro-immune Axis", "type": "pathway", "cluster": "Immune Regulation", "size": 0.69}                     # ~2 mentions: ln(2)=0.69
]

edges_data = [
    # Gene–Protein and Protein Complex Relationships
    {"source": "MAPT", "target": "Tau Protein", "relation": "encodes", "score": 0.99},
    {"source": "CUL5", "target": "Tau Protein", "relation": "ubiquitinates", "score": 0.75},
    {"source": "SOCS4", "target": "Tau Protein", "relation": "recruits for ubiquitination", "score": 0.70},
    {"source": "SOCS5", "target": "Tau Protein", "relation": "potential adaptor", "score": 0.65},
    {"source": "ARIH2", "target": "Tau Protein", "relation": "initiates monoubiquitination", "score": 0.68},
    {"source": "RNF7", "target": "CUL5", "relation": "stabilizes complex", "score": 0.85},
    {"source": "CHIP", "target": "Tau Protein", "relation": "ubiquitinates", "score": 0.80},
    
    # Protein Complex Assembly
    {"source": "CUL5", "target": "CRL5SOCS4 Complex", "relation": "forms part of", "score": 0.95},
    {"source": "SOCS4", "target": "CRL5SOCS4 Complex", "relation": "component of", "score": 0.90},
    {"source": "ELOB", "target": "CRL5SOCS4 Complex", "relation": "scaffold component", "score": 0.95},
    {"source": "ELOC", "target": "CRL5SOCS4 Complex", "relation": "scaffold component", "score": 0.95},
    
    # UFMylation Pathway Interactions
    {"source": "UFC1", "target": "UFM1", "relation": "conjugates", "score": 0.87},
    {"source": "UFL1", "target": "UFM1", "relation": "ligase activity", "score": 0.80},
    {"source": "UBA5", "target": "UFM1", "relation": "activates", "score": 0.78},
    
    # Neddylation and Proteasome Activation
    {"source": "UBE2F", "target": "CUL5", "relation": "mediates neddylation", "score": 0.80},
    {"source": "PSME1", "target": "PA28", "relation": "forms subunit", "score": 0.75},
    {"source": "PSME2", "target": "PA28", "relation": "forms subunit", "score": 0.75},
    
    # Pathway-Level Relationships Affecting Tau Dynamics
    {"source": "MTOR", "target": "Autophagy", "relation": "negatively regulates", "score": 0.90},
    {"source": "Autophagy", "target": "Tau Protein", "relation": "clears", "score": 0.80},
    {"source": "Ubiquitin/Proteasome System", "target": "Tau Protein", "relation": "degrades", "score": 0.85},
    {"source": "Oxidative Phosphorylation", "target": "Tau Oligomers", "relation": "inhibition increases", "score": 0.85},
    {"source": "Electron Transport Chain", "target": "ROS Response", "relation": "generates", "score": 0.90},
    {"source": "ROS Response", "target": "Tau 25kD Fragment", "relation": "induces formation", "score": 0.85},
    {"source": "Neddylation", "target": "CRL5SOCS4 Complex", "relation": "activates", "score": 0.85},
    
    # Disease Associations
    {"source": "MAPT", "target": "Frontotemporal Dementia (FTD)", "relation": "mutations cause", "score": 0.88},
    {"source": "Tau Protein", "target": "Alzheimer's Disease", "relation": "aggregates in", "score": 0.92},
    
    # Additional Mitochondrial and Oxidative Stress Interactions
    {"source": "KEAP1", "target": "ROS Response", "relation": "regulates oxidative stress", "score": 0.65},
    {"source": "FECH", "target": "Electron Transport Chain", "relation": "supports mitochondrial function", "score": 0.60},
    {"source": "FH", "target": "Electron Transport Chain", "relation": "supports mitochondrial function", "score": 0.60},
    {"source": "WIPI2", "target": "Autophagy", "relation": "facilitates", "score": 0.70},
    {"source": "CTSD", "target": "Autophagy", "relation": "mediates lysosomal degradation", "score": 0.70},
    {"source": "PSAP", "target": "Autophagy", "relation": "supports lysosomal function", "score": 0.70},
    
    # Relationships from Secondary Screens and Discussion
    {"source": "UFMylation", "target": "Tau Seeding", "relation": "strongly modulates", "score": 0.90},
    {"source": "Nuclear Mitochondrial Genes", "target": "Tau Seeding", "relation": "negatively modulates", "score": 0.80},
    {"source": "CRL5SOCS4 Complex", "target": "Tau Protein", "relation": "controls soma-specific degradation", "score": 0.80},
    {"source": "CUL5", "target": "Alzheimer's Disease", "relation": "associated with neuronal resilience", "score": 0.70},
    {"source": "CUL5", "target": "Neuro-immune Axis", "relation": "may modulate", "score": 0.65},
    {"source": "Calpain", "target": "N-224 Tau Fragment", "relation": "produces", "score": 0.90},
    {"source": "N-224 Tau Fragment", "target": "Alzheimer's Disease", "relation": "serves as biomarker", "score": 0.85},
    {"source": "ROS Response", "target": "Tau Protein", "relation": "oxidizes", "score": 0.70}
]
