import sys
import re


data = sys.stdin.read()

pattern = re.compile(r"^TMS-\d{,2}:\s")

sys.stdout.write(pattern.sub("", data))


"""
git filter-branch -f --msg-filter 'python3 /Users/gebeto/Desktop/Github/python-projects/fil.py' --tag-name-filter cat -- --all
"""