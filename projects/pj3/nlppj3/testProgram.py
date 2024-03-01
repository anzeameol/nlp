import subprocess
import argparse
import os


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, choices=["qwen", "baichuan", "chatgpt"])
    opt = parser.parse_args()
    return opt


def testProgram(name):
    path = os.path.join("program", name)
    # os.chdir(path)
    passed = []
    for i in range(1, 8):
        ok = False
        for j in range(2):
            try:
                subprocess.check_output(
                    [
                        "python",
                        "-m",
                        "py_compile",
                        os.path.join(path, "q" + str(i), "turn" + str(j) + ".py"),
                    ]
                )
                ok = True
            except subprocess.CalledProcessError as e:
                pass
        if ok:
            passed.append(i)
    print("Passed: ", passed)


if __name__ == "__main__":
    opt = parseargs()
    testProgram(opt.model)
