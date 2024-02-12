import os
import re

old_date_re = re.compile(r"(\d\d)-(\d\d)-(\d\d\d\d)(-.*)?")

all_files = os.listdir('.')
directories = [f for f in all_files if os.path.isdir(f)]

for d in directories:
  matched = old_date_re.match(d)
  if matched:
    date = matched.group(1)
    month = matched.group(2)
    year = matched.group(3)
    postfix = matched.group(4)
    # print(date, month, year, postfix)
    new_name = f"{year}-{month}-{date}{postfix or ''}"
    print(d, " >> ", new_name)
    # os.rename(d, new_name)

