import json


data = json.load(open("items.json"))


for item in data:
	new_date = item["date"]
	date, time = new_date.split(" ")
	date = date.split(".")
	date.reverse()
	date = ".".join(date)
	print(date, time)
	item["date"] = f"{date} {time}"

json.dump(data, open("items2.json", "w"), indent=4, ensure_ascii=False)
