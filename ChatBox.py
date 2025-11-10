# ChatBox.py
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch API key from .env (make sure to add your key there)
key = os.getenv("GKEY")

# Initialize Groq/OpenAI client
client = OpenAI(
    api_key=key,
    base_url="https://api.groq.com/openai/v1",
)

# Store message history
messages = [
    {'role': 'system', 'content': "You are Talkora, a personal assistant."}
]

# Generate chatbot responses
def get_response(user_input):
    try:
        messages.append({'role': 'user', 'content': user_input})
        chat = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({'role': 'assistant', 'content': reply})
        return reply
    except Exception as e:
        return str(e)
