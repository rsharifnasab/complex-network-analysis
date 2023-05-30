#!/usr/bin/env python3

from collections import defaultdict
import networkx as nx

from facebook import load_dataset as facebook_load_dataset
from stats import GraphStats


class CommunityDetection():
    def __init__(self, name, G, seed: int = 1):
        self.seed = seed
        self.name = name
        self.G = G
        self.stats = GraphStats(name, self.G)

    def find_communities(self):
        return nx.community.louvain_communities(
            self.G,
            seed=self.seed,
            resolution=1,
        )

    def modularity(self, community_structure):
        return nx.community.modularity(
            self.G,
            communities=community_structure,
        )

    def save_comms(self, save_dir):
        with open(f"{save_dir}/{self.name}_comms.txt", "w", encoding="UTF-8") as f:
            for comm in self.find_communities():
                s = " ".join(comm)
                f.write(s)
                f.write("\n")

    def community_stats(self, verbose=False) -> str:
        res = ""
        res += f"{self.name} Graph\n"
        comms = self.find_communities()
        modularity = self.modularity(comms)
        res += f"modularity: {modularity}\n"
        res += f"community count: {len(comms)}\n"
        res += f"largest community size: {len(max(comms))}\n"

        if verbose:
            good_comms = [comm for comm in comms if len(comm) > 3]
            res += f"good comms: {len(good_comms)}\n"
            res += f"total nodes in good comms: {sum(good_comms)}\n"
            res += f"total nodes in all  comms: {self.stats.node_count()}\n"
            res += f"good_comm/all_comm: {sum(good_comms)/self.stats.node_count()}\n"
            res += f"avg comm size: {sum(good_comms)/len(good_comms)}\n"

        return res


def main(dataset_loader):
    name, G = dataset_loader()
    CD = CommunityDetection(name, G)
    print(CD.community_stats())

    CD.save_comms(".")


if __name__ == "__main__":
    main(facebook_load_dataset)
