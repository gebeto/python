import json

prefix = """INSERT INTO wp_comments
(comment_post_ID, comment_author, comment_date, comment_date_gmt, comment_approved, comment_content)
VALUES
"""


items = json.load(open("items2.json"))

res = []
for item in items:
	if "подар" in item["text"].lower(): continue
	text = item['text'].strip().replace('"', "'").replace("\n", "\\n")
	if not text: continue
	if len(text) < 20: continue
	res.append(f'(398, "Гость", "{item["date"]}", "{item["date"]}", 1, "{text}")')

open('s.sql', "w").write(prefix + ",\n".join(res))