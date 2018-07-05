import os
import urllib
import requests
from CoursesList import CoursesList
from SearchCoursesList import SearchCoursesList
from configs import get_bookmarts_url
from configs import auth_headers


def download_bookmarts():
	courses = CoursesList(requests.get(get_bookmarts_url, headers=auth_headers).json()["elements"])
	courses.download()

def search():
	os.system('cls' if os.name == 'nt' else 'clear')
	url = "https://www.linkedin.com/learning-api/search?sortBy=RELEVANCE&start=0&includeLearningPaths=true&keywords=%s&count=30&q=search&enableSpellCheck=false&entityType=COURSE"
	url = url % raw_input("Enter search query: ")
	courses = SearchCoursesList(requests.get(url, headers=auth_headers).json()["elements"])
	courses.select_course()

menu = {
	"1. Search course": search,
	"2. Download MY(Slavik Nychkalo) bookmarks": download_bookmarts,
}

def main():
	# os.system('cls' if os.name == 'nt' else 'clear')
	for k, v in menu.items():
		print k
	index = raw_input("> ")
	if index.isdigit():
		menu.items()[int(index)-1][1]()


while 1:
	main()