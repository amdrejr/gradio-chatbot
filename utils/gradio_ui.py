from time import sleep

import gradio as gr
from fastapi import FastAPI

from utils.openai_connect import message_openai
from utils.style import style


def send_messages(msg, history):
    # response = message_openai(msg) # descomente aqui
    response = 'Edite o arquivo utils/gradio_ui.py para habilitar a conexão com a API da OpenAI' # comente aqui

    for i in range(len(response)):
        sleep(0.02) # Simula um delay de digitação
        yield response[: i + 1]


def create_gradio_app():
# biblioteca de themes -> https://huggingface.co/spaces/gradio/theme-gallery
    with gr.Blocks(theme='gradio/monochrome') as chatbot:
        chat = gr.Chatbot(placeholder='Pergunte-me sobre a doc do Spotify')
        
        gr.ChatInterface(
            fn=send_messages,
            chatbot=chat,
            # css=style, # Se preferir customizar na mão com CSS, editar o arquivo style.py
        )

    return chatbot

gradio_ui = create_gradio_app()