from requests import get, post
from bs4 import BeautifulSoup
import hashlib
import json
import time
import os
import re


abs_path = os.path.abspath(__file__)
dir_path, filename = os.path.split(abs_path)

def find_price(price):
    p = re.findall(r"[\d.]+", price)
    if p:
        return float(p[0])
    return price


def cached_get(url):
    file_path_raw = hashlib.md5(url.encode()).hexdigest()
    file_path = f"{file_path_raw}.html"
    try:
        file_data = open(file_path, "r").read()
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file_data = get(url).text
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
        result["price"] = f"{price[0]} - {price[-1]}"
    else:
        result["price"] = f"{price[0]}"

    # if len(price) > 1:
    #     price_start = price[0]
    #     price_end = price[-1]
    #     result["price_range_raw"] = [price_start, price_end]
    #     result["price_range"] = [find_price(price_start), find_price(price_end)]
    # else:
    #     result["price_raw"] = price[0]
    #     result["price"] = find_price(price[0])

    return result


def parse_items(html):
    soup = BeautifulSoup(response, "lxml")
    wrapper = soup.find("ul", {"class": "srp-results"})
    # items = wrapper.find_all("li", {"class": "s-item"})
    items = [i for i in wrapper.children][1:]

    jsons = []

    for item in items:
        if item.name == "div":
            if "srp-river-answer" in item["class"]:
                break
            else:
                continue
        jsons.append(parse_item(item))

    return jsons


def get_item_name(item):
    data = str(item)
    filename = hashlib.md5(data.encode()).hexdigest()
    return f"{dir_path}/data/{filename}.json"


def save_all_items(items, on_new_found):
    for item in items:
        filename = get_item_name(item)
        if not os.path.exists(filename):
            on_new_found(item)
        json.dump(item, open(filename, "w"), indent=4)


def upload_to_telegram(item):
    token = open("token", "r").read().strip()
    bot_url = f"https://api.telegram.org/bot{token}/sendPhoto"

    resp = post(bot_url, json={
        "chat_id": "@pebble_search",
        "photo": item["image"],
        "caption": f"""{item["title"]}

*Link*: [ebay.com]({item["url"]})
*Price*: *{item["price"]}*
        """,
        "parse_mode": "markdown"
    })

    print(resp, resp.content)
    time.sleep(3)


# url = "https://www.ebay.com/sch/i.html?_nkw=pebble+round"
url = "https://www.ebay.com/sch/i.html?_nkw=pebble+round&rt=nc&LH_BIN=1"

response = get(url).content
# response = cached_get(url)
items = parse_items(response)
save_all_items(items, upload_to_telegram)
