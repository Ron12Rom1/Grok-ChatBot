import os, time, random
from dotenv import load_dotenv
from TextToSpeach.TTS import pyttsx3_TTS

Rules = """Do not use astrics or curly brackets or any other special characters.
Do not use capital letters.
Do not talk too much, Keep the conversation short and only talk alot when needed to.
Do not use profanity.
Do not use emojis.
"""

you_are = """ An AI named Azura, You can ONLY check the wheter and tell me the time. """

memory = """  """


load_dotenv()

from groq import Groq


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

userIn = "Hi"

while True:
    chat_completion = client.chat.completions.create(
        messages=[
            # {
            #     "role": "system",
            #     "content": f"Folow this rule: DONT TALK TOO MUCH NOT MORE THEN 15 WORDS AVARAGE, You are :{you_are}, Your mamory: {memory}, Rules: {Rules}, other: time: {time.ctime()},",
            # },
            {
                "role": "user",
                "content": userIn,
            }
        ],
        model="mixtral-8x7b-32768",
        stream=False,
        # max_tokens=256
        seed = int(time.time() * random.random())

    )

    output = chat_completion.choices[0].message.content

    print("\n", output)
    # pyttsx3_TTS(output)

    userIn = input("\n: ")

    memory = memory + " You: " + output + " User: " + userIn