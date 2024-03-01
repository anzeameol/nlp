from transformers import AutoTokenizer, AutoModelForSequenceClassification

"""
从远程仓库中下载模型
返回tokenizer和model
"""


def get_model(name, num_labels=2):
    if name == "bert-tiny":
        tokenizer = AutoTokenizer.from_pretrained(
            "prajjwal1/bert-tiny", num_labels=num_labels
        )
        model = AutoModelForSequenceClassification.from_pretrained(
            "prajjwal1/bert-tiny", num_labels=num_labels
        )
    elif name == "bert-base-uncased":
        tokenizer = AutoTokenizer.from_pretrained(
            "bert-base-uncased", num_labels=num_labels
        )
        model = AutoModelForSequenceClassification.from_pretrained(
            "bert-base-uncased", num_labels=num_labels
        )
    return tokenizer, model


"""
从本地加载模型
返回tokenizer和model
"""


def get_model_from_cached(path, num_labels=2):
    return AutoTokenizer.from_pretrained(
        path, num_labels=num_labels
    ), AutoModelForSequenceClassification.from_pretrained(path, num_labels=num_labels)
