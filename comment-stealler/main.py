import json
import requests
from bs4 import BeautifulSoup


base_url = "https://accountgames.ru/responses?type=good&page={page}"


def parse(url):
	content = requests.get(url).content
	soup = BeautifulSoup(content, "html.parser")
	reviews = soup.find_all("div", {"id": "gameReview"})
	items = [{
		"date": r.find("div", {"class": "gameReviewDate"}).text.strip(" "),
		"text": r.find("div", {"class": "gameReviewText"}).text.strip(" "),
	} for r in reviews]
	return items



items = []
# for i in range(1, 650):
for i in range(1, 650):
	print("Page =", i)
	items += parse(
		base_url.format(
			page=i
		)
	)
	json.dump(items, open("items", "w"), indent=4, ensure_ascii=False)

# print(items)