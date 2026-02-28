import streamlit as st
from ai_caption import generate_caption
from poster import create_poster

st.title("AI Poster Generator")

topic = st.text_input("Enter Event / Topic")
tone = st.selectbox("Tone", ["Funny", "Professional", "Motivational"])
style = st.selectbox("Style", ["Modern", "Minimal", "Vintage", "Neon"])
extra = st.text_area("Additional Details")

if st.button("Generate Poster"):

    result = generate_caption(topic, tone, style, extra)

    st.subheader("AI Generated Content")
    st.write(result)

    poster = create_poster(result)

    st.image(poster)

    with open(poster, "rb") as f:
        st.download_button("Download Poster", f, file_name="poster.png")