# Complex Network Analysis
Set of tools to analyze a complex network and extract some metrics with Networks.



## Install

```sh
pip3 install -r ./requirements.txt
```

## Use

Feel free to explore different files. There is a main function to demo the capabilities of each component. There is also a `main.py` which load the dataset and perform all kind of tasks on it!

```sh
cd src
python3 main.py
```


## Example Usage


```python
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
```

## Add my dataset
For each dataset, there should be a `load_dataset` function. This function is a flexible way of importing a dataset with any structure! At the end, just report G and the name of the dataset. Note that there is an optional assertion of a number of nodes and edges that can be utilized to make sure all lines of the files are read correctly.

```python
dataset_path = "../datasets/facebook.txt"
nodes_count = 4039
edges_count = 88234

def load_dataset():
    G = nx.Graph()
    with open(dataset_path, "r", encoding="UTF-8") as dataset_file:
        for line in dataset_file:
            a, b = line.split()
            G.add_edge(a, b)

    assert len(G.nodes) == nodes_count
    assert len(G.edges) == edges_count

    return "facebook", G
```
