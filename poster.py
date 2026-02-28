from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import textwrap

def get_text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

def create_poster(text):

    # get background
    url = "https://picsum.photos/800/1000"
    img = Image.open(BytesIO(requests.get(url).content)).convert("RGB")

    # DARK OVERLAY (this is what makes posters readable)
    overlay = Image.new('RGBA', img.size, (0,0,0,140))
    img = Image.alpha_composite(img.convert('RGBA'), overlay)

    draw = ImageDraw.Draw(img)

    # split caption & tagline
    lines = text.split("\n")
    caption = lines[0].replace("Caption:", "").strip()
    tagline = lines[1].replace("Tagline:", "").strip()

    # load fonts
    title_font = ImageFont.truetype("Montserrat-Bold.ttf", 70)
    tagline_font = ImageFont.truetype("Montserrat-Regular.ttf", 40)

    # wrap long text
    caption_lines = textwrap.wrap(caption, width=15)

    # center text
    y_text = 350
    for line in caption_lines:
        w, h = get_text_size(draw, line, title_font)
        draw.text(((800-w)/2, y_text), line, font=title_font, fill="white")
        y_text += h + 10

    # tagline
    w, h = get_text_size(draw, tagline, tagline_font)
    draw.text(((800-w)/2, y_text+40), tagline, font=tagline_font, fill="#FFD700")

    img = img.convert("RGB")
    img.save("poster.png")
    return "poster.png"