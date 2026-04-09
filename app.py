import streamlit as st
from ai_caption import generate_caption
from poster import create_poster

st.title("AI Poster Generator")

# Initialize session state for button disable state
if "generating" not in st.session_state:
    st.session_state.generating = False

topic = st.text_input("Enter Event / Topic")
tone = st.selectbox("Tone", ["Funny", "Professional", "Motivational", "Inspirational", "Humorous", "Elegant", "Bold", "Casual"])
style = st.selectbox("Style", ["Modern", "Minimal", "Vintage", "Neon", "Gradient", "Bordered", "Textured", "Monochrome"])
color_scheme = st.selectbox("Color Scheme", ["Warm", "Cool", "Monochrome", "Vibrant"])
font_size_title = st.slider("Title Font Size", 40, 100, 70)
font_size_tagline = st.slider("Tagline Font Size", 20, 60, 40)
text_color = st.color_picker("Title Text Color", "#FFFFFF")
tagline_color = st.color_picker("Tagline Text Color", "#FFD700")
background_effect = st.selectbox("Background Effect", ["Overlay", "Gradient", "Solid"])
extra = st.text_area("Additional Details")

# Show button or status message
if not st.session_state.generating:
    if st.button("Generate Poster"):
        st.session_state.generating = True
else:
    st.write("⏳ Generating poster, please wait...")

# Process poster generation
if st.session_state.generating:
    try:
        result = generate_caption(topic, tone, style, extra)

        st.subheader("AI Generated Content")
        st.write(result)

        poster = create_poster(result, style, color_scheme, font_size_title, font_size_tagline, text_color, tagline_color, background_effect)

        st.image(poster)

        with open(poster, "rb") as f:
            st.download_button("Download Poster", f, file_name="poster.png")
    except Exception as e:
        st.error(f"Error generating poster: {str(e)}")
    finally:
        st.session_state.generating = False
        st.rerun()