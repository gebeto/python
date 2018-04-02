from threading import Thread


from time import sleep
def runparser(pid, dur):
	def parsing():
		duration = dur
		while duration:
			print "P%s - %s" % (pid, duration)
			duration -= 1
			sleep(1)
	return parsing


class QueueThreadRunner(object):
	def __init__(self, functions, max_limit):
		self.functions = functions
		self.max = max_limit


	def thread_run(self, target):
		target()
		self.add_new()


	def start(self):
		size = 0
		while True:
			if size >= self.max or not self.functions: break;
			p = self.functions.pop(0)
			Thread(target=self.thread_run, args=[p]).start()
			size += 1


	def add_new(self):
		if not self.functions: return
		p = self.functions.pop(0)
		Thread(target=self.thread_run, args=[p]).start()


if __name__ == "__main__":
	parsers = [
		runparser(1, 7),
		runparser(2, 3),
		runparser(3, 3),
		runparser(4, 6),
		runparser(5, 9),
		runparser(6, 20),
		runparser(7, 11),
	]
	q = QueueThreadRunner(parsers, 2)
	q.start()
