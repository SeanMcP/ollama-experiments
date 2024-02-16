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

def get_completion(prompt, model="llama2", temperature=0.0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    content = response.choices[0].message.content

    with open("completion-log.txt", "a") as f:
        f.write(f"{divider} {get_timestamp()} {divider}\n")
        f.write(f"\tmodel:      {model}\n")
        f.write(f"\ttemp:       {temperature}\n")
        f.write(f"\tprompt:     {prompt}\n")
        f.write(f"\tcompletion: {content}\n")
        f.write("\tnotes:       \n\n")

    return content

# ==============================================================================

article = """
Last Saturday, my five-year-old son asked me “Can we make our own video game?” He asks a lot of “Can we make out own…” questions, and the practical answer is usually no. But I felt uniquely qualified to help with this one, so I said “Sure!”

I turned to Kaboom.js, “a Javascript game programming library that helps you make games fast and fun.” I had some previous experience playing around with it in 2019 and knew that it would be a good option for what he wanted to build. Between the Kaboom playground and the Kaboom template on Replit, it was really easy to get started building the game.

That said, we quickly outgrew online dev environments and wanted to move local. I created a new directory, npm inited, and then installed kaboom. I imported the library from an .html file, opened it with Live Server, and we were off to the races. With this setup, we worked on the game Saturday and after work a few days this week.

The big takeaway from one week of development is that making games is hard! Even a Mario-clone is a complex application with a lot of conditions to manage and interactions to handle. Kaboom makes it easy, but it still takes a lot of time to build. I wish there were more examples in the Kaboom documentation; I’ve found a lot of detailed but outdated tutorials online and it’s hard to sift through what still works and what depends on old APIs.

But more importantly, building the game has meant a lot of quality time with my kids. Although the project started with my older son and me, we where quickly joined by my three-year-old son. Both boys really enjoy working on the game together, even though most of the time is spent with me reading the documentation and debugging issues. But doing it with them on my lap is a wonderful experience. I’m looking forward to building more with them as they grow.

If you are interested in making a game with your kids or nieces/nephews or students, here are some recommendations:

Involve your kids as much as possible in designing the game: Let their imagination run wild, and then figure out how to make it a reality later. If they’re stuck, guide them through the brainstorming process, and have paper and pencils handy for their designs.
Make small, incremental, and visible changes: It can be really tempting when you’re working in a new library to refactor old code when you learn new things. But for the sake of the kids, make sure to have something different about the game that they can see after each session. And give them lots of chances to play the game during and after coding.
Use Kaboom’s types when you’re developing: Kaboom adds a ton of global functions, and it is challenging to learn what they are and how to use them. Thankfully, the library includes type definitions that help with this. A bundler like Vite would probably bring in those types automatically, but if you (like me) want to keep things simple you can import the types with a JSDoc @typedef comment like this:
/** @typedef { import("./node_modules/kaboom/dist/global") } */
import kaboom from "./node_modules/kaboom/dist/kaboom.mjs";
When the game is in a more finished state, I’ll be happy to share it. But in the meantime, I’m just going to enjoy the opportunity to use my talents to spend extra time with my sons.
"""

prompt = f"""
You wrote an article and now you want to create a preview for it.

Your task it to perform the following actions:
1. Summarize the article in three bullet points
2. Extract the keywords from each bullet point. Limit each bullet point to 1-2 keywords.
3. Convert those keywords into a concise sentence that previews the article content. Limit one sentence.

You can use first person language when writing the final sentence, like "I", "me", "my", etc.

Article: '''{article}'''
"""
response = get_completion(prompt)
print(response)
