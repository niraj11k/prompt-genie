# app/prompt_creator.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()


TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")  # Keep your key secret

def create_prompt(task_description: str) -> str:
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
    if response.status_code != 200:
        return f"❌ API Error: {response.text}"
    return response.json()["choices"][0]["message"]["content"]
