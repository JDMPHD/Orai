import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # The '/v1' is required here for the library to find the chat path
    base_url="https://models.github.ai",
    api_key=os.environ.get("GITHUB_TOKEN"),
)

print("--- AI Chat Started (Type 'quit' to stop) ---")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["quit", "exit"]:
        break

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
            model="gpt-4o",
        )
        print(f"AI: {response.choices[0].message.content}\n")
    except Exception as e:
        print(f"Error: {e}\n")
