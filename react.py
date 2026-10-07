from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num:float) -> float:
    """
    parameter: The number to triple
    returns: The triple of the input number
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatOllama(model="qwen3-coder:30b", temperature=0).bind_tools(tools)
# llm = ChatOllama(model="qwen3.8:27b", temperature=0).bind_tools(tools)