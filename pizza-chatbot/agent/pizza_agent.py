from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from agent.prompts import SYSTEM_PROMPT

def get_llm():
    return ChatOllama(model="gemma3:1b", temperature=0.3)

def chat_with_agent(user_input: str, chat_history: list) -> str:
    """
    chat_history: list of {"role": "user"/"assistant", "content": "..."}
    Returns agent response string.
    """
    llm = get_llm()

    messages = [SystemMessage(content=SYSTEM_PROMPT)]

    for msg in chat_history:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(AIMessage(content=msg["content"]))

    messages.append(HumanMessage(content=user_input))

    response = llm.invoke(messages)
    return response.content
