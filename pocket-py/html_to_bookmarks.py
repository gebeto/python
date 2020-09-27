from bs4 import BeautifulSoup
import api

soup = BeautifulSoup(open("bookmarks.html"), "html.parser")

links = soup.find_all("a")


for link in links:
	# print(link["href"], link.text.strip())
	api.add_bookmark(link["href"], link.text.strip())
