import ollama
from datetime import datetime

divider = "=" * 10

def get_timestamp():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def get_completion(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    response = ollama.chat(model, messages)
    content = response['message']['content']

    with open("logs/completion-log.txt", "a") as f:
        f.write(f"{divider} {get_timestamp()} {divider}\n")
        f.write(f"model:      {model}\n")
        f.write(f"prompt:     {prompt}\n")
        f.write(f"completion: {content}\n")
        f.write(f"notes:      \n\n")

    return content

# ==============================================================================

prompt = f"""
I am working on -2(4+x) =8. I got it to -8+2x=8, but I'm not sure what to do next.
"""

response = get_completion(prompt, model="wizard-math")

print(response)
