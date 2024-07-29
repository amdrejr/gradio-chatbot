from time import sleep

import gradio as gr

from utils.openai_connect import message_openai
from utils.style import style


def send_messages(msg, history):
    response = message_openai(msg)

    for i in range(len(response)):
        sleep(0.02) # Simula um delay de digitação
        yield response[: i + 1]


# biblioteca de themes -> https://huggingface.co/spaces/gradio/theme-gallery
with gr.Blocks(theme='gradio/monochrome') as chatbot:
    chat = gr.Chatbot(placeholder='Pergunte-me sobre a doc do Spotify')
    
    gr.ChatInterface(
        fn=send_messages,
        chatbot=chat,
        # css=style, # Se preferir customizar na mão com CSS, editar o arquivo style.py
    )


chatbot.launch()