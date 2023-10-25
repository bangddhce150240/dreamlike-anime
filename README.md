---
title: Dream Anime
emoji: 🏃
colorFrom: pink
colorTo: purple
sdk: gradio
sdk_version: 3.50.2
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

 Dreamlike Anime Generator

This is a Python program that generates dreamlike anime images based on a given prompt.

## Requirements

- Python 3.x
- gradio
- torch
- diffusers
- pytorch-cuda==12.1 (using anaconda)
## Installation

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run `pip install gradio torch diffusers` to install the required packages.

## Usage

1. Open the `app.py` file in your preferred Python editor.
2. Set the `model_id` and `device` variables to your desired values.
3. Run the `app.py` file.
4. Enter your prompt in the text box and click "Run".
5. The generated images will be displayed in the gallery.

## Additional Information

- The `negative_prompt` variable can be modified to change the negative prompts used by the generator.
- The `debug` parameter in the `demo.launch()` function can be set to `False` to disable debug mode.