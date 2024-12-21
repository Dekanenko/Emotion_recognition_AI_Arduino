from langchain_openai import ChatOpenAI

from langchain_core.output_parsers.string import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.messages.chat import ChatMessage
from AI.utils import build_conversation

from pathlib import Path

script_dir = Path(__file__).parent

class ChatModel():
    def __init__(self, model_name: str = "gpt-4o-mini", memory_size: int = 4):
        self.model_name=model_name
        self.memory_size=memory_size
        self.conversation = []

        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
        prompt = PromptTemplate(input_variables=["context", "input"],  template=Path(script_dir / "chat.prompt").read_text())

        self.chain = prompt | self.llm | StrOutputParser()

    def invoke(self, input: str) -> list[ChatMessage]:
        response = self.chain.invoke({"input": input, "conversation":build_conversation(self.conversation)})
        self.conversation.append(ChatMessage(role="User", content=input))
        self.conversation.append(ChatMessage(role="Agent", content=response))

        if len(self.conversation) > self.memory_size:
            self.conversation = self.conversation[len(self.conversation)-self.memory_size:]

        return self.conversation