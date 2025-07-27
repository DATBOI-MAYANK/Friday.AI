from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from config import OLLAMA_MODEL

load_dotenv()

paper_input  = input("Enter the paper: ")
style_input = input("Enter the style: ")
length_input = input("Enter the length: ")

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following
specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets
where applicable.
2. Analogies:
- Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and
length.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)

prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

def main():
    model = ChatOllama(model=OLLAMA_MODEL)
    print("Ollama + LangSmith Paper Summarizer")
    response = model.invoke(prompt)
    print(response.content)

if __name__ == "__main__":
    main()