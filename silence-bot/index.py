"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
import time
import requests

from threading import Thread

TOKEN = open("token.txt").read()
url = "https://api.telegram.org/bot{}/sendVoice".format(TOKEN)


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

frames = []

from StringIO import StringIO

def to_wav(p, frames):
	st = StringIO(b'')
	wf = wave.open(st, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	st.seek(0)
	return st

def encode(s):
	return int(s.encode('hex'), 16)


def send_message(message):
	# print message.read()

	res = requests.post(url, data={
		"chat_id": '@sounds_great_gebeto',
	}, files={
		"voice": message.read()
	})

class SenderBot(object):
	def __init__(self):
		super(SenderBot, self).__init__()
		self.queue = []
		self.thread = Thread(target=self.listen)

	def listen(self):
		while 1:
			self._listen()
			time.sleep(1)

	def _listen(self):
		if self.queue:
			p, frames = self.queue.pop()
			send_message(to_wav(p, frames))
			print time.time()

	def start(self):
		self.thread.start()

	def add(self, p, item):
		self.queue.append((p, item))
		

class ListenerBot(object):
	def __init__(self):
		super(ListenerBot, self).__init__()
		self.p = pyaudio.PyAudio()
		self.sender = SenderBot()
		self.sender.start()
		self.frames = []
		
		self.stream = self.p.open(
			format=FORMAT,
			channels=CHANNELS,
			rate=RATE,
			input=True,
			frames_per_buffer=CHUNK,
			stream_callback=self.callback
		)

	def callback(self, data, frame_count, time_info, status):
		sound_level = sum(map(encode, data)) / len(data)

		if sound_level > 100:
			print "IS VOICE"
			self.frames.append(data)
		else:
			if self.frames:
				self.sender.add(self.p, self.frames)
				self.frames = []
			print "SILENCE"

		return (data, pyaudio.paContinue)

	def __del__(self):
		stream.stop_stream()
		stream.close()
		p.terminate()


lis = ListenerBot()

raw_input("Press enter to stop")

del lis
