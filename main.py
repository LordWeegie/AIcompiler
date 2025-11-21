import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('deepseekapi'), base_url="https://api.deepseek.com")
filepath = input("What is the file with your pseudocode? ")
codepath = input("What is the C file that you want to put the working code into? ")

with open(filepath, 'r') as file:
    content = file.read()


response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Hello, you need to read the pseudocode and then turn it into c code. please don't comment the code. OR put it in ``` ``` (this is required) as that makes it not work."},
        {"role": "user", "content": "This is the sudo code!" + content},   
    ],
    stream=False
)



with open(codepath, 'w') as codefile:
    codefile.write(response.choices[0].message.content) 
    
with open(codepath, 'r') as file:
    content = file.read()                  # read the actual file content

content = content.replace("```c", "")
content = content.replace("```\n", "")      # removes plain "```" + newline if present
content = content.replace("```c", "")       # fallback if no newline
content = content.replace("```", "")        # final cleanup of any leftover ```

content = content.strip()                   # removes any leading/trailing blank lines left behind


with open(codepath, 'w') as file:
    file.write(content)

print(response.choices[0].message.content)
