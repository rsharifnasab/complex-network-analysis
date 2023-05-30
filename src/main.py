#!/usr/bin/env python3

from facebook import load_dataset as facebook_load_dataset
from stats import GraphStats
from comm import CommunityDetection
from modeling import ModelGenerator


def main(dataset_loader):
    name, G = dataset_loader()

    GS = GraphStats(name, G, slow=False, force_undirect=True)
    GS.print_summary()

    CD = CommunityDetection(name, G)
    print(CD.community_stats())
    CD.save_comms(".")

    MG = ModelGenerator(name, G)
    MG.auto_ws(p=0.5)


if __name__ == "__main__":
    main(facebook_load_dataset)
