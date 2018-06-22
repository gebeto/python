import sys
from Telegram import TelegramDocument
from PIL import Image, ImageDraw, ImageFont

file = TelegramDocument()

im = Image.open("assets/post-bg.png")
font = ImageFont.truetype("assets/Archive.otf", 40)



draw = ImageDraw.Draw(im)
draw.text((10, 25), "Hello asd world!!", font=font)
del draw



im.save(open("text.png", "wb"), "PNG")
im.save(file, "PNG")

file.send()