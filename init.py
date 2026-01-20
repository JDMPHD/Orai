import os
from openai import OpenAI
from dotenv import load_dotenv

# This looks for the .env file and loads GITHUB_TOKEN into your environment
load_dotenv()

client = OpenAI(
    base_url="https://models.github.ai", /v1
    api_key=os.environ.get("GITHUB_TOKEN"), 
)

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
    model="openai/gpt-4o", 
)

print(response.choices[0].message.content)
