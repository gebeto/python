import requests
from bs4 import BeautifulSoup
import urllib


def get_top_apps(count):
	all_apps = []
	url = "http://freeder.net/app-store/top/"
	resp = requests.get(url).content
	soup = BeautifulSoup(resp, "html.parser")
	apps_list = soup.find("div", {"class": "apps_list"})
	apps = apps_list.find_all("div", {"class": "slide"})
	for app in apps:
		all_apps.append({
				"title": app.find("div", {"class": "apps_info"}).h2.a.getText().encode("utf8"),
				"icon": urllib.urlopen(app.a.img["src"])
			})
	all_apps = all_apps[:count]
	all_apps.reverse()
	return all_apps

