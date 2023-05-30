import networkx as nx

txt_path = "../datasets/1-citation-network/citation-network/Cit-HepTh.txt"
nodes_count = 27770
edges_count = 352807


def load_dataset():
    G = nx.DiGraph()
    with open(txt_path, "r", encoding="UTF-8") as dataset_file:
        for line in dataset_file:
            if line.startswith("#"):
                continue
            a, b = line.split()
            G.add_edge(a, b)

    assert len(G.nodes) == nodes_count
    assert len(G.edges) == edges_count

    return "citation_network", G
