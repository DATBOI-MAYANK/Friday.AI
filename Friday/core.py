from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from .config import SYSTEM_PROMPT, OLLAMA_MODEL

def create_chain():
    llm = OllamaLLM(model=OLLAMA_MODEL)

    prompt = PromptTemplate.from_template(
        SYSTEM_PROMPT + "\n{input}"
    )

    chain = prompt | llm
    return chain

def run_chain(chain, prompt):
    return chain.invoke({"input": prompt})
