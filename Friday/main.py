from .core import create_chain, run_chain
from .notify import parse_and_notify

def main():
    print("🤖 Friday.AI CLI — type 'exit' to quit")
    chain = create_chain()

    while True:
        user_prompt = input("> ")
        if user_prompt.strip().lower() == "exit":
            break

        response = run_chain(chain, user_prompt)
        notified = parse_and_notify(response)
        if not notified:
            print("📜 Output:", response)
