import os
import json
from urllib.parse import urlparse
import requests


base_path = "scripts"

scripts = json.load(open("scripts.json"))

try:
	os.mkdir(base_path)
except: pass

for script in scripts:
	url = urlparse(script)
	filename = os.path.split(url.path)[-1]
	filepath = os.path.join(base_path, filename)
	scheme = url.scheme or 'https'
	script_url = f"{scheme}://{url.netloc}{url.path}?{url.query}"
	try:
		response = requests.get(script_url, timeout=5)
		open(filepath, "wb").write(response.content)
	except Exception as e:
		print("ERROR >>>", e)
