from http import HTTPStatus
import dashscope
import jsonlines
import json
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role

system_prompt = [
    "You are a math teacher. You are teaching a student how to solve a math problem. The student asks you a question.",
    "You are a veteran programmer.",
    "You are a helpful assistant.",
]


def call_with_messages(start_seq=1, end_seq=35):
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
                messages = [{"role": Role.SYSTEM, "content": system_prompt[2]}]
                for i in line["turns"]:
                    messages.append({"role": Role.USER, "content": i})
                    response = Generation.call(
                        model="baichuan2-13b-chat-v1",
                        messages=messages,
                        result_format="message",  # set the result to be "message" format.
                    )
                    if response.status_code == HTTPStatus.OK:
                        messages.append(
                            {
                                "role": response.output.choices[0]["message"]["role"],
                                "content": response.output.choices[0]["message"][
                                    "content"
                                ],
                            }
                        )
                        ans.append(response.output.choices[0]["message"]["content"])
            answer[line["question_id"]] = ans
    with open("baichuan-answer.json", "w", encoding="utf-8") as f:
        json.dump(answer, f, ensure_ascii=False)


def call_with_prompt():
    prompt = "介绍下故宫"
    rsp = dashscope.Generation.call(model="baichuan2-7b-chat-v1", prompt=prompt)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print(
            "Failed, status_code: %s, code: %s, message: %s"
            % (rsp.status_code, rsp.code, rsp.message)
        )


if __name__ == "__main__":
    type = "message"
    if type == "prompt":
        call_with_prompt()
    elif type == "message":
        call_with_messages(28, 35)
    else:
        print("call type not support")
