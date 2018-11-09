from StringIO import StringIO
from threading import Thread
import time
import wave
import requests

from globals import CHANNELS, FORMAT, RATE

from datetime import datetime

import speech_recognition as sr

import certifi


class SendQueue(object):
	_url = "https://api.telegram.org/bot{}/sendVoice"

	def __init__(self, token, chat_id, with_text=False, PROXY = {}):
		super(SendQueue, self).__init__()
		self.PROXY = PROXY
		self.with_text = with_text
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

	def audio_caption(self, source):
		source.seek(0)
		if not self.with_text: return None
		r = sr.Recognizer()
		with sr.AudioFile(message) as source:
			audio = r.record(source)
		try:
			# command = r.recognize_google(audio, language='uk-UA')
			command = r.recognize_google(audio, language='ru-RU')
			return command
		except:
			pass
		return None

	def _send_message(self, message):
		now = datetime.now()
		caption = self.audio_caption(message) or "Recorded:\n{}".format(now.strftime("%Y-%m-%d\n%H:%M:%S"))
		message.seek(0)
		msg_file = message.read()
		res = requests.post(self.url, verify=certifi.where(), data={
			"chat_id": self.chat_id,
			"duration": len(msg_file) / 120000,
			"caption": caption
		}, files={
			"voice": msg_file
		}, proxies=self.PROXY, headers={
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,la;q=0.6,da;q=0.5,uk;q=0.4",
			"Cache-Control": "max-age=0",
			"Connection": "keep-alive",
			# "Cookie": "_ga=GA1.2.811703182.1532686150; _gid=GA1.2.1399802875.1541779040",
			"Host": "api.telegram.org",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
		})
		
