from AI.chat_bot.chat_chain import ChatModel
from AI.emo_bot.emo_chain import EmoRGBModel
from AI.models import RGBColor
from Arduino.serial_send import send_rgb

import chainlit as cl

chat_model = ChatModel(memory_size=6)
emo_model = EmoRGBModel()

@cl.on_chat_start
async def main():
    await cl.Message(
        content="Greetings, I am Emotion Mirror🪞",
        author="🧙‍♂️"
    ).send()


@cl.on_message
async def message(message: str):
    user_input = message.content

    response = chat_model.invoke(input=user_input)
    color = emo_model.invoke(input=response)
    print(color)
    send_rgb(red=color.r, green=color.g, blue=color.b)

    await cl.Message(
        content=response[-1].content,
        author="🧙"
    ).send()
