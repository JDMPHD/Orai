import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# The base_url must NOT have /v1 for the GitHub Models inference endpoint
client = OpenAI(
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
            # Use the full provider/model path
            model="openai/gpt-4o", 
        )
        print(f"AI: {response.choices[0].message.content}\n")
    except Exception as e:
        print(f"Error: {e}\n")
