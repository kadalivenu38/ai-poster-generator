from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import textwrap
import random

def get_text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

def create_gradient(size, color1, color2):
    """Create a vertical gradient image."""
    width, height = size
    gradient = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(gradient)
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        draw.line((0, y, width, y), fill=(r, g, b))
    return gradient

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_poster(text, style, color_scheme, font_size_title, font_size_tagline, text_color, tagline_color, background_effect):

    # get background
    url = "https://picsum.photos/800/1000"
    img = Image.open(BytesIO(requests.get(url).content)).convert("RGB")

    # Apply background effect
    if background_effect == "Gradient":
        if color_scheme == "Warm":
            grad = create_gradient(img.size, (255, 100, 100), (255, 200, 100))
        elif color_scheme == "Cool":
            grad = create_gradient(img.size, (100, 100, 255), (100, 200, 255))
        elif color_scheme == "Monochrome":
            grad = create_gradient(img.size, (50, 50, 50), (200, 200, 200))
        else:  # Vibrant
            grad = create_gradient(img.size, (255, 0, 150), (150, 255, 0))
        img = Image.blend(img, grad, 0.5)
    elif background_effect == "Solid":
        if color_scheme == "Warm":
            solid = Image.new('RGB', img.size, (255, 150, 100))
        elif color_scheme == "Cool":
            solid = Image.new('RGB', img.size, (100, 150, 255))
        elif color_scheme == "Monochrome":
            solid = Image.new('RGB', img.size, (100, 100, 100))
        else:  # Vibrant
            solid = Image.new('RGB', img.size, (255, 100, 200))
        img = Image.blend(img, solid, 0.7)
    else:  # Overlay
        if color_scheme == "Warm":
            overlay = Image.new('RGBA', img.size, (255, 100, 50, 120))
        elif color_scheme == "Cool":
            overlay = Image.new('RGBA', img.size, (50, 100, 255, 120))
        elif color_scheme == "Monochrome":
            overlay = Image.new('RGBA', img.size, (0, 0, 0, 140))
        else:  # Vibrant
            overlay = Image.new('RGBA', img.size, (255, 0, 255, 100))
        img = Image.alpha_composite(img.convert('RGBA'), overlay)

    # Apply style effects
    if style == "Bordered":
        draw_border = ImageDraw.Draw(img)
        draw_border.rectangle([20, 20, 780, 980], outline=text_color, width=10)
    elif style == "Textured":
        # Add some noise or pattern, simple random dots
        draw_texture = ImageDraw.Draw(img)
        for _ in range(500):
            x = random.randint(0, 800)
            y = random.randint(0, 1000)
            draw_texture.point((x, y), fill=(255, 255, 255, 50))
    # Other styles can be added similarly

    draw = ImageDraw.Draw(img)

    # split caption & tagline
    lines = text.split("\n")
    caption = lines[0].replace("Caption:", "").strip()
    tagline = lines[1].replace("Tagline:", "").strip()

    # load fonts with custom sizes
    title_font = ImageFont.truetype("Montserrat-Bold.ttf", font_size_title)
    tagline_font = ImageFont.truetype("Montserrat-Regular.ttf", font_size_tagline)

    # wrap long text
    caption_lines = textwrap.wrap(caption, width=15)

    # center text
    y_text = 350
    text_rgb = hex_to_rgb(text_color)
    for line in caption_lines:
        w, h = get_text_size(draw, line, title_font)
        draw.text(((800-w)/2, y_text), line, font=title_font, fill=text_rgb)
        y_text += h + 10

    # tagline
    tagline_rgb = hex_to_rgb(tagline_color)
    w, h = get_text_size(draw, tagline, tagline_font)
    draw.text(((800-w)/2, y_text+40), tagline, font=tagline_font, fill=tagline_rgb)

    img = img.convert("RGB")
    img.save("poster.png")
    return "poster.png"