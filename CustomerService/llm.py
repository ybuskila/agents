from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()

llm = chatopenai = OpenAI(model="gpt-4o-mini", temperature=0.7)