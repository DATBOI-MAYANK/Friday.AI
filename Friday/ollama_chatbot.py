from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from config import OLLAMA_MODEL

load_dotenv()

chat_history = []

def main():
    model = ChatOllama(model=OLLAMA_MODEL)
    print("Ollama + LangSmith Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        chat_history.append(user_input)
        if user_input.lower() == "exit":
            break
        response = model.invoke( chat_history)
        chat_history.append(response.content)
        print("AI:", response.content)

print("Chat History:", chat_history)


if __name__ == "__main__":
    main()
