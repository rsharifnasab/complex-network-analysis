#!/usr/bin/env python3

import networkx as nx

from citation import load_dataset as citation_load_dataset
from facebook import load_dataset as facebook_load_dataset
from twitter import load_dataset as twitter_load_dataset


from stats import GraphStats


class ModelGenerator():
    def __init__(self, name, G, seed: int = 1):
        self.seed = seed
        self.name = name
        self.G = G
        self.stats = GraphStats(name, self.G)

    def WS(self, n, k, p):
        return nx.watts_strogatz_graph(n, k, p, self.seed)

    def auto_ws(self, p):
        n = self.stats.node_count()
        k = int(float(self.stats.average_degree())) + 1
        model = self.WS(n, k, p)
        stats_model = GraphStats(f"{self.name}_WS", model)
        stats_model.print_summary()

        self.stats.print_summary()

    def BA(self, n, m):
        return nx.barabasi_albert_graph(n, m, self.seed)

    def auto_ba(self, km):
        n = self.stats.node_count()
        m = int(float(self.stats.average_degree()) * km)
        model = self.BA(n, m)
        stats_model = GraphStats(f"{self.name}_BA", model)
        stats_model.print_summary()

        self.stats.print_summary()


def main(dataset_loader):

    name, G = dataset_loader()
    ModelGenerator(name, G).auto_ba(km=0.52)


if __name__ == "__main__":
    main(facebook_load_dataset)
