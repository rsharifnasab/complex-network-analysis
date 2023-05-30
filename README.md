# Complex Network analysis
Set of tools to analysis a complex network and extract some metrics



## Install

```bash
pip3 install -r ./requirements.txt
```

## Use

Feel free to explore different files. there is a main function to demo capabilities of each file. There is also a `main.py` which load dataset and perform all kind of tasks on it!

```
cd src
python3 main.py
```

## Add my dataset
for each dataset there should be a `load_dataset` function. This function is a flexible way of importing a dataset with any structure! At the end just report G and name of the dataset. Note that there is an optional assertion of number of nodes and edges that can be utilized to make sure all lines of the files is read correctly.
