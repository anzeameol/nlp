<center><font size = 5>nlp-pj2</font></center>
<p align='right'>刘卓瀚 21307130254</p>

# how to use
`main.py`文件会实现预训练模型的加载和微调，保存训练的模型，输出验证集的预测准确率  
`main.py`文件有三个参数：
- `--task`：任务名称，可选`mrpc`或`wnli`
- `--model`：模型名称，可选`bert-tiny`或`bert-base-uncased`
- `--from_cached`：是否从缓存加载数据集，指定此参数即为从缓存加载（则需要在`cfgs`文件夹中对应的文件给出数据集和模型的缓存地址）

模型的参数保存在`cfgs`文件夹中，分任务存放，比如`mrpc`任务+使用`bert-tiny`模型就应该在`cfgs/mrpc/bert-tiny.json`中给出参数，参数有如下：
```json
{
    "datapath": "./datasets/glue/mrpc",
    "modelpath": "./pretrained_models/bert-tiny",
    "learning_rate": 2e-5,
    "train_batch_size": 32,
    "eval_batch_size": 32,
    "num_train_epochs": 5,
    "weight_decay": 0.01,
    "max_length": 128
}
```
设定好参数，运行`main.py`即可

# my result
我的运行结果在`eval_results`文件夹中，参数为`cfgs`中的参数，具体见`模型准确率.docx`

# 代码结构
加载模型部分在`model.py`中，数据集处理部分在`dataset.py`中，训练、测试部分在`main.py`中，具体见代码注释