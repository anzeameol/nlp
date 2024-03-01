import json
import argparse
import os


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, choices=["qwen", "baichuan", "chatgpt"])
    opt = parser.parse_args()
    return opt


def getScore(ans_name):
    ans_path = ans_name + "-answer.json"
    with open(ans_path, "r", encoding="utf-8") as f:
        answer = json.load(f)
    for id, ans in answer.items():
        if int(id) > 7:
            break
        os.makedirs(os.path.join("program", ans_name, "q" + str(id)), exist_ok=True)
        for turn, ans in enumerate(ans):
            program_start = ans.find("```python")
            program_end = ans.find("```", program_start + 1)
            program = ans[program_start + 9 : program_end]
            with open(
                os.path.join(
                    "program",
                    ans_name,
                    "q" + str(id),
                    "turn" + str(turn) + ".py",
                ),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(program)


if __name__ == "__main__":
    opt = parseargs()
    getScore(opt.model)
