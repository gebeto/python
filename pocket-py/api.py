import requests

from auth import get_auth_data
from req import consumer_key

auth = get_auth_data()

def add_bookmark(url, title):
	res = requests.post("https://getpocket.com/v3/add", json={
		"url": url,
		"title": title,
		"consumer_key": consumer_key,
		"access_token": auth["access_token"],
	})

	if res.status_code == 200:
		print("Success!")
	else:
		print("Error!")

	# print(res.content)
