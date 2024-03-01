import jsonlines
import json
import openai
import argparse
import backoff


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, choices=["qwen", "baichuan", "chatgpt"])
    opt = parser.parse_args()
    return opt


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(messages):
    return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)


def judge(ans_name, start_seq=1, end_seq=35):
    ans_path = ans_name + "-answer.json"
    questions = {}
    categories = {}
    references = {}
    with open("pj3-test.jsonl", "r", encoding="utf-8") as f:
        data = jsonlines.Reader(f)
        for line in data:
            questions[line["question_id"]] = line["turns"]
            categories[line["question_id"]] = line["category"]
            if line["category"] == "math":
                references[line["question_id"]] = line["reference"]
    answers = {}
    with open(ans_path, "r", encoding="utf-8") as f:
        answers = json.load(f)
    judge_prompt = {}
    with open("judge-prompts.jsonl", "r", encoding="utf-8") as f:
        data = jsonlines.Reader(f)
        for line in data:
            judge_prompt[line["name"]] = {
                "system_prompt": line["system_prompt"],
                "prompt_template": line["prompt_template"],
            }
    judgment = {}
    for question_id in questions.keys():
        if question_id < start_seq:
            continue
        if question_id > end_seq:
            break
        print(question_id)
        question = questions[question_id]
        category = categories[question_id]
        if category == "coding":
            answer = answers[str(question_id)][0:1]
            system_prompt = judge_prompt["base-v1"]["system_prompt"]
            prompt_template = judge_prompt["base-v1"]["prompt_template"]
            prompt = prompt_template.format(question=question[0], answer=answer[0])
        elif category == "roleplay":
            answer = answers[str(question_id)]
            system_prompt = judge_prompt["multi-turn"]["system_prompt"]
            # prompt_template = judge_prompt["multi-turn"]["prompt_template"]
            template_start = "<|The Start of Assistant A's Conversation with User|>\n\n"
            template_QA = "### User:\n{question}\n\n### Assistant A:\n{answer}\n\n"
            template_end = "<|The End of Assistant A's Conversation with User|>"
            prompt = template_start
            for i in range(len(question)):
                prompt += template_QA.format(question=question[i], answer=answer[i])
            prompt += template_end
        elif category == "writing":
            answer = answers[str(question_id)]
            system_prompt = judge_prompt["base-v1"]["system_prompt"]
            prompt_template = judge_prompt["base-v1"]["prompt_template"]
            prompt = prompt_template.format(question=question[0], answer=answer[0])
        else:
            answer = answers[str(question_id)]
            system_prompt = judge_prompt["math-v1"]["system_prompt"]
            prompt_template = judge_prompt["math-v1"]["prompt_template"]
            reference = references[question_id]
            prompt = prompt_template.format(
                question=question[0], answer=answer[0], ref_answer_1=reference[0]
            )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
        response = completions_with_backoff(messages)
        content = response.get("choices")[0]["message"]["content"]
        judgment[question_id] = content
    with open(ans_name + "-judge.json", "w", encoding="utf-8") as f:
        json.dump(judgment, f, ensure_ascii=False)


if __name__ == "__main__":
    opt = parseargs()
    judge(opt.model)
