from langchain_openai import ChatOpenAI

from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.exceptions import OutputParserException
from langchain.prompts import PromptTemplate
from langchain_core.messages.chat import ChatMessage
from AI.utils import build_conversation
from AI.models import RGBColor
from pathlib import Path

script_dir = Path(__file__).parent

class EmoRGBModel():
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name=model_name
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

        parser = PydanticOutputParser(pydantic_object=RGBColor)
        prompt = PromptTemplate(
            input_variables=["input", "error"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
            template=Path(script_dir / "emo.prompt").read_text(),
        )
        self.chain = prompt | self.llm | parser

    def invoke(
            self, 
            input: list[ChatMessage], 
            retry: int = 3,
            errors: list[str] = [],
        ) -> RGBColor:

        error = ""
        if errors:
            error_message = "\n".join(errors)
            error = f"\n\nPreviously encountered errors: {error_message}\nMake sure not to make them now!\n\n"

        try:
            return self.chain.invoke({"conversation": build_conversation(input), "error": error})
        except OutputParserException as e:
            if retry == 0:
                raise Exception(f"Cannot parse object: {e}")

            errors.append(e)
            self.invoke(input=input, retry=retry-1, errors=errors)