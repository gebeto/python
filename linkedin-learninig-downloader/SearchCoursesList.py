import requests
from configs import auth_headers
from configs import get_video_url
from configs import get_course_url


from ChaptersList import ChaptersList
from VideosList import VideosList

import os


class SearchCoursesList():
	def __init__(self, courses):
		self.courses = [SearchCourse(course) for course in courses]

	def __repr__(self):
		return str(self.courses)

	def __getitem__(self, i):
		return self.courses[i]

	def print_list(self):
		for i, course in enumerate(self.courses):
			print "%s. %s" % (i+1, course.title)

	def select_course(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		print "Search result\n"
		self.print_list()
		index = int(input("\nEnter number of course: "))
		os.system('cls' if os.name == 'nt' else 'clear')
		self.courses[index-1].download()

	def download(self):
		for course in self.courses:
			course.download()


class SearchCourse():
	def __init__(self, course_json):
		self.title = course_json["hitInfo"]["com.linkedin.learning.api.search.SearchCourse"]["course"]["title"]
		self.urn = course_json["hitInfo"]["com.linkedin.learning.api.search.SearchCourse"]["course"]["urn"]
		self.slug = course_json["hitInfo"]["com.linkedin.learning.api.search.SearchCourse"]["course"]["slug"]
		self.type = course_json["hitInfo"]["com.linkedin.learning.api.search.SearchCourse"]["course"]["courseType"]
		self.duration = course_json["hitInfo"]["com.linkedin.learning.api.search.SearchCourse"]["course"]["durationInSeconds"]
		self.url = get_course_url % {"course_id": self.urn.split(":")[-1]}

	def __repr__(self):
		return "<Course %s>" % self.slug

	@property
	def chapters(self):
		resp = requests.get(self.url, headers=auth_headers).json()
		chapters = ChaptersList(resp["chapters"])
		return chapters

	def download(self):
		print "\n\n", self.title
		for chapter in self.chapters:
			chapter.download(self.slug)

