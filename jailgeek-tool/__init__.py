import sys
from PIL import Image, ImageDraw, ImageFont

try:
    # python 2
    from StringIO import StringIO
except ImportError:
    # python 3
    from io import StringIO


im = Image.open("assets/post-bg.png")
font = ImageFont.truetype("assets/Archive.otf", 40)


draw = ImageDraw.Draw(im)
draw.text((10, 25), "Hello world!!", font=font)


del draw

# write to stdout
output = StringIO()
im.save(open("text.png", "wb"), "PNG")
im.save(output, "PNG")
contents = output.getvalue()
output.close()
print contents