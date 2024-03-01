import argparse
import json
import transformers
from dataset import get_dataset, get_dataset_from_cached
from model import get_model, get_model_from_cached
import os
import numpy as np
import torch

"""
锁定训练的随机种子
用于debug
"""


def lock_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.manual_seed(seed)


"""
解析命令行参数
"""


def parseargs():
    parser = argparse.ArgumentParser()
    # 任务选择：mrpc或wnli
    parser.add_argument(
        "--task", choices=["mrpc", "wnli"], default="none", help="which task to perform"
    )
    # 模型选择：bert-tiny或bert-base-uncased
    parser.add_argument(
        "--model",
        choices=["bert-tiny", "bert-base-uncased"],
        default="none",
        help="which model to use",
    )
    # 是否从本地加载数据集和模型
    parser.add_argument("--from_cached", action="store_true")
    opt = parser.parse_args()
    return opt


"""
训练和评估模型
"""


def solve(opt):
    # 读取配置文件
    path = os.path.join("cfgs", opt.task, opt.model + ".json")
    cfgs = None
    with open(path) as f:
        cfgs = json.load(f)

    # 加载数据集和模型
    if opt.from_cached:
        print("Loading from cached...")
        dataset = get_dataset_from_cached(cfgs["datapath"])
        tokenizer, model = get_model_from_cached(cfgs["modelpath"])
    else:
        print("Loading from scratch...")
        dataset = get_dataset(opt.task)
        tokenizer, model = get_model(opt.model)

    # 使用tokenizer对数据集进行编码
    encoded_dataset = dataset.map(
        lambda examples: tokenizer(
            examples["sentence1"],
            examples["sentence2"],
            truncation=True,
            max_length=cfgs["max_length"],
            padding="max_length",
        ),
        batched=True,
    )

    # 设定训练参数
    training_args = transformers.TrainingArguments(
        output_dir=os.path.join("./train_results", opt.task, opt.model),
        evaluation_strategy="epoch",
        learning_rate=cfgs["learning_rate"],
        per_device_train_batch_size=cfgs["train_batch_size"],
        per_device_eval_batch_size=cfgs["eval_batch_size"],
        num_train_epochs=cfgs["num_train_epochs"],
        weight_decay=cfgs["weight_decay"],
    )

    # 训练器
    trainer = transformers.Trainer(
        model=model,
        args=training_args,
        train_dataset=encoded_dataset["train"],
        eval_dataset=encoded_dataset["validation"],
    )

    # 训练前评估
    print("evaluate before finetuning...")
    trainer.model.eval()
    preds, label_ids, _ = trainer.predict(encoded_dataset["validation"])
    correct = 0
    for i in range(len(preds)):
        correct += preds[i].argmax() == label_ids[i]
    accuracy_before_finetune = correct / len(preds)
    print("accuracy before finetuning: %f" % (accuracy_before_finetune))

    # 训练
    print("Start training...")
    trainer.model.train()
    trainer.train()

    # 保存模型
    trainer.save_model(os.path.join("./trained_models", opt.task, opt.model))

    # 评估
    print("Start evaluating...")
    trainer.model.eval()
    preds, label_ids, _ = trainer.predict(encoded_dataset["validation"])
    correct = 0
    for i in range(len(preds)):
        correct += preds[i].argmax() == label_ids[i]
    accuracy = correct / len(preds)
    print("accuracy: %f" % (accuracy))

    # 保存评估结果
    with open(
        os.path.join("./eval_results", opt.task, opt.model, "eval_result.json"), "w"
    ) as f:
        json.dump(
            {
                "accuracy": accuracy,
                "accuracy before finetuning": accuracy_before_finetune,
            },
            f,
        )


if __name__ == "__main__":
    opt = parseargs()
    solve(opt)
