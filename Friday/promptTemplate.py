from langchain_core.prompts import  load_prompt
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from config import OLLAMA_MODEL

load_dotenv()

paper_input  = input("Enter the paper: ")
style_input = input("Enter the style: ")
length_input = input("Enter the length: ")

template = load_prompt("template.json")

# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })

def main():
    model = ChatOllama(model=OLLAMA_MODEL)
    print("Ollama + LangSmith Paper Summarizer")
    chain  = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    print(result.content)

if __name__ == "__main__":
    main()
