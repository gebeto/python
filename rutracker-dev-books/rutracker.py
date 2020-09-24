from . import rutracker

TOPIC = "1426"


limit = rutracker.get_limit(TOPIC)

data = []
for start in range(0, limit + 1, 50):
	print(f"PAGE: {start}")
	data.extend(rutracker.parse_page(TOPIC, start))

data = [dict(t) for t in {tuple(d.items()) for d in data}]

json.dump(data, open("data.json", "w"), indent=4, ensure_ascii=False)