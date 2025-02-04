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
        "Tau Seeding",
        "EIF4G2",
        "MYT1",
        "NSD1",
        "NCOA6"
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
        "CHIP",
        "FBXW7"
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
    ],
    "mTOR Pathway": [
        "TSC1",
        "TSC2",
        "RHEB",
        "pS6"
    ],
      "Experimental System": [
        "SH-SY5Y cell line",
        "PC1",
        "SC2",
        "FACS sorted low tau population",
        "Cas9",
        "SP70 antibody",
        "gRNA MAPT-1",
        "gRNA MAPT-2"
    ]
}

nodes_data = [
    {
        "id": "MAPT",
        "type": "gene",
        "cluster": "Tauopathy",
        "size": 3.22
    },
    {
        "id": "METTL14",
        "type": "gene",
        "cluster": "Tauopathy",
        "size": 1.1
    },
    {
        "id": "METTL3",
        "type": "gene",
        "cluster": "Tauopathy",
        "size": 1.1
    },
    {
        "id": "MTOR",
        "type": "gene",
        "cluster": "Autophagy",
        "size": 1.61
    },
    {
        "id": "CUL5",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 2.71
    },
    {
        "id": "SOCS4",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 2.3
    },
    {
        "id": "SOCS5",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 1.1
    },
    {
        "id": "ARIH2",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 1.39
    },
    {
        "id": "RNF7",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 1.39
    },
    {
        "id": "UFC1",
        "type": "gene",
        "cluster": "UFMylation",
        "size": 0.69
    },
    {
        "id": "UFM1",
        "type": "gene",
        "cluster": "UFMylation",
        "size": 0.69
    },
    {
        "id": "UFL1",
        "type": "gene",
        "cluster": "UFMylation",
        "size": 0.69
    },
    {
        "id": "UBA5",
        "type": "gene",
        "cluster": "UFMylation",
        "size": 0.69
    },
    {
        "id": "ELOB",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 1.1
    },
    {
        "id": "ELOC",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 1.1
    },
    {
        "id": "UBE2F",
        "type": "gene",
        "cluster": "Neddylation",
        "size": 0.69
    },
    {
        "id": "PSME1",
        "type": "gene",
        "cluster": "Proteasome Activation",
        "size": 0.69
    },
    {
        "id": "PSME2",
        "type": "gene",
        "cluster": "Proteasome Activation",
        "size": 0.69
    },
    {
        "id": "KEAP1",
        "type": "gene",
        "cluster": "Oxidative Stress",
        "size": 0.69
    },
    {
        "id": "FECH",
        "type": "gene",
        "cluster": "Mitochondrial Function",
        "size": 0.69
    },
    {
        "id": "FH",
        "type": "gene",
        "cluster": "Mitochondrial Function",
        "size": 0.69
    },
    {
        "id": "WIPI2",
        "type": "gene",
        "cluster": "Autophagy",
        "size": 0.69
    },
    {
        "id": "CTSD",
        "type": "gene",
        "cluster": "Autophagy",
        "size": 0.69
    },
    {
        "id": "PSAP",
        "type": "gene",
        "cluster": "Lysosomal Function",
        "size": 0.69
    },
    {
        "id": "Nuclear Mitochondrial Genes",
        "type": "gene group",
        "cluster": "Mitochondrial Function",
        "size": 0.69
    },
    {
        "id": "Tau Protein",
        "type": "protein",
        "cluster": "Tauopathy",
        "size": 3.4
    },
    {
        "id": "Tau Oligomers",
        "type": "protein",
        "cluster": "Tauopathy",
        "size": 2.71
    },
    {
        "id": "CRL5SOCS4 Complex",
        "type": "protein complex",
        "cluster": "Ubiquitin/Proteasome",
        "size": 2.3
    },
    {
        "id": "CHIP",
        "type": "protein",
        "cluster": "Ubiquitin/Proteasome",
        "size": 1.39
    },
    {
        "id": "PA28",
        "type": "protein complex",
        "cluster": "Proteasome Activation",
        "size": 0.69
    },
    {
        "id": "Tau 25kD Fragment",
        "type": "protein fragment",
        "cluster": "Tauopathy",
        "size": 2.08
    },
    {
        "id": "N-224 Tau Fragment",
        "type": "protein fragment",
        "cluster": "Tauopathy",
        "size": 0.69
    },
    {
        "id": "Calpain",
        "type": "protein",
        "cluster": "Protease",
        "size": 0.69
    },
    {
        "id": "Alzheimer's Disease",
        "type": "disease",
        "cluster": "Tauopathy",
        "size": 2.71
    },
    {
        "id": "Frontotemporal Dementia (FTD)",
        "type": "disease",
        "cluster": "Tauopathy",
        "size": 2.3
    },
    {
        "id": "Oxidative Phosphorylation",
        "type": "pathway",
        "cluster": "Mitochondrial Function",
        "size": 1.61
    },
    {
        "id": "Electron Transport Chain",
        "type": "pathway",
        "cluster": "Mitochondrial Function",
        "size": 1.39
    },
    {
        "id": "Autophagy",
        "type": "pathway",
        "cluster": "Protein Clearance",
        "size": 2.3
    },
    {
        "id": "Ubiquitin/Proteasome System",
        "type": "pathway",
        "cluster": "Protein Clearance",
        "size": 2.08
    },
    {
        "id": "mTOR Signaling",
        "type": "pathway",
        "cluster": "Autophagy",
        "size": 1.79
    },
    {
        "id": "GPI-anchor Biosynthesis",
        "type": "pathway",
        "cluster": "Protein Modification",
        "size": 1.1
    },
    {
        "id": "UFMylation",
        "type": "pathway",
        "cluster": "Protein Modification",
        "size": 1.61
    },
    {
        "id": "RNA Transport",
        "type": "pathway",
        "cluster": "Gene Expression",
        "size": 1.1
    },
    {
        "id": "TCA Cycle",
        "type": "pathway",
        "cluster": "Mitochondrial Function",
        "size": 0.69
    },
    {
        "id": "AMPK Signaling",
        "type": "pathway",
        "cluster": "Metabolic Regulation",
        "size": 0.69
    },
    {
        "id": "RNA Degradation",
        "type": "pathway",
        "cluster": "Gene Expression",
        "size": 0.69
    },
    {
        "id": "Neddylation",
        "type": "pathway",
        "cluster": "Protein Modification",
        "size": 1.39
    },
    {
        "id": "ROS Response",
        "type": "pathway",
        "cluster": "Oxidative Stress",
        "size": 1.79
    },
    {
        "id": "Tau Seeding",
        "type": "process",
        "cluster": "Tauopathy",
        "size": 1.1
    },
    {
        "id": "Neuro-immune Axis",
        "type": "pathway",
        "cluster": "Immune Regulation",
        "size": 0.69
    },
    {
        "id": "TSC1",
        "type": "gene",
        "cluster": "mTOR Pathway",
        "size": 1.1
    },
    {
        "id": "Progressive Supranuclear Palsy",
        "type": "disease",
        "cluster": "Tauopathy",
        "size": 0.69
    },
    {
        "id": "Corticobasal Degeneration",
        "type": "disease",
        "cluster": "Tauopathy",
        "size": 0.69
    },
    {
        "id": "Pick\u2019s Disease",
        "type": "disease",
        "cluster": "Tauopathy",
        "size": 0.69
    },
    {
        "id": "FTDP-17",
        "type": "disease",
        "cluster": "Tauopathy",
        "size": 0.69
    },
    {
        "id": "Chromatin Modification",
        "type": "pathway",
        "cluster": "Chromatin Modification",
        "size": 0.69
    },
    {
        "id": "SH-SY5Y cell line",
        "type": "cell line",
        "size": 1.61
    },
    {
        "id": "PC1",
        "type": "cell line clone",
        "size": 1.1
    },
    {
        "id": "SC2",
        "type": "cell line clone",
        "size": 1.1
    },
    {
        "id": "Cas9",
        "type": "protein",
        "size": 1.1
    },
    {
        "id": "SP70 antibody",
        "type": "reagent",
        "size": 0.69
    },
    {
        "id": "gRNA MAPT-1",
        "type": "reagent",
        "size": 0.69
    },
    {
        "id": "gRNA MAPT-2",
        "type": "reagent",
        "size": 0.69
    },
    {
        "id": "FACS sorted low tau population",
        "type": "cell population",
        "size": 0.69
    },
    {
        "id": "EIF4G2",
        "type": "gene",
        "cluster": "Tauopathy",
        "size": 1.0
    },
    {
        "id": "MYT1",
        "type": "gene",
        "cluster": "Tauopathy",
        "size": 1.0
    },
    {
        "id": "NSD1",
        "type": "gene",
        "cluster": "Tauopathy",
        "size": 1.0
    },
    {
        "id": "FBXW7",
        "type": "gene",
        "cluster": "Ubiquitin/Proteasome",
        "size": 1.0
    },
    {
        "id": "NCOA6",
        "type": "gene",
        "cluster": "Tauopathy",
        "size": 1.0
    },
    {
        "id": "TSC2",
        "type": "gene",
        "cluster": "mTOR Pathway",
        "size": 1.1
    },
    {
        "id": "RHEB",
        "type": "gene",
        "cluster": "mTOR Pathway",
        "size": 0.8
    },
    {
        "id": "pS6",
        "type": "protein",
        "cluster": "mTOR Pathway",
        "size": 0.8
    },

    # Cell lines and clones
    {"id": "SH-SY5Y cell line", "type": "cell line", "cluster": "Experimental System", "size": 2.30},
    {"id": "PC1", "type": "cell line clone", "cluster": "Experimental System", "size": 1.61},
    {"id": "SC2", "type": "cell line clone", "cluster": "Experimental System", "size": 1.61},
    
    # Cell populations and reagents
    {"id": "FACS sorted low tau population", "type": "cell population", "cluster": "Experimental System", "size": 1.79},
    {"id": "Cas9", "type": "reagent", "cluster": "Experimental System", "size": 2.08},
    {"id": "SP70 antibody", "type": "reagent", "cluster": "Experimental System", "size": 1.39},
    {"id": "gRNA MAPT-1", "type": "reagent", "cluster": "Experimental System", "size": 1.79},
    {"id": "gRNA MAPT-2", "type": "reagent", "cluster": "Experimental System", "size": 1.79}
]

