import requests
from configs import auth_headers
from configs import get_video_url
from configs import get_course_url

from ChaptersList import ChaptersList
from VideosList import VideosList


class CoursesList():
	def __init__(self, courses):
		self.courses = [Course(course) for course in courses]
		# print self.courses

	def __repr__(self):
		return str(self.courses)

	def __getitem__(self, i):
		return self.courses[i]

	def download(self):
		for course in self.courses:
			course.download()


class Course():
	def __init__(self, course_json):
		self.title = course_json["content"]["com.linkedin.learning.api.ListedCourse"]["title"]
		self.urn = course_json["content"]["com.linkedin.learning.api.ListedCourse"]["urn"]
		self.slug = course_json["content"]["com.linkedin.learning.api.ListedCourse"]["slug"]
		self.type = course_json["content"]["com.linkedin.learning.api.ListedCourse"]["courseType"]
		self.duration = course_json["content"]["com.linkedin.learning.api.ListedCourse"]["durationInSeconds"]
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

