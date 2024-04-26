from fastapi import FastAPI
import gradio as gr
from gradio import demo

# create fastapi instance
app = FastAPI()

@app.get('/')
async def root():
    return {"status": "app is running...",
            "code": "200 OK"}

# app path
app = gr.mount_gradio_app(app, demo, path='/predit')