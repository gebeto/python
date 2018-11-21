from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests
from urllib import parse

group_id = "80167947"
access_token = "ACCESS_TOKEN"


def upload_cover(image, access_token, group_id, width=1590, height=400):
	crop_url = 'https://api.vk.com/method/photos.getOwnerCoverPhotoUploadServer?' + parse.urlencode({
		"group_id": group_id,
		"crop_x": 0,
		"crop_y": 0,
		"crop_x2": width,
		"crop_y2": height,
		"access_token": access_token,
		"v": 5.67
	})
	upload_url = requests.get(crop_url).json()
	upload_url = upload_url["response"]["upload_url"]
	uploaded_data = requests.post(upload_url, files={"photo": image}).json()
	set_cover_url = 'https://api.vk.com/method/photos.saveOwnerCoverPhoto?' + parse.urlencode({
		"photo": uploaded_data["photo"],
		"hash": uploaded_data["hash"],
		"access_token": access_token,
		"v": "5.63"
	})
	upload_result = requests.get(set_cover_url).content
	return upload_result


def draw_basic(text, width=1590, height=400, bg="#e74c3c", color="#000000"):
	im = Image.new("RGBA", (width,height), bg)
	draw = ImageDraw.Draw(im)
	fnt = ImageFont.truetype("overpass.otf", 24)
	w, h = draw.textsize(text, font=fnt)
	draw.text(((width-w)/2,(height-h)/2), text, fill=color, align="center", font=fnt)
	stream = BytesIO()
	im.save(stream, format='png')
	stream.seek(0)
	img = stream.read()
	open('image.png', 'wb').write(img)
	return img


upload_cover(draw_basic("Hello world", bg="#e74c3c"), access_token, group_id)

