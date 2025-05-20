""" Generation of text with gemini-2.0-flash
    https://cloud.google.com/vertex-ai/docs/generative-ai/learn/models
"""

from google.cloud import logging

from google import genai
from google.genai.types import GenerateContentConfig

import gradio as gr

PROJECT_ID = "<REPLACE_WITH_YOUR_PROJECT_ID>" # <---- CHANGE THIS
LOCATION = "europe-west4"
MODEL_GOOGLE = "gemini-2.0-flash"

# https://cloud.google.com/logging/docs/reference/libraries#use
logging_client = logging.Client()
log_name = "genai-vertex-text-gradio-log"
logger = logging_client.logger(log_name)

gemini_client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

def predict(prompt, max_output_tokens, temperature, top_p, top_k):

    response = gemini_client.models.generate_content(
    model=MODEL_GOOGLE, contents=prompt,
        config=GenerateContentConfig(
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            candidate_count=1,
            seed=5,
            max_output_tokens=max_output_tokens,
            stop_sequences=["STOP!"],
            presence_penalty=0.0,
            frequency_penalty=0.0,
        ),
    )
    logger.log_text(prompt)
    logger.log_text(response.text)
    return response.text

examples = [
    ["Best receipt for banana bread:"],
    ["You are an equities analyst researching information for your report with relevant facts and figures. Tell me about the mortgage market in US."],
    ["Brainstorm some ideas combining VR and fitness:"],
]

demo = gr.Interface(
    predict, 
    [ gr.Textbox(label="Enter prompt:", value="Best receipt for banana bread:"),
      gr.Slider(32, 1024, value=512, step = 32, label = "max_output_tokens"),
      gr.Slider(0, 1, value=0.2, step = 0.1, label = "temperature"),
      gr.Slider(0, 1, value=0.8, step = 0.1, label = "top_p"),
      gr.Slider(1, 40, value=38, step = 1, label = "top_k"),
    ],
    "text",
    examples=examples
    )

demo.launch(server_name="0.0.0.0", server_port=7860)