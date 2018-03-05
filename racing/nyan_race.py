import os
import time
from threading import Thread
from random import randrange
import sys

rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns) + 1
rows = int(rows)

def print_on(data, x, y):
	cut_size = columns - (x + len(data))
	print ("\033[%(y)s;%(x)sH" % {
		"x": x,
		"y": y
	}) + data
	# }) + data[0:len(data) + cut_size]

def start_car(spaces, top=0):
	# os.system('clear')
	x = spaces
	car = [
		"       █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█",
		"       █░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█",
		"       █░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄",
		"  ▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█",
		"  █░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█",
		"  ▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█",
		"      █░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█",
		"     ▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█",
		"    █░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█",
		"    █▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█",
	]
	for i, row in enumerate(car):
		print_on(row, x, i + 1 + top)

def race(y):
	speed = 0.001 * randrange(0, 30)
	for x in range(0, columns):
		if x % 20 == 0:
			speed = 0.001 * randrange(0, 30)
		time.sleep(0.01 + speed)
		start_car(x, y)
	

# for y in range(0, 12):
# 	race(randrange(0, 12))

for car in range(0, rows / 12):
	Thread(target=race, args=([car * 12])).start()
# Thread(target=race, args=([0])).start()
