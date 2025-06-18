import re
from .core import send_to_ollama
from .notify import parse_and_notify

def main():
    print("Ollama Chat (type 'exit' to quit)")
    chat_history = ""
    notify_pattern = re.compile(r"^\(notify,(\d+)\)\s*(.+)", re.DOTALL)
    while True:
        user_prompt = input("> ")
        if user_prompt.strip().lower() == "exit":
            break
        is_notify = bool(notify_pattern.match(user_prompt.strip()))
        model_response = send_to_ollama(user_prompt, chat_history, is_notify)
        notified = parse_and_notify(model_response)
        if not notified:
            print("Ollama:", model_response.strip())
            chat_history += f"\nUser: {user_prompt}\nAssistant: {model_response.strip()}"
