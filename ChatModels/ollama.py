
from langchain_ollama import ChatOllama

# Connect to locally running Ollama model
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=1.5
)

# Invoke the model
result = llm.invoke("Write a 2 line poem on India?")

print(result.content)
