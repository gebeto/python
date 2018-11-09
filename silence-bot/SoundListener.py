import pyaudio
import time

from globals import FORMAT, CHANNELS, RATE, CHUNK


def encode(s):
	return int(s.encode('hex'), 16)


class SoundListener(object):
	def __init__(self, processing_queue):
		super(SoundListener, self).__init__()
		self.last_record_time = time.time()
		self.recording = False
		self.p = pyaudio.PyAudio()
		self.queue = processing_queue
		self.queue.start()
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
		time_now = time.time()

		if sound_level > 110:
			# print "IS VOICE"
			self.recording = True
			self.last_record_time = time_now

		if self.recording:
			self.frames.append(data)


		if self.frames and len(self.frames) > 10 and self.last_record_time and time_now - self.last_record_time > 1:
			print "Add to queue"
			self.queue.add(self.p, self.frames)
			self.frames = []
			self.recording = False

		if self.frames:
			print "Frames -", len(self.frames), sound_level, time_now - self.last_record_time

		return (data, pyaudio.paContinue)

	def __del__(self):
		stream.stop_stream()
		stream.close()
		p.terminate()