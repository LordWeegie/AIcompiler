import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('deepseekapi'), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are an AI model that has the job to compile code. You need to read the input and guess what the output of said code would be. Please don't say anything other then the output of the code! During loops or when ever a new line would be made please make a new line. Thank you! The code needs to handle errors. If the user happens to write some code that makes it usally give an error I *need* you to do it! Please don't give errors. Handle for loops, while loops, do while loops."},
        {"role": "user", "content": ""},
    ],
    stream=False
)

print(response.choices[0].message.content)