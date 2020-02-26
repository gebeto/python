import requests
import json
from bs4 import BeautifulSoup
import re

url = "https://yarofon.com"

response = requests.get(url)
content = response.content

text = content.decode("utf-8")

soup = BeautifulSoup(content, "html.parser")
scripts = soup.find_all("script")

res = []
for script in scripts:
	src = script.attrs.get('src')
	if src:
		res.append(src)
		print(src)

print(res)
json.dump(res, open("scripts.json", "w"), indent=4)
# print(scripts)
