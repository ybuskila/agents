from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)