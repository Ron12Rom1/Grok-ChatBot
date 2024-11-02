import os, time, random
from dotenv import load_dotenv
from TextToSpeach.TTS import pyttsx3_TTS
from groq import Groq

Rules = """Do not use astrics or curly brackets or any other special characters.
Do not use capital letters.
Do not talk too much, Keep the conversation short and only talk alot when needed to.
Do not use profanity.
Do not use emojis.
"""
memory = """  """


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


with open("who-are-you.txt", "r") as f1:
    you_are = f1.read()



userIn = "Hi"

while True:

    with open ("memory.txt", "r+") as mem:
        memory = mem.read()

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": str(you_are) + "It is: " + str(time.time()) + 
             ".   this is what you remember from our previous conversation: " + str(memory)},

            {"role": "user", "content": userIn}
        ],
        model="llama3-70b-8192",
        stream=False,
        top_p=1,
        temperature=1.5,
        frequency_penalty=2.0,
        presence_penalty=2.0,
        seed = int(time.time() * random.random())

    )

    output = chat_completion.choices[0].message.content

    print("\n", output)
    # pyttsx3_TTS(output)

    userIn = input("\n: ")

    with open("memory.txt", "a") as mem:
        mem.write("\nUser: " + userIn  + "\nYou: " + output)
