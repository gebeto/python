import os
import glob

files = glob.glob("scripts/*.js")


for file_path in files:
	file = open(file_path).read()
	print(file.find("wow"))

