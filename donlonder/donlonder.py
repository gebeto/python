from threading import Thread, Lock
import requests
import shutil
import time
import os

DATA_PATH = "data"

ipsw_url = "http://updates-http.cdn-apple.com/2019FallFCS/fullrestores/061-08416/B909A8DE-C875-11E9-BEC0-C95359F8FB35/iPhone11,8_13.0_17A577_Restore.ipsw"

info = requests.head(ipsw_url).headers
content_length = int(info.get('Content-Length'))


class Loader():
	def __init__(self):
		self.perc = 0
		self.lock = Lock()

	def print(self):
		# print("\r" + ("#" * 10))
		print("\r{} > {}%       ".format("#" * self.perc, self.perc), end='')

	def add(self):
		self.lock.acquire()
		try:
			self.perc += 1
			self.print()
		except:
			pass
		self.lock.release()

loader = Loader()

def calculate_ranges(size, chunks_count = 1):
	chunk_size = int(size / chunks_count)
	chunks = []
	chunked = 0
	for index in range(chunks_count - 1):
		chunked = chunk_size * (index + 1)
		chunks.append([
			chunk_size * index,
			chunked - 1,
		])

	chunks.append([
		chunked,
		size,
	])
	return chunks


def download_chunk_range(url, index, chunk_range):
	def download():
		try:
			content_range = "{}-{}".format(*chunk_range)
			response = requests.get(url, headers={"Range": "bytes={}".format(content_range)})
			filename = "data/file.ipsw{}".format(index)
			open(filename, "wb").write(response.content)
		except:
			print("Downloading error: %s" % index)
			return False
		return True

	while not download():
		pass

	loader.add()


def mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)


# print(content_length)
# print(calculate_ranges(content_length, 100))
# exit()


mkdir(DATA_PATH)
# data_len = 4093153955
data_len = 100000000
data_len = content_length
content_ranges = calculate_ranges(data_len, 100)
for index, content_range in enumerate(content_ranges):
	Thread(target=download_chunk_range, args=(ipsw_url, index, content_range)).start()
loader.print()