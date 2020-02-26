import requests
import json
from bs4 import BeautifulSoup
import re

url = "https://yarofon.com"

response = requests.get(url)
content = response.content
text = content.decode("utf-8")
soup = BeautifulSoup(content, "html.parser")

# print(dir(soup))
# items = soup.find_all(["img", "script", "style"])
items = soup.find_all(["style"])
# print(items)

for item in items:
	src = item.attrs.get("src")
	href = item.attrs.get("href")
	if src:
		print(src)
	if href:
		print(href)
