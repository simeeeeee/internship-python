import os
import openai 
import secrets

openai.api_key = secrets.api_key

while True:
    content = input("User : ")
    message = [
        {"role":"user", "content":content}
    ]

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        message = message
    )

    chatgpt_response = response.choices[0].message.content    
    print(f"ChatGPT : {chatgpt_response}")