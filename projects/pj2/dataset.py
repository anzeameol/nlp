import datasets

"""
从远程仓库中下载数据集
返回数据集
"""


def get_dataset(name):
    if name == "mrpc":
        return datasets.load_dataset(path="glue", name="mrpc")
    elif name == "wnli":
        return datasets.load_dataset(path="glue", name="wnli")
    else:
        print("Dataset not found.")
        exit(1)


"""
从本地加载数据集
"""


def get_dataset_from_cached(path):
    return datasets.load_from_disk(path)
