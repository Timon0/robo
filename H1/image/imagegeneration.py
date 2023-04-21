from PIL import Image, ImageDraw, ImageFont


class ImageGeneration:
    def __init__(self):
        return

    def get_image_for_text(self, message, font_size=150):
        img = Image.new('RGB', (1920, 1080), color=(73, 109, 137))

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", size=font_size)
        width, height = img.size
        text_width, text_height = d.textsize(message, font=font)
        x_text = (width - text_width) / 2
        y_text = (height - text_height) / 2
        d.text((x_text, y_text), message, font=font, fill=(255, 255, 0))

        return img