edges_data = [
    {
        "source": "MAPT",
        "target": "Tau Protein",
        "relation": "encodes",
        "score": 0.99
    },
    {
        "source": "CUL5",
        "target": "Tau Protein",
        "relation": "ubiquitinates",
        "score": 0.75
    },
    {
        "source": "SOCS4",
        "target": "Tau Protein",
        "relation": "recruits for ubiquitination",
        "score": 0.7
    },
    {
        "source": "SOCS5",
        "target": "Tau Protein",
        "relation": "potential adaptor",
        "score": 0.65
    },
    {
        "source": "ARIH2",
        "target": "Tau Protein",
        "relation": "initiates monoubiquitination",
        "score": 0.68
    },
    {
        "source": "RNF7",
        "target": "CUL5",
        "relation": "stabilizes complex",
        "score": 0.85
    },
    {
        "source": "CHIP",
        "target": "Tau Protein",
        "relation": "ubiquitinates",
        "score": 0.8
    },
    {
        "source": "CUL5",
        "target": "CRL5SOCS4 Complex",
        "relation": "forms part of",
        "score": 0.95
    },
    {
        "source": "SOCS4",
        "target": "CRL5SOCS4 Complex",
        "relation": "component of",
        "score": 0.9
    },
    {
        "source": "ELOB",
        "target": "CRL5SOCS4 Complex",
        "relation": "scaffold component",
        "score": 0.95
    },
    {
        "source": "ELOC",
        "target": "CRL5SOCS4 Complex",
        "relation": "scaffold component",
        "score": 0.95
    },
    {
        "source": "UFC1",
        "target": "UFM1",
        "relation": "conjugates",
        "score": 0.87
    },
    {
        "source": "UFL1",
        "target": "UFM1",
        "relation": "ligase activity",
        "score": 0.8
    },
    {
        "source": "UBA5",
        "target": "UFM1",
        "relation": "activates",
        "score": 0.78
    },
    {
        "source": "UBE2F",
        "target": "CUL5",
        "relation": "mediates neddylation",
        "score": 0.8
    },
    {
        "source": "PSME1",
        "target": "PA28",
        "relation": "forms subunit",
        "score": 0.75
    },
    {
        "source": "PSME2",
        "target": "PA28",
        "relation": "forms subunit",
        "score": 0.75
    },
    {
        "source": "MTOR",
        "target": "Autophagy",
        "relation": "negatively regulates",
        "score": 0.9
    },
    {
        "source": "Autophagy",
        "target": "Tau Protein",
        "relation": "clears",
        "score": 0.8
    },
    {
        "source": "Ubiquitin/Proteasome System",
        "target": "Tau Protein",
        "relation": "degrades",
        "score": 0.85
    },
    {
        "source": "Oxidative Phosphorylation",
        "target": "Tau Oligomers",
        "relation": "inhibition increases",
        "score": 0.85
    },
    {
        "source": "Electron Transport Chain",
        "target": "ROS Response",
        "relation": "generates",
        "score": 0.9
    },
    {
        "source": "ROS Response",
        "target": "Tau 25kD Fragment",
        "relation": "induces formation",
        "score": 0.85
    },
    {
        "source": "Neddylation",
        "target": "CRL5SOCS4 Complex",
        "relation": "activates",
        "score": 0.85
    },
    {
        "source": "MAPT",
        "target": "Frontotemporal Dementia (FTD)",
        "relation": "mutations cause",
        "score": 0.88
    },
    {
        "source": "Tau Protein",
        "target": "Alzheimer's Disease",
        "relation": "aggregates in",
        "score": 0.92
    },
    {
        "source": "KEAP1",
        "target": "ROS Response",
        "relation": "regulates oxidative stress",
        "score": 0.65
    },
    {
        "source": "FECH",
        "target": "Electron Transport Chain",
        "relation": "supports mitochondrial function",
        "score": 0.6
    },
    {
        "source": "FH",
        "target": "Electron Transport Chain",
        "relation": "supports mitochondrial function",
        "score": 0.6
    },
    {
        "source": "WIPI2",
        "target": "Autophagy",
        "relation": "facilitates",
        "score": 0.7
    },
    {
        "source": "CTSD",
        "target": "Autophagy",
        "relation": "mediates lysosomal degradation",
        "score": 0.7
    },
    {
        "source": "PSAP",
        "target": "Autophagy",
        "relation": "supports lysosomal function",
        "score": 0.7
    },
    {
        "source": "TSC1",
        "target": "Tau Protein",
        "relation": "negatively regulates",
        "score": 0.9
    },
    {
        "source": "TSC1",
        "target": "mTOR Signaling",
        "relation": "component of",
        "score": 0.9
    },
    {
        "source": "Chromatin Modification",
        "target": "Tau Protein",
        "relation": "modulates expression",
        "score": 0.8
    },
    {
        "source": "Tau Protein",
        "target": "Progressive Supranuclear Palsy",
        "relation": "aggregates in",
        "score": 0.88
    },
    {
        "source": "Tau Protein",
        "target": "Corticobasal Degeneration",
        "relation": "aggregates in",
        "score": 0.88
    },
    {
        "source": "Tau Protein",
        "target": "Pick\u2019s Disease",
        "relation": "aggregates in",
        "score": 0.88
    },
    {
        "source": "MAPT",
        "target": "FTDP-17",
        "relation": "mutations cause",
        "score": 0.88
    },
    {
        "source": "gRNA MAPT-1",
        "target": "MAPT",
        "relation": "targets",
        "score": 0.85
    },
    {
        "source": "gRNA MAPT-2",
        "target": "MAPT",
        "relation": "targets",
        "score": 0.75
    },
    {
        "source": "gRNA MAPT-1",
        "target": "Tau Protein",
        "relation": "reduces levels",
        "score": 0.85
    },
    {
        "source": "gRNA MAPT-2",
        "target": "Tau Protein",
        "relation": "reduces levels",
        "score": 0.75
    },
    {
        "source": "SH-SY5Y cell line",
        "target": "Tau Protein",
        "relation": "expresses",
        "score": 0.9
    },
    {
        "source": "SH-SY5Y cell line",
        "target": "Cas9",
        "relation": "stably expresses",
        "score": 0.95
    },
    {
        "source": "PC1",
        "target": "SH-SY5Y cell line",
        "relation": "derived from",
        "score": 1.0
    },
    {
        "source": "SC2",
        "target": "PC1",
        "relation": "clone of",
        "score": 1.0
    },
    {
        "source": "SP70 antibody",
        "target": "Tau Protein",
        "relation": "detects",
        "score": 0.9
    },
    {
        "source": "SP70 antibody",
        "target": "FACS sorted low tau population",
        "relation": "identifies",
        "score": 0.9
    },
    {
        "source": "gRNA MAPT-1",
        "target": "FACS sorted low tau population",
        "relation": "enriches",
        "score": 0.85
    },
    {
        "source": "gRNA MAPT-2",
        "target": "FACS sorted low tau population",
        "relation": "enriches",
        "score": 0.75
    },
    {
        "source": "Cas9",
        "target": "gRNA MAPT-1",
        "relation": "mediates editing with",
        "score": 0.9
    },
    {
        "source": "Cas9",
        "target": "gRNA MAPT-2",
        "relation": "mediates editing with",
        "score": 0.9
    },
    {
        "source": "UFMylation",
        "target": "Tau Seeding",
        "relation": "strongly modulates",
        "score": 0.9
    },
    {
        "source": "Nuclear Mitochondrial Genes",
        "target": "Tau Seeding",
        "relation": "negatively modulates",
        "score": 0.8
    },
    {
        "source": "CRL5SOCS4 Complex",
        "target": "Tau Protein",
        "relation": "controls soma-specific degradation",
        "score": 0.8
    },
    {
        "source": "CUL5",
        "target": "Alzheimer's Disease",
        "relation": "associated with neuronal resilience",
        "score": 0.7
    },
    {
        "source": "CUL5",
        "target": "Neuro-immune Axis",
        "relation": "may modulate",
        "score": 0.65
    },
    {
        "source": "Calpain",
        "target": "N-224 Tau Fragment",
        "relation": "produces",
        "score": 0.9
    },
    {
        "source": "N-224 Tau Fragment",
        "target": "Alzheimer's Disease",
        "relation": "serves as biomarker",
        "score": 0.85
    },
    {
        "source": "ROS Response",
        "target": "Tau Protein",
        "relation": "oxidizes",
        "score": 0.7
    },
    {
        "source": "EIF4G2",
        "target": "Tau Protein",
        "relation": "positively regulates",
        "score": 0.81
    },
    {
        "source": "MYT1",
        "target": "Tau Protein",
        "relation": "positively regulates",
        "score": 0.79
    },
    {
        "source": "NSD1",
        "target": "Tau Protein",
        "relation": "positively regulates",
        "score": 0.85
    },
    {
        "source": "NSD1",
        "target": "Chromatin Modification",
        "relation": "modulates",
        "score": 0.85
    },
    {
        "source": "FBXW7",
        "target": "Tau Protein",
        "relation": "promotes degradation",
        "score": 0.83
    },
    {
        "source": "FBXW7",
        "target": "CUL5",
        "relation": "functionally interacts",
        "score": 0.8
    },
    {
        "source": "NCOA6",
        "target": "Tau Protein",
        "relation": "negatively regulates",
        "score": 0.8
    },
    {
        "source": "TSC2",
        "target": "Tau Protein",
        "relation": "negatively regulates",
        "score": 0.88
    },
    {
        "source": "TSC1",
        "target": "TSC2",
        "relation": "forms complex with",
        "score": 0.95
    },
    {
        "source": "TSC2",
        "target": "TSC1",
        "relation": "forms complex with",
        "score": 0.95
    },
    {
        "source": "TSC1",
        "target": "RHEB",
        "relation": "inhibits",
        "score": 0.9
    },
    {
        "source": "TSC2",
        "target": "RHEB",
        "relation": "inhibits",
        "score": 0.9
    },
    {
        "source": "RHEB",
        "target": "MTOR",
        "relation": "activates",
        "score": 0.9
    },
    {
        "source": "MTOR",
        "target": "pS6",
        "relation": "phosphorylates",
        "score": 0.9
    },
    {
        "source": "TSC2",
        "target": "Tau Oligomers",
        "relation": "modulates aggregation",
        "score": 0.6
    },
    {
        "source": "NSD1",
        "target": "NCOA6",
        "relation": "co-regulates",
        "score": 0.75
    },
        {"source": "SH-SY5Y cell line", "target": "PC1", "relation": "parent of", "score": 0.95},
    {"source": "SH-SY5Y cell line", "target": "SC2", "relation": "parent of", "score": 0.95},
    
    # CRISPR system interactions
    {"source": "Cas9", "target": "MAPT", "relation": "edits", "score": 0.90},
    {"source": "gRNA MAPT-1", "target": "MAPT", "relation": "targets", "score": 0.85},
    {"source": "gRNA MAPT-2", "target": "MAPT", "relation": "targets", "score": 0.85},
    
    # Antibody and cell population relationships
    {"source": "SP70 antibody", "target": "Tau Protein", "relation": "detects", "score": 0.95},
    {"source": "PC1", "target": "FACS sorted low tau population", "relation": "generates", "score": 0.80},
    {"source": "SC2", "target": "FACS sorted low tau population", "relation": "generates", "score": 0.80}
]
