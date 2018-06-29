import fnmatch
import os
import re


def get_files(path):
	result = []
	for root, dirnames, filenames in os.walk(path):
		for filename in fnmatch.filter(filenames, '*.js'):
			result.append(os.path.join(root, filename))
	return result


def find_window_pattern(file_path, names):
	file = open(file_path, "r").read()
	res = re.findall(r"window\['\w+?'\]", file)
	return [f for f in res if f in names]


def replace_window_pattern(file_path, replaces):
	file = open(file_path, "r").read()
	rep = replaces[0]
	for rep in replaces:
		file = file.replace(rep[0],  "window._SG['{}']".format(rep[1]))
	return file


def scan_rename_list(file_path):
	res = []
	lines = open(file_path, "r").readlines()
	i = 1
	for line in lines:
		f = re.findall(r"(window\[['|\"][\w\W]+?['|\"]\])[\w\W]+[//]?>>\s+(\w+)", line)
		if f:
			i += 1
			res.append(f[0])
	return res




def statistic(match, rename_list):
	founded = find_window_pattern(match, [r[0] for r in rename_list])
	founded_count = {}
	for f in founded:
		if not founded_count.get(f):
			founded_count[f] = 0
		founded_count[f] += 1
	replaces = [f for f in rename_list if f[0] in founded]
	if founded:
		print "Founded %s replaces in %s:" % (len(founded), match)
		for r in replaces:
			print "{:>5}. - {:<30}{:->4} window._SG['{}']".format(
				founded_count[r[0]],
				r[0],
				"---->",
				r[1],
			)
		print ""

def refactor(match, rename_list):
	directory = os.path.dirname(match)
	filename = os.path.basename(match)
	new_file_directory = os.path.join(directory, "ref")
	new_file = os.path.join(new_file_directory, filename)
	founded = find_window_pattern(match, [r[0] for r in rename_list])
	replaces = [f for f in rename_list if f[0] in founded]
	if founded:
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
		if not os.path.exists(new_file_directory):
			os.mkdir(new_file_directory)
		open(new_file, "w").write(new_file_content)


matches = []
matches.extend(get_files('UI\\Scripts'))
matches.extend(get_files('mobilejs\\Scripts'))

rename_list = scan_rename_list("./UI/Scripts/160-Settings.js")
print {k: v for k, v in rename_list}
exit();

for m in matches:
	print "Processing \"%s\"" % m
	# statistic(m, rename_list)
	refactor(m, rename_list)
	# exit()