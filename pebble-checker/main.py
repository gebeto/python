import requests
import json
from bs4 import BeautifulSoup
import hashlib


def cached_get(url):
    file_path_raw = hashlib.md5(url.encode()).hexdigest()
    file_path = f"{file_path_raw}.html"
    try:
        file_data = open(file_path, "r").read()
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file_data = requests.get(url).text
            file.write(file_data)
    return file_data


def parse_item(item):
    result = {
        "title": item.find("h3").getText(),
        "image": item.find("img", {"class": "s-item__image-img"})["src"],
        "url": item.find("a", {"class": "s-item__link"})["href"],
    }

    price = [i for i in item.find("span", {"class": "s-item__price"}).children]
    if len(price) > 1:
        result["price_range_raw"] = [price[0], price[-1]]
        result["price_range"] = result["price_range_raw"]
    else:
        result["price_raw"] = price[0]
        result["price"] = result["price_raw"]

    return result


def parse_items(html):
    soup = BeautifulSoup(response, "lxml")
    wrapper = soup.find("ul", {"class": "srp-results"})
    items = wrapper.find_all("li", {"class": "s-item"})

    jsons = []

    for item in items:
        jsons.append(parse_item(item))

    return jsons


# url = "https://www.ebay.com/sch/i.html?_nkw=pebble+round"
url = "https://www.ebay.com/sch/i.html?_nkw=pebble+round&rt=nc&LH_BIN=1"

response = cached_get(url)
items = parse_items(response)

json.dump(items, open("pebble.json", "w"), indent=4)
