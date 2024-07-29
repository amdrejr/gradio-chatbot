import gradio as gr
from fastapi import FastAPI

from utils.gradio_ui import gradio_ui

fastAPI = FastAPI()

app = gr.mount_gradio_app(fastAPI, gradio_ui, path='/')
