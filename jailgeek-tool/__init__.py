import sys
from Telegram import TelegramDocument
from PIL import Image, ImageFont
from PILSlavik import ImageDrawSlavik




file = TelegramDocument()

# im = Image.open("assets/post-bg.png")
im = Image.open("assets/test.png")
font = ImageFont.truetype("assets/SFUIDisplayBlack.otf", 120)


text = u"Мы поможем вам cохранить shsh."
draw = ImageDrawSlavik(im)
draw.text_box(
	(100, 130),
	(1400, 750),
	text,
	font=font,
	spacing=30,
	fill=(60, 77, 96,255),
	hfill=(56, 128, 211, 255),
)

# draw.multiline_text
# draw.textsize(text, font)

del draw



im.save(open("text.png", "wb"), "PNG")
# im.save(file, "PNG")

# file.send()