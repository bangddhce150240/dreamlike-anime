import gradio as gr
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import logging

model_id = "dreamlike-art/dreamlike-anime-1.0"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)
negative_prompt = 'simple background, duplicate, retro style, low quality, lowest quality, 1980s, 1990s, 2000s, 2005 2006 2007 2008 2009 2010 2011 2012 2013, bad anatomy, bad proportions, extra digits, lowres, username, artist name, error, duplicate, watermark, signature, text, extra digit, fewer digits, worst quality, jpeg artifacts, blurry'

block = gr.Blocks(css=".container { max-width: 800px; margin: auto; }")

def infer(prompt):
    with autocast("cuda"):
        images = pipe(prompt, negative_prompt=negative_prompt)["images"]
    return images


with block as demo:
    gr.Markdown("<h1><center>Dreamlike anime</center></h1>")
    with gr.Group():
        with gr.Box():
            with gr.Row().style(mobile_collapse=False, equal_height=True):

                text = gr.Textbox(
                    label="Enter your prompt", show_label=False, max_lines=1
                ).style(
                    border=(True, False, True, True),
                    rounded=(True, False, False, True),
                    container=False,
                )
                btn = gr.Button("Run").style(
                    margin=False,
                    rounded=(False, True, True, False),
                )

        gallery = gr.Gallery(label="Generated images", show_label=False).style(
            grid=[2], height="auto"
        )
        text.submit(infer, inputs=[text], outputs=gallery)
        btn.click(infer, inputs=[text], outputs=gallery)

demo.launch(debug=True)