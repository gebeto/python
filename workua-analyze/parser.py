import re
import json
import requests
from bs4 import BeautifulSoup

domain = "https://www.work.ua"
all_base_url = "https://www.work.ua/jobs-%(query)s/?page=%(page)s"
lviv_base_url = "https://www.work.ua/jobs-lviv-%(query)s/?page=%(page)s"
city_base_url = "https://www.work.ua/jobs-%(city)s-%(query)s/?page=%(page)s"


def string_to_query(string):
	return string.replace(" ", "+")


def parse_works(query, page=1):
	result = []
	response = requests.get(lviv_base_url % {
		"query": query,
		"page": page
	}).content
	soup = BeautifulSoup(response, "html.parser")
	if not soup.find("div", {"class": "card"}):
		return []
	works = soup.find_all("div", {"class": "card"})
	result += [{
		"url": domain + w.find("h2").a.get("href"),
		"title": w.find("h2").a.text
	} for w in works if w.find("h2") and w.find("h2").find("a")]
	result += parse_works(query, page=page+1)
	return result

def parse_requirements(work):
	print "WORK --------", work["title"], work["url"]
	response = requests.get(work["url"]).content
	soup = BeautifulSoup(response, "html.parser")
	reqs = soup.find(text=[
		re.compile(r'required', flags=re.I),
		re.compile(r'requirements', flags=re.I),
		re.compile(r'responsibilities', flags=re.I),
		re.compile(r'вимоги', flags=re.I),
		re.compile(r'требования', flags=re.I),
		r'Вимоги:',
		r'Требования:',
		r'Requirments:',

	])
	if not reqs:
		print work["url"]
		return []
	reqs = reqs.parent.findNext("ul").find_all("li")
	reqs = [r.text.replace(u"\xa0", "").replace(u"\u2014", "").strip() for r in reqs]
	reqs = [r for r in reqs if r.strip()]
	return reqs


def array_split(requirements):
	res = []
	for req in requirements:
		res += re.split(r"[.,\(\):\s+=\/-;-]*", req)
	return list(set([r.strip().lower() for r in res if len(r.strip()) > 1]))



def main():
	s_query = string_to_query("it")
	s_works = []
	s_tags = []

	s_works = parse_works(s_query)
	for work in s_works:
		work["tags"] = array_split(parse_requirements(work))
		s_tags += work["tags"]

	s_tags = list(set(s_tags))
	s_tags.sort(key=lambda x: len(x))

	json.dump({
		"tags": s_tags,
		"works": s_works,
	}, open("src/work_data.json", "wb"), indent=4)




if __name__ == '__main__':
	if raw_input("Parse data? (y/n): ").lower() == "y":
		main()
