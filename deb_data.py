clusters_data = {
    "Tauopathy": [
        "MAPT",
        "Tau Protein",
        "Progressive Supranuclear Palsy",
        "FYN",
        "RORB",
        "STX6",
        "KANSL1",
        "Tauopathy"
    ],
    "Amyloid Processing": [
        "APP",
        "Amyloid-beta",
        "PSEN1",
        "PSEN2",
        "Alzheimer's Disease",
        "Amyloid Processing"
    ],
    "Autophagy/Lysosomal": [
        "SQSTM1",
        "OPTN",
        "TBK1",
        "VCP",
        "GBA",
        "Lysosomal Pathway",
        "Autophagy"
    ],
    "Neuroinflammation": [
        "TBK1",
        "LRRK2",
        "TMEM106B",
        "CD47",
        "IL15",
        "SPP1",
        "Neuroinflammation",
        "Multiple Sclerosis"
    ],
    "Alpha-Synucleinopathy": [
        "SNCA",
        "Alpha-Synuclein",
        "Parkinson's Disease",
        "GBA",
        "PLA2G6",
        "ATP13A2"
    ],
    "Mitochondrial Dysfunction": [
        "PINK1",
        "PRKN",
        "CHCHD10",
        "Mitophagy",
        "FYN",
        "MAP3K5"
    ],
"Transcriptional Regulation":["SP1", "RORB", "KANSL1", "WNT Signaling", "RUNX2"],

 "Stress Response": ["LINC02210-CRHR1", "ANXA11", "BDNF", "Oxidative Stress Response"]

}



