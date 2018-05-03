import requests
import sys
import os
from datetime import datetime
now = datetime.now().strftime("-%d%m%Y%H%M")
# print now


headers = {
	"Cookie": "_ga=GA1.2.1064349617.1525345428; _gid=GA1.2.1675776968.1525345428; _gat=1; PHPSESSID=595e3e5b7e69bca89cfac2628530cf53; language=en; language=en; settings|manage=YTo5OntzOjc6InBlclBhZ2UiO2k6MjU7czo1OiJzdGF0ZSI7YjoxO3M6NToicHJpY2UiO2I6MTtzOjc6InNlY3Rpb24iO2I6MTtzOjQ6ImRhdGUiO2I6MTtzOjQ6InNpemUiO2I6MTtzOjY6ImF1dGhvciI7YjoxO3M6MTA6ImRvd25sb2FkZWQiO2I6MTtzOjY6InJhdGluZyI7YjoxO30=",
}


def create_dir(path):
	try:
		os.mkdir("%s" % (dir_path))
	except:
		pass

def download_file(url, folder):
	filename = url.split("/")[-1]
	resp = requests.get(url, headers=headers)
	print filename
	open(os.path.join(folder, filename), "wb").write(resp.content)


args = sys.argv
# if len(args) < 2:
# 	exit()

urls_file_path = args[-1]
file_name = os.path.split(args[-1])[-1]
dir_path = os.path.join(os.path.dirname(urls_file_path), file_name.split(".")[0]) + now
urls_file = open(urls_file_path).read().split("\n")

create_dir(dir_path)
for url in urls_file:
	download_file(url, dir_path)
