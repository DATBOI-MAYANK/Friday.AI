from langchain_ollama import OllamaLLM 
from dotenv import load_dotenv

load_dotenv()

from Friday.config import OLLAMA_MODEL

def main():
    llm = OllamaLLM(model=OLLAMA_MODEL)
    print("Ollama + LangSmith Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = llm.invoke( user_input)
        print(response)

if __name__ == "__main__":
    main()