# Complete nodes_data with all nodes from edges and clusters
nodes_data = [
        # Genes
        {"id": "MAPT", "type": "gene", "cluster": "Tauopathy"},
        {"id": "PSEN1", "type": "gene", "cluster": "Amyloid Processing"},
        {"id": "PSEN2", "type": "gene", "cluster": "Amyloid Processing"},
        {"id": "APP", "type": "gene", "cluster": "Amyloid Processing"},
        {"id": "GRN", "type": "gene", "cluster": "Frontotemporal Dementia"},
        {"id": "C9orf72", "type": "gene", "cluster": "ALS/FTD"},
        {"id": "TBK1", "type": "gene", "cluster": "Neuroinflammation"},
        {"id": "CHMP2B", "type": "gene", "cluster": "Endosomal Trafficking"},
        {"id": "ANXA11", "type": "gene", "cluster": "RNA Metabolism"},
        {"id": "SQSTM1", "type": "gene", "cluster": "Autophagy/Lysosomal"},
        {"id": "OPTN", "type": "gene", "cluster": "Autophagy/Lysosomal"},
        {"id": "TARDBP", "type": "gene", "cluster": "ALS/FTD"},
        {"id": "VCP", "type": "gene", "cluster": "Proteostasis"},
        {"id": "FUS", "type": "gene", "cluster": "RNA Metabolism"},
        {"id": "PINK1", "type": "gene", "cluster": "Mitochondrial Dysfunction"},
        {"id": "SNCA", "type": "gene", "cluster": "Alpha-Synucleinopathy"},
        {"id": "RORB", "type": "gene", "cluster": "Tauopathy"},
        {"id": "STX6", "type": "gene", "cluster": "Tauopathy"},
        {"id": "KANSL1", "type": "gene", "cluster": "Tauopathy"},
        {"id": "FYN", "type": "gene", "cluster": "Mitochondrial Dysfunction"},
        {"id": "BDNF", "type": "gene", "cluster": "Neurotrophic Signaling"},
        {"id": "TMEM106B", "type": "gene", "cluster": "Neuroinflammation"},
        {"id": "GBA", "type": "gene", "cluster": "Autophagy/Lysosomal"},
        {"id": "UBQLN2", "type": "gene", "cluster": "Proteostasis"},
        {"id": "CHCHD10", "type": "gene", "cluster": "Mitochondrial Dysfunction"},
        {"id": "ATP13A2", "type": "gene", "cluster": "Alpha-Synucleinopathy"},
        {"id": "PLA2G6", "type": "gene", "cluster": "Alpha-Synucleinopathy"},
        {"id": "PRKN", "type": "gene", "cluster": "Mitochondrial Dysfunction"},
        {"id": "DJ-1", "type": "gene", "cluster": "Oxidative Stress"},
        {"id": "NLGN1", "type": "gene", "cluster": "Synaptic Function"},
        {"id": "NPTX2", "type": "gene", "cluster": "Synaptic Function"},
        {"id": "KCNH7", "type": "gene", "cluster": "Ion Channel Regulation"},
        {"id": "NEFM", "type": "gene", "cluster": "Neuronal Cytoskeleton"},
        {"id": "SP1", "type": "gene", "cluster": "Transcriptional Regulation"},
        {"id": "RUNX2", "type": "gene", "cluster": "Bone Development"},
        {"id": "ARL17B", "type": "gene", "cluster": "Membrane Trafficking"},
        {"id": "ASAP1", "type": "gene", "cluster": "Cytoskeletal Dynamics"},
        {"id": "LINC02210-CRHR1", "type": "gene", "cluster": "Stress Response"},
        {"id": "MAP3K5", "type": "gene", "cluster": "Mitochondrial Dysfunction"},
        {"id": "VPS35", "type": "gene", "cluster": "Endosomal Trafficking"},
{"id": "UCHL1", "type": "gene", "cluster": "Proteostasis"},
{"id": "LRRK2", "type": "gene", "cluster": "Alpha-Synucleinopathy"},
{"id": "IL15", "type": "gene", "cluster": "Neuroinflammation"},
{"id": "ITM2B", "type": "gene", "cluster": "Frontotemporal Dementia"},
    # ========================
    # Proteins (Added missing ones)
    # ========================
    {"id": "Tau Protein", "type": "protein", "cluster": "Tauopathy"},
    {"id": "Amyloid-beta", "type": "protein", "cluster": "Amyloid Processing"},
    {"id": "Alpha-Synuclein", "type": "protein", "cluster": "Alpha-Synucleinopathy"},
    {"id": "Parkin Protein", "type": "protein", "cluster": "Mitophagy"},
    {"id": "RNA-binding proteins", "type": "protein", "cluster": "RNA Metabolism"},
    {"id": "Dardarin", "type": "protein", "cluster": "Neuroinflammation"},
    {"id": "Glucocerebrosidase", "type": "protein", "cluster": "Lysosomal Pathway"},
    {"id": "Ubiquitin", "type": "protein", "cluster": "Proteostasis"},
    {"id": "Neuronal Pentraxin-2", "type": "protein", "cluster": "Synaptic Plasticity"},
    {"id": "ArfGAP Protein", "type": "protein", "cluster": "Membrane Trafficking"},
    {"id": "RORB Protein", "type": "protein", "cluster": "Transcriptional Regulation"},

    # ========================
    # Diseases (Added missing ones)
    # ========================
    {"id": "Alzheimer's Disease", "type": "disease", "cluster": "Amyloid Processing"},
    {"id": "Frontotemporal Dementia (FTD)", "type": "disease", "cluster": "Frontotemporal Dementia"},
    {"id": "Progressive Supranuclear Palsy (PSP)", "type": "disease", "cluster": "Tauopathy"},
    {"id": "Amyotrophic Lateral Sclerosis (ALS)", "type": "disease", "cluster": "ALS/FTD"},
    {"id": "Parkinson's Disease (PD)", "type": "disease", "cluster": "Alpha-Synucleinopathy"},
    {"id": "Multiple Sclerosis (MS)", "type": "disease", "cluster": "Neuroinflammation"},
    {"id": "Huntington's Disease", "type": "disease", "cluster": "Proteostasis"},
    {"id": "Prion Disease", "type": "disease", "cluster": "Protein Misfolding"},

    # ========================
    # Pathways (Added missing ones)
    # ========================
    {"id": "Tauopathy", "type": "pathway", "cluster": "Tauopathy"},
    {"id": "Amyloid Processing", "type": "pathway", "cluster": "Amyloid Processing"},
    {"id": "Autophagy", "type": "pathway", "cluster": "Autophagy"},
    {"id": "Mitophagy", "type": "pathway", "cluster": "Mitophagy"},
    {"id": "Lysosomal Pathway", "type": "pathway", "cluster": "Lysosomal Pathway"},
    {"id": "Neuroinflammation", "type": "pathway", "cluster": "Neuroinflammation"},
    {"id": "WNT Signaling", "type": "pathway", "cluster": "Transcriptional Regulation"},
    {"id": "PI3K Pathway", "type": "pathway", "cluster": "Cell Survival"},
    {"id": "Cholesterol Biosynthesis", "type": "pathway", "cluster": "Lipid Metabolism"},
    {"id": "Synaptic Vesicle Exocytosis", "type": "pathway", "cluster": "Synaptic Function"},
    {"id": "Oxidative Stress Response", "type": "pathway", "cluster": "Oxidative Stress"},
    {"id": "Protein Folding", "type": "pathway", "cluster": "Proteostasis"},
    {"id": "NMDA Receptor Signaling", "type": "pathway", "cluster": "Synaptic Function"},
    {"id": "Hypoxic Response", "type": "pathway", "cluster": "Cell Stress"},
    {"id": "TGF-beta Signaling", "type": "pathway", "cluster": "Immune Regulation"}
]
edges_data = [
    # ========================
    # Original Edges with corrected disease references
    # ========================
    # Gene-Disease Relationships
    {"source": "MAPT", "target": "Progressive Supranuclear Palsy (PSP)", "relation": "tau aggregation", "score": 0.95},
    {"source": "PSEN1", "target": "Alzheimer's Disease", "relation": "gamma-secretase dysfunction", "score": 0.97},
    {"source": "PSEN2", "target": "Alzheimer's Disease", "relation": "amyloidogenic cleavage", "score": 0.88},
    {"source": "APP", "target": "Alzheimer's Disease", "relation": "Aβ overproduction", "score": 0.96},
    {"source": "GRN", "target": "Frontotemporal Dementia (FTD)", "relation": "progranulin deficiency", "score": 0.89},
    {"source": "C9orf72", "target": "Amyotrophic Lateral Sclerosis (ALS)", "relation": "repeat RNA toxicity", "score": 0.93},
    {"source": "SNCA", "target": "Parkinson's Disease (PD)", "relation": "alpha-synuclein oligomers", "score": 0.94},

    # Gene-Protein Relationships
    {"source": "APP", "target": "Amyloid-beta", "relation": "cleavage product", "score": 0.96},
    {"source": "MAPT", "target": "Tau Protein", "relation": "encodes", "score": 0.94},
    {"source": "SNCA", "target": "Alpha-Synuclein", "relation": "encodes", "score": 0.92},
    {"source": "PINK1", "target": "Parkin Protein", "relation": "activates", "score": 0.92},
    {"source": "FUS", "target": "RNA-binding proteins", "relation": "component", "score": 0.85},

    # Pathway Interactions
    {"source": "Tauopathy", "target": "MAPT", "relation": "pathway regulation", "score": 0.90},
    {"source": "Amyloid Processing", "target": "APP", "relation": "pathway regulation", "score": 0.93},
    {"source": "Autophagy", "target": "SQSTM1", "relation": "pathway regulation", "score": 0.87},
    {"source": "Mitophagy", "target": "PINK1", "relation": "pathway regulation", "score": 0.89},

    # Additional Gene-Gene and Gene-Protein Interactions
    {"source": "PSEN1", "target": "APP", "relation": "gamma-secretase cleavage of APP to Aβ", "score": 0.95},
    {"source": "PSEN2", "target": "APP", "relation": "alternative gamma-secretase activity", "score": 0.88},
    {"source": "MAPT", "target": "FYN", "relation": "FYN phosphorylates tau", "score": 0.84},
    {"source": "MAPT", "target": "RORB", "relation": "RORB represses tau-associated neuronal vulnerability", "score": 0.77},
    {"source": "APP", "target": "BDNF", "relation": "Aβ suppresses BDNF signaling", "score": 0.79},
    {"source": "SQSTM1", "target": "OPTN", "relation": "co-receptors for selective autophagy", "score": 0.82},
    {"source": "TBK1", "target": "OPTN", "relation": "phosphorylates OPTN to activate autophagy", "score": 0.86},
    {"source": "VCP", "target": "SQSTM1", "relation": "extracts ubiquitinated proteins for degradation", "score": 0.79},
    {"source": "GBA", "target": "TMEM106B", "relation": "lysosomal pH regulation", "score": 0.75},
    {"source": "UBQLN2", "target": "VCP", "relation": "ubiquitin-proteasome coordination", "score": 0.83},
    {"source": "C9orf72", "target": "TBK1", "relation": "regulates autophagy in ALS", "score": 0.81},
    {"source": "TARDBP", "target": "FUS", "relation": "co-regulate RNA splicing", "score": 0.89},
    {"source": "ANXA11", "target": "C9orf72", "relation": "stress granule dynamics", "score": 0.78},
    {"source": "CHMP2B", "target": "VPS35", "relation": "endosomal sorting complex interaction", "score": 0.74},
    {"source": "TMEM106B", "target": "GRN", "relation": "modifies FTD risk", "score": 0.80},
    {"source": "PINK1", "target": "PRKN", "relation": "activates Parkin for mitophagy", "score": 0.92},
    {"source": "CHCHD10", "target": "PINK1", "relation": "mitochondrial cristae stability", "score": 0.76},
    {"source": "ATP13A2", "target": "PLA2G6", "relation": "lipid metabolism in mitochondria", "score": 0.72},
    {"source": "DJ-1", "target": "PINK1", "relation": "oxidative stress response", "score": 0.83},
    {"source": "NLGN1", "target": "NPTX2", "relation": "synaptic plasticity regulation", "score": 0.79},
    {"source": "BDNF", "target": "MAP3K5", "relation": "apoptosis suppression", "score": 0.77},
    {"source": "KCNH7", "target": "FYN", "relation": "ion channel phosphorylation", "score": 0.68},
    {"source": "NEFM", "target": "STX6", "relation": "axonal vesicle transport", "score": 0.72},
    {"source": "SP1", "target": "APP", "relation": "transcriptional regulation of APP", "score": 0.75},
    {"source": "RUNX2", "target": "KANSL1", "relation": "chromatin remodeling in neurodegeneration", "score": 0.69},
    {"source": "ARL17B", "target": "ASAP1", "relation": "membrane trafficking coordination", "score": 0.71},
    {"source": "LINC02210-CRHR1", "target": "ANXA11", "relation": "stress response modulation", "score": 0.66},

    # Gene-Disease Relationships (Corrected)
    {"source": "TMEM106B", "target": "Frontotemporal Dementia (FTD)", "relation": "lysosomal dysfunction", "score": 0.80},
    {"source": "UBQLN2", "target": "Amyotrophic Lateral Sclerosis (ALS)", "relation": "proteasome impairment", "score": 0.82},
    {"source": "ATP13A2", "target": "Parkinson's Disease (PD)", "relation": "mitochondrial ion imbalance", "score": 0.76},
    {"source": "PLA2G6", "target": "Parkinson's Disease (PD)", "relation": "lipid peroxidation", "score": 0.74},
    {"source": "DJ-1", "target": "Parkinson's Disease (PD)", "relation": "oxidative stress response", "score": 0.83},
    {"source": "RORB", "target": "Progressive Supranuclear Palsy (PSP)", "relation": "neuronal vulnerability", "score": 0.77},
    {"source": "NEFM", "target": "Amyotrophic Lateral Sclerosis (ALS)", "relation": "axonal transport defects", "score": 0.70},
    {"source": "KCNH7", "target": "Alzheimer's Disease", "relation": "ion channel dysregulation", "score": 0.68},
    {"source": "SP1", "target": "Alzheimer's Disease", "relation": "transcriptional dysregulation", "score": 0.75},
    {"source": "BDNF", "target": "Alzheimer's Disease", "relation": "neurotrophic support loss", "score": 0.88},
{"source": "VPS35", "target": "Parkinson's Disease (PD)", "relation": "endosomal trafficking defects", "score": 0.75, "source_type": "STRINGdb"},
{"source": "UCHL1", "target": "Parkinson's Disease (PD)", "relation": "ubiquitin homeostasis disruption", "score": 0.80, "source_type": "Paper"},
{"source": "KANSL1", "target": "Progressive Supranuclear Palsy (PSP)", "relation": "chromatin remodeling defects", "score": 0.68, "source_type": "Paper"},


    # Gene-Protein Relationships
    {"source": "LRRK2", "target": "Dardarin", "relation": "encodes", "score": 0.91},
    {"source": "UCHL1", "target": "Ubiquitin", "relation": "deubiquitinating enzyme", "score": 0.85},
    {"source": "VCP", "target": "Ubiquitin", "relation": "extracts substrates", "score": 0.88},
    {"source": "PRKN", "target": "Parkin Protein", "relation": "encodes", "score": 0.90},
    {"source": "GBA", "target": "Glucocerebrosidase", "relation": "encodes", "score": 0.89},
{"source": "RORB", "target": "RORB Protein", "relation": "encodes", "score": 0.94, "source_type": "STRINGdb"},
{"source": "NPTX2", "target": "Neuronal Pentraxin-2", "relation": "encodes", "score": 0.89, "source_type": "STRINGdb"},
{"source": "ASAP1", "target": "ArfGAP Protein", "relation": "encodes", "score": 0.85, "source_type": "STRINGdb"},


    # Gene-Gene Interactions
    {"source": "LRRK2", "target": "PINK1", "relation": "modulates mitophagy", "score": 0.83},
    {"source": "VCP", "target": "UBQLN2", "relation": "proteasome coordination", "score": 0.79},
    {"source": "SQSTM1", "target": "VCP", "relation": "aggresome formation", "score": 0.81},
    {"source": "FUS", "target": "TARDBP", "relation": "RNA splicing co-regulation", "score": 0.87},
    {"source": "CHCHD10", "target": "ATP13A2", "relation": "mitochondrial ion homeostasis", "score": 0.73},
    {"source": "PINK1", "target": "PRKN", "relation": "activates Parkin", "score": 0.92},
    {"source": "GBA", "target": "SNCA", "relation": "lysosomal clearance of aggregates", "score": 0.77},
    {"source": "TMEM106B", "target": "GRN", "relation": "progranulin trafficking", "score": 0.80},
    {"source": "OPTN", "target": "TBK1", "relation": "autophagy initiation", "score": 0.82},
    {"source": "ASAP1", "target": "ARL17B", "relation": "membrane trafficking", "score": 0.71},

    # Gene-Pathway Relationships
    {"source": "MAPT", "target": "Tauopathy", "relation": "drives pathology", "score": 0.95},
    {"source": "APP", "target": "Amyloid Processing", "relation": "Aβ production", "score": 0.96},
    {"source": "PINK1", "target": "Mitophagy", "relation": "mitochondrial quality control", "score": 0.91},
    {"source": "LRRK2", "target": "Neuroinflammation", "relation": "NF-κB activation", "score": 0.85},
    {"source": "RORB", "target": "WNT Signaling", "relation": "transcriptional regulation", "score": 0.77},
    {"source": "BDNF", "target": "Synaptic Vesicle Exocytosis", "relation": "enhances plasticity", "score": 0.88},

    # Pathway-Disease Relationships (Corrected)
    {"source": "Tauopathy", "target": "Alzheimer's Disease", "relation": "secondary pathology", "score": 0.90},
    {"source": "Autophagy", "target": "Amyotrophic Lateral Sclerosis (ALS)", "relation": "defective protein clearance", "score": 0.87},
    {"source": "Neuroinflammation", "target": "Alzheimer's Disease", "relation": "microglial activation", "score": 0.85},
    {"source": "Lysosomal Pathway", "target": "Parkinson's Disease (PD)", "relation": "α-synuclein degradation", "score": 0.89},
    {"source": "Oxidative Stress Response", "target": "Parkinson's Disease (PD)", "relation": "ROS accumulation", "score": 0.83},

{"source": "WNT Signaling", "target": "Tauopathy", "relation": "modulates tau phosphorylation", "score": 0.78, "source_type": "Paper"},
{"source": "Autophagy", "target": "Lysosomal Pathway", "relation": "lysosomal degradation dependency", "score": 0.91, "source_type": "Reactome"},
{"source": "Neuroinflammation", "target": "Oxidative Stress Response", "relation": "ROS amplification", "score": 0.83, "source_type": "STRINGdb"},
{"source": "Tau Protein", "target": "Tauopathy", "relation": "hyperphosphorylation cascade", "score": 0.95, "source_type": "Paper"},
{"source": "Amyloid-beta", "target": "Amyloid Processing", "relation": "plaque formation", "score": 0.97, "source_type": "Reactome"},
{"source": "Alpha-Synuclein", "target": "Lysosomal Pathway", "relation": "impaired degradation", "score": 0.89, "source_type": "STRINGdb"},

{"source": "LINC02210-CRHR1", "target": "BDNF", "relation": "stress-induced BDNF suppression", "score": 0.72, "source_type": "Paper"},
{"source": "KANSL1", "target": "SP1", "relation": "chromatin accessibility regulation", "score": 0.69, "source_type": "STRINGdb"},
{"source": "RUNX2", "target": "MAPT", "relation": "osteogenic transcription feedback", "score": 0.65, "source_type": "Paper"},
    # Protein-Disease Relationships (Corrected)
    {"source": "Glucocerebrosidase", "target": "Parkinson's Disease (PD)", "relation": "lysosomal dysfunction", "score": 0.89},
    {"source": "Ubiquitin", "target": "Amyotrophic Lateral Sclerosis (ALS)", "relation": "proteasome impairment", "score": 0.82},
    {"source": "RNA-binding proteins", "target": "Amyotrophic Lateral Sclerosis (ALS)", "relation": "stress granule pathology", "score": 0.85},
    {"source": "IL15", "target": "Neuroinflammation", "relation": "immune activation", "score": 0.79},
    {"source": "ITM2B", "target": "Frontotemporal Dementia (FTD)", "relation": "mutations cause dementia", "score": 0.85}
]
