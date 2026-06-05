from llm import llm
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}")
    ]
)

chain = prompt | llm

response = chain.invoke({
    "question": "Tell me a joke"
})

print(response)