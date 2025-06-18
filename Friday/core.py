import requests
from .config import OLLAMA_URL, MODEL, SYSTEM_PROMPT

def send_to_ollama(prompt, chat_history, is_notify):
    if is_notify:
        full_prompt = SYSTEM_PROMPT + prompt
    else:
        full_prompt = chat_history + "\nUser: " + prompt + "\nAssistant:"
    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False,
        "options": {"num_ctx": 256, "num_predict": 50}
    }
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json().get("response", "")
