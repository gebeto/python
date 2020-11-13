import requests
# # from bs4 import BeautifulSoup
# from lxml.html import parse

# get_tracker_url = lambda no: f"https://dominos.ua/uk/lviv/tracker/{no}/"


# tracker_url = get_tracker_url(7508846)
# content = requests.get(tracker_url).content

# # print(content)

# import lxml.html
# from lxml.html import fromstring

# # print(dir(lxml.html.html_parser))
# # exit()

# page = fromstring(content)
# # print(page)
# data = page.xpath('//html/title/text()')
# print()
# # [a.attrib['href'] for a in result.xpath("//a[@target='_blank']")]


headers = {
	"cookie": "COOKIE"
}

tracker = requests.get("https://dominos.ua/uk/lviv/tracker/", headers=headers).url
tracker_number = tracker.split("/")[-2]

data = requests.get(f"https://dominos.ua/api/v1/tracker/{tracker_number}/get_status/", headers=headers).json()
print(data)
