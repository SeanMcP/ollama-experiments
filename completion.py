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
Given the following Common Core standard and student grade level, create a \
short reading passage at the appropriate reading level and questions for every \
part of the standard to assess student mastery of the standard.

Grade Level: 3
Standard: CCSS.ELA-LITERACY.CCRA.R.1 Read closely to determine what the text says explicitly and to make logical inferences from it; cite specific textual evidence when writing or speaking to support conclusions drawn from the text.
"""

response = get_completion(prompt, model="gemma")

print(response)
