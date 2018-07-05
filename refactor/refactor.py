import fnmatch
import json
import os
import re


class FileSearch(object):
	def __init__(self, patterns, keys):
		self.patterns = patterns
		self.keys = keys

	def search_in_file(self, file_content):
		# file_content = file.read()
		result = []
		for key in self.keys:
			result.extend(re.findall(key, file_content))
		return result




def load_config(file_path):
	return json.load(open(file_path, "r"));


def get_files(path):
	result = []
	for root, dirnames, filenames in os.walk(path):
		for filename in fnmatch.filter(filenames, '*.js'):
			result.append(os.path.join(root, filename))
	return result


def create_refactored_file(file_path):
	directory = os.path.dirname(match)
	filename = os.path.basename(match)
	new_file_directory = os.path.join(directory, "ref")
	new_file = os.path.join(new_file_directory, filename)
	if not os.path.exists(new_directory):
		os.mkdir(new_directory)
	return new_file


def statistic(match, rename_list):
	print match, rename_list

def refactor(match, rename_list):
	founded = find_window_pattern(match, [r[0] for r in rename_list])
	replaces = [f for f in rename_list if f[0] in founded]
	if founded:
		new_file = create_refactored_file(match)
		print "Founded %s replaces in %s:" % (len(founded), match)
		print replaces
		for r in replaces:
			print "{:<30}{:->4} window._SG['{}']".format(
				r[0],
				"---->",
				r[1],
			)

		print ""
		new_file_content = replace_window_pattern(match, replaces)
		open(new_file, "w").write(new_file_content)


matches = []
matches.extend(get_files('test'))

config = load_config("refactor_dict.json")
print config



for m in matches:
	print "Processing \"%s\"" % m
	statistic(m, config)
	# refactor(m, rename_list)
	# exit()