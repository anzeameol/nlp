import jsonlines
import json
import openai
import os
import backoff

system_prompt = [
    "You are a math teacher. You are teaching a student how to solve a math problem. The student asks you a question.",
    "You are a veteran programmer.",
    "You are a helpful assistant.",
]


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(messages):
    return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)


def conversation_with_messages(start_seq=1, end_seq=35):
    answer = {}
    with open("pj3-test.jsonl", "r", encoding="utf-8") as f:
        data = jsonlines.Reader(f)
        for line in data:
            if int(line["question_id"]) < start_seq:
                continue
            if int(line["question_id"]) > end_seq:
                break

            print(line["question_id"])

            ans = []
            if line["category"] == "coding":
                turn = 3
            else:
                turn = 1
            for k in range(turn):
                messages = [{"role": "system", "content": system_prompt[2]}]
                for i in line["turns"]:
                    messages.append({"role": "user", "content": i})
                    response = completions_with_backoff(messages=messages)
                    content = response.get("choices")[0]["message"]["content"]
                    ans.append(content)
                    messages.append(
                        {
                            "role": "assistant",
                            "content": content,
                        }
                    )
            answer[line["question_id"]] = ans
    with open(
        "chatgpt-answer.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(answer, f, ensure_ascii=False)


if __name__ == "__main__":
    conversation_with_messages(28, 35)
