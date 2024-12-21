from langchain_core.messages.chat import ChatMessage

def build_conversation(conversation: list[ChatMessage]) -> str:
    output: str = ""
    for message in conversation:
        output += f"{message.role}: {message.content}\n"
    
    return output