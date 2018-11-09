from StringIO import StringIO
from threading import Thread
import time
import wave
import requests

from globals import CHANNELS, FORMAT, RATE

from datetime import datetime


class SendQueue(object):
	_url = "https://api.telegram.org/bot{}/sendVoice"

	def __init__(self, token, chat_id):
		super(SendQueue, self).__init__()
		self.chat_id = chat_id
		self.url = self._url.format(token)
		self.queue = []
		self.thread = Thread(target=self.listen)
		self.thread.setDaemon(1)

	def _to_wav(self, p, frames):
		st = StringIO(b'')
		wf = wave.open(st, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()
		return st

	def listen(self):
		while 1:
			self._listen()
			time.sleep(1)

	def _listen(self):
		if self.queue:
			p, frames = self.queue.pop()
			self._send_message(self._to_wav(p, frames))
			print "SEND --", time.time()

	def start(self):
		self.thread.start()

	def add(self, p, item):
		self.queue.append((p, item))

	def _send_message(self, message):
		message.seek(0)
		msg_file = message.read()
		now = datetime.now()
		res = requests.post(self.url, data={
			"chat_id": self.chat_id,
			"duration": len(msg_file) / 120000,
			"caption": "Recorded:\n{}".format(now.strftime("%Y-%m-%d\n%H:%M:%S"))
		}, files={
			"voice": msg_file
		})
		
