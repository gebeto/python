from VideosList import VideosList

class ChaptersList():
	def __init__(self, chapters_json):
		self.chapters = [Chapter(chapter, i) for i, chapter in enumerate(chapters_json)]

	def __repr__(self):
		return str(self.chapters)

	def __getitem__(self, i):
		return self.chapters[i]

	def download(self, folder):
		for chapter in self.chapters:
			chapter.download(folder)


class Chapter():
	def __init__(self, chapter_json, chapter_num):
		self.title = chapter_json["title"]
		self.videos = VideosList(chapter_json["videos"], chapter_num)
		self.chapter_num = chapter_num

	def __repr__(self):
		return "<Chapter (%s)>" % self.title

	def download(self, folder):
		print "\nChapter", self.chapter_num
		self.videos.download(folder)
		

