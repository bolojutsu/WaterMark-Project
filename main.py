from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/ravishingrick/Desktop', title="select an Image: ")


def add_watermark(image, wm_text):
    open_image = Image.open(image)
    image_width, image_height = open_image.size
    draw = ImageDraw.Draw(open_image)
    font_size = int(image_width / 6)
    font = ImageFont.truetype("Arial.ttf", font_size)
    x, y = int(image_width / 2), int(image_height / 2)
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_widthl=5, stroke_fill='#222', anchor="ms")
    open_image.show()


add_watermark(filename, 'YRRRRRR')
