from openai import OpenAI
from datetime import datetime

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

divider = "=" * 10

def get_timestamp():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def get_completion(prompt, model, temperature=0.0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    content = response.choices[0].message.content

    with open("logs/openai-completion-log.txt", "a") as f:
        f.write(f"{divider} {get_timestamp()} {divider}\n")
        f.write(f"model:      {model}\n")
        f.write(f"temp:       {temperature}\n")
        f.write(f"prompt:     {prompt}\n")
        f.write(f"completion: {content}\n")
        f.write(f"notes:      \n\n")

    return content

# ==============================================================================

prompt = f"""
I am working on -2(4+x) =8. I got it to -8+2x=8, but I'm not sure what to do next.
"""

response = get_completion(prompt, model="wizard-math")

evaluation_prompt = f"""
Evaluate if the provided completion includes the correct answer of x=-8.

If it is correct, please respond with "correct". If it is incorrect, please respond with "incorrect".

Prompt: {response}
"""

eval = get_completion(evaluation_prompt, model="wizard-math")

print(eval)
