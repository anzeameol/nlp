import json
import argparse


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, choices=["qwen", "baichuan", "chatgpt"])
    opt = parser.parse_args()
    return opt


def getScore(judge_name):
    judge_path = judge_name + "-judge.json"
    with open(judge_path, "r", encoding="utf-8") as f:
        judgment = json.load(f)
    print("|     | chatgpt rate | compile PASS or not |")
    print("| --- | ------------ | ------------------- |")
    total_score = 0
    question_num = 0
    for id in judgment.keys():
        judge = judgment[id]
        start_idx = judge.find("[[", len(judge) - 10)
        end_idx = judge.find("]]", start_idx)
        num = float(judge[start_idx + 2 : end_idx])
        total_score += num
        question_num += 1
        print("| %d   | %.1f            |                     |" % (int(id), num))
    print(
        "|  avg   |    %.2f          |                     |"
        % (total_score / question_num)
    )


if __name__ == "__main__":
    opt = parseargs()
    getScore(opt.model)
