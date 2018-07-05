from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
from io import BytesIO


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


def draw_basic(text, width=1590, height=400, bg="#e74c3c", color="#000000"):
	im = Image.new("RGBA", (width,height), bg)
	# im = Image.new("RGBA",(width,height),'#'+str(datetime.now().time()).split('.')[1])
	draw = ImageDraw.Draw(im)
	fnt = ImageFont.truetype("fonts/overpass.otf", 24)
	w, h = draw.textsize(text, font=fnt)
	draw.text(((width-w)/2,(height-h)/2), text, fill=color, align="center", font=fnt)
	stream = BytesIO()
	im.save(stream, format='png')
	stream.seek(0)
	img = stream.read()
	open('image.png', 'wb').write(img)
	return img


def draw_apps_icons(icons):
	W, H = (1590, 400)
	icons_img = [Image.open(icon["icon"]) for icon in icons]
	icons_img = [add_corners(icon, 20) for icon in icons_img]

	im = Image.new("RGBA", (W, H), "#fff")
	draw = ImageDraw.Draw(im)
	fnt = ImageFont.truetype("fonts/overpass.otf", 22)

	# Draw icons
	curpos = len(icons_img) * (-2) + 3
	for i, icn in enumerate(icons_img):
		text = '\n'.join(icons[i]['title'].split(r'—')[0].split(' '))
		w, h = draw.textsize(text, font=fnt)
		im.paste(icn, (W / 2 - icn.size[0] / 2 * curpos, H / 2 - 80))
		draw.text((W / 2 - icons_img[0].size[0] / 2 * curpos + (icons_img[0].size[0] - w) / 2, H / 2 + 40), text, fill="black", font=fnt, align="center")
		curpos += 4

	stream = BytesIO()
	im.save(stream, format='png')
	stream.seek(0)
	img = stream.read()
	open('image.png', 'wb').write(img)
	return img
