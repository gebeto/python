from bs4 import BeautifulSoup
import requests
import json


def getJson(productsUrl):
	result = []
	pagesCount = getPagesCount(productsUrl)
	for pageNumber in range(pagesCount):
		url = productsUrl + "/page=%s" % (pageNumber + 1)
		response = requests.get(url).content.split('"usual","products":')[1].split("}]")[0] + "}]"
		response = json.loads(response)
		for product in response:
			result.append({
				"price": product["productPrice"],
				"name": product["productName"]
			})
	return result


def getPagesCount(productsUrl):
	url = productsUrl
	response = requests.get(url).content
	soup = BeautifulSoup(response, "html.parser")
	try:
		return int(soup.find("ul", {"name": "paginator"}).find_all("li")[-1].a.text)
	except:
		return 1


if __name__ == "__main__":
	# resp = getJson("http://rozetka.com.ua/stabilizers/c144719/")
	urlForRequest = raw_input("Parse URL: ")
	fileName = raw_input("Output file name: ")
	json.dump(getJson(urlForRequest), open(fileName + ".json", "wb"), indent=4, ensure_ascii=False)
