import time

def generate_and_time(model, prompt, max_tokens=50, prompt_template=None):
    full_prompt = prompt_template.format(prompt=prompt) if prompt_template else prompt

    start = time.time()
    result = model(
        prompt=full_prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        stop=["</s>", "###"],
        echo=False
    )
    total_time = time.time() - start

    output_text = result["choices"][0]["text"]
    token_count = len(output_text.split()) or 1
    avg_token_time = total_time / token_count
    tpm = 60 / avg_token_time

    return {
        "output": output_text,
        "gen_time": total_time,
        "avg_token": avg_token_time,
        "tokens_per_min": tpm
    }
