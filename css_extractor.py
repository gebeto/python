#! /usr/local/bin/python

import sys

# if __name__ == "__main__":
# 	for line in sys.stdin:
# 		sys.stdout.write("DEBUG: got line: " + line)

script, main_file_path, child_file_path = sys.argv
# sys.stdout.write(str(sys.argv))

# exit(0)

# main_file_path = 'main_styles.css'
# child_file_path = 'cart_styles.css'


def get_styles(file_path):
	file = open(file_path).read()
	items = [(i + '}').strip() for i in file.split("}")]
	return items

main = get_styles(main_file_path)
child = get_styles(child_file_path)

new = [i for i in child if not i in main]
res = "\n".join(new)
sys.stdout.write(res)