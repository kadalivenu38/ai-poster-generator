import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY is None:
    API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

def generate_caption(topic, tone, style, extra):

    prompt = f"""
    Create a POSTER TEXT only.

    Topic: {topic}
    Tone: {tone}
    Style: {style}
    Extra: {extra}

    Rules:
    - Caption must be MAX 8 words
    - Tagline must be MAX 6 words
    - No paragraphs
    - No explanations

    Output strictly:

    Caption: <headline>
    Tagline: <tagline>
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text