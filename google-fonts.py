import urllib.request
import sys
import re
import os

try:
	script, font, path = sys.argv
except:
	print("""How to use:

 > google-fonts.py "Font" /to/path
""")
	exit(0)

url = "https://fonts.googleapis.com/css?family={}".format(font)
# response = str(urllib.request.urlopen(url).read())
request = urllib.request.Request(url, headers={
	"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
})
response = urllib.request.urlopen(request).read().decode("utf-8")
fonts = re.findall(r"url\(([\w\W]+?)\)", response)


try: os.mkdir(path)
except: pass

for font in fonts:
	file_name = font.split("/")[-1]
	font_path = os.path.join(path, file_name)
	print(file_name)
	response = response.replace(font, file_name)
	open(font_path, "wb").write(urllib.request.urlopen(font).read())

open(os.path.join(path, "fonts.css"), "w").write(response)