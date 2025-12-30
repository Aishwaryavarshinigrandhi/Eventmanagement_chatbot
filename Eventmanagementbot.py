# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(api_key="YOUR_API_KEY")


    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Explain the event planning steps in simple terms."""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()


import os
import streamlit as st
from google import genai
from google.genai import types


client = genai.Client(api_key="YOUR_API_KEY")

SYSTEM_PROMPT = """
You are an Event Management Explainer Bot.

Explain event planning stages, venue setup, coordination roles, and event-day activities in simple and clear language.

Only give informational explanations.
Do not book venues, register users, or perform real actions.
If asked, politely say you can only explain.
"""

st.set_page_config(page_title="Event Management Chatbot", page_icon="🎉")

st.title("🎉 Event Management Explainer Bot")
st.write("Ask anything about event planning and operations")

user_input = st.text_input("Enter your question:")

if user_input:
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=SYSTEM_PROMPT + "\n\nUser Question: " + user_input
                )
            ],
        )
    ]

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=contents,
    )

    st.subheader("🤖 Bot Response")
    st.write(response.text)

