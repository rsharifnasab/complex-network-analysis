import networkx as nx

# ego-facebook dataset from snap
# https://snap.stanford.edu/data/ego-Facebook.html

dataset_path = "../datasets/facebook.txt"
nodes_count = 4039
edges_count = 88234
# hard coding nodes and edge
# just to make sure eveything is ok


def load_dataset():
    G = nx.Graph()
    with open(dataset_path, "r", encoding="UTF-8") as dataset_file:
        for line in dataset_file:
            a, b = line.split()
            G.add_edge(a, b)

    assert len(G.nodes) == nodes_count
    assert len(G.edges) == edges_count

    return "facebook", G


if __name__ == "__main__":
    load_dataset()
