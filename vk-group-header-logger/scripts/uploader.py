import requests
from urllib import urlencode


def upload_cover(image, access_token, group_id, width=1590, height=400, debug=False):
	crop_url = 'https://api.vk.com/method/photos.getOwnerCoverPhotoUploadServer?' + urlencode({
		"group_id": group_id,
		"crop_x": 0,
		"crop_y": 0,
		"crop_x2": width,
		"crop_y2": height,
		"access_token": access_token,
		"v": 5.63
	})
	upload_url = requests.get(crop_url).json()["response"]["upload_url"]
	if debug:
		print upload_url
		print ""
	uploaded_data = requests.post(upload_url, files={"photo": image}).json()
	if debug:
		print uploaded_data
		print ""
	set_cover_url = 'https://api.vk.com/method/photos.saveOwnerCoverPhoto?' + urlencode({
		"photo": uploaded_data["photo"],
		"hash": uploaded_data["hash"],
		"access_token": access_token,
		"v": "5.63"
	})
	upload_result = requests.get(set_cover_url).content
	if debug:
		print upload_result
		print ""


