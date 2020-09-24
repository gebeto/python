from urllib import parse
import requests
from bs4 import BeautifulSoup
import json


BASE_URL = "https://rutracker.org/forum/"


def parse_url(url):
	content = requests.get(url).content
	soup = BeautifulSoup(content, "html.parser")
	return soup


def get_limit(topic):
	url = f"{BASE_URL}/viewforum.php?f={topic}"
	soup = parse_url(url)
	pages = soup.find_all("a", {"class": "pg"})
	href = pages[-2]["href"]
	href_split = parse.urlsplit(href)
	query = dict(parse.parse_qsl(href_split.query))
	limit = int(query["start"])
	return limit


def parse_page(topic, start):
	url = f"{BASE_URL}/viewforum.php?f={topic}&start={start}"
	soup = parse_url(url)
	items = soup.find_all("a", {"class": "torTopic bold tt-text"})
	items = [i.parent.parent.parent for i in items]
	result = []
	for item in items:
		title = item.find("a", {"class": "torTopic bold tt-text"})
		result.append({
			"title": title.text,
			"href": BASE_URL + title["href"],
		})
	return result