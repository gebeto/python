import re
import os
import requests
from configs import auth_headers
from configs import get_video_url

class VideosList():
	def __init__(self, videos_json, chapter_num):
		self.videos = [Video(video, chapter_num, i) for i, video in enumerate(videos_json)]

	def __repr__(self):
		return str(self.videos)

	def __getitem__(self, i):
		return self.videos[i]

	def download(self, folder):
		for video in self.videos:
			video.download(folder)


class Video():
	def __init__(self, video_json, chapter_num, video_num):
		self.urn = video_json["urn"]
		self.title = video_json["title"].replace("/", "").replace("?", "(QUESTION)")
		self.chapter_num = chapter_num
		self.video_num = video_num

	@property
	def url(self):
		ids = re.findall(r"\d+", self.urn)
		url = get_video_url % {
			"course_id": ids[0],
			"video_id": ids[1]
		}
		resp = requests.get(url, headers=auth_headers).json()["url"]["progressiveUrl"]
		return resp

	def __repr__(self):
		return "<Video (%s)>" % self.title

	def create_folder(self, name):
		try:
			os.mkdir(name)
		except:
			pass

	def download(self, folder):
		print self.title
		self.create_folder(folder)
		try:
			file = open("%s/%s.%s. %s.mp4" % (folder, self.chapter_num, self.video_num, self.title))
			file.seek(0, 2)
			if file.tell() > 1000:
				log_progress(100, 100)
				print ""
				return ""
		except:
			pass

		file = requests.get(self.url, stream=True)
		size = file.headers.get("Content-Length")

		open("%s/%s.%s. %s.mp4" % (folder, self.chapter_num, self.video_num, self.title), "wb")
		for i, chunk in enumerate(file.iter_content(int(size) / 100)):
			log_progress(100, i)
			open("%s/%s.%s. %s.mp4" % (folder, self.chapter_num, self.video_num, self.title), "ab").write(chunk)
		print ""


def log_progress(maxx, curr):
	maxx = maxx / 2
	curr = curr / 2
	print "[" + "#"*curr + " "*(maxx-curr) + "]" + " - " + str(curr * 2) + "%\r",

