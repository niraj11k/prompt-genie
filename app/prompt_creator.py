# app/prompt_creator.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load API keys from .env
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")


#TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")  # Keep your key secret

def create_prompt(task_description: str) -> str:
    provider = provider.lower()
    import os
import requests
import openai
from dotenv import load_dotenv

load_dotenv()

# Load API keys from .env
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

def create_prompt(task_description: str, provider: str) -> str:
    provider = provider.lower()

    try:
        if provider == "openai":
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a helpful assistant."},
                    {"role": "user", "content": task_description}
                ]
            )
            return response['choices'][0]['message']['content']

        elif provider == "together":
            url = "https://api.together.xyz/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "mistralai/Mistral-7B-Instruct-v0.1",
                "messages": [
                    {"role": "system", "content": "You are an experienced prompt engineer from Howard University and You are an expert in generating prompts for AI models."},
            {"role": "user", "content": f"Review this user prompt yourself and Optimize this user prompt to make it extremly detailed to get an output as a professional level: {task_description}"}
                ]
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

        elif provider == "huggingface":
            url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            payload = {"inputs": task_description, "parameters": {"max_new_tokens": 300}}
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list) and "generated_text" in data[0]:
                return data[0]["generated_text"]
            return str(data)

        else:
            return f"❌ Unknown provider: {provider}"

    except Exception as e:
        return f"❌ Error: {str(e)}"

