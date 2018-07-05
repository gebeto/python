import requests

headers = {
	"Connection": "keep-alive",
	"X-BUNDLE-IDENTIFIER": "com.teamtreehouse.Treehouse",
	"Accept": "application/vnd.treehouse.v1",
	"1": "X-Jailbroken",
	"User-Agent": "Treehouse iOS (Build 3869; iPhone; iOS 10.2; Scale/2.00)",
	"Accept-Language": "ru-UA;q=1, en-UA;q=0.9, uk-UA;q=0.8, en-US;q=0.7",
	"Authorization": "Bearer 981eae928e17bd20e3350b8de054f91bfcbcf1530d1cd6922c07029a921113b1",
	"Accept-Encoding": "gzip, deflate",
}


def fix_file_name(fileName):
    fileName = fileName.replace(":", ".")
    fileName = fileName.replace("|", "OR")
    fileName = fileName.replace("&", "AND")
    fileName = fileName.replace("?", ".")
    fileName = fileName.replace('"', "'")
    fileName = fileName.replace('/', "~")
    fileName = fileName.replace(u"\u2019", "'")
    fileName = fileName.replace(u"\u201c", "'")
    fileName = fileName.replace(u"\u201d", "'")
    return fileName


def create_topic_dir(topic):
    try:
        os.mkdir(topic)
    except:
        pass



def download_video(course, title, video_id):
    course = course.strip()
    url = "https://api.teamtreehouse.com/videos/" + str(video_id)
    resp = requests.get(url, headers=headers).json()
    create_topic_dir(course)
    ttitle = title.replace(u"\u2019", "'")
    ttitle = ttitle.replace(u"\u201c", "'")
    ttitle = ttitle.replace(u"\u201d", "'")
    try:
        print "  %s" % (ttitle + ".mp4")
    except:
        print "  SOME ERROR WITH PRINTING NAME"
    # download(course + "/" + title, resp["video_urls"]["high_resolution"])


main_url = "https://api.teamtreehouse.com/syllabi/3082"

resp = requests.get(main_url, headers=headers).json()
title = resp['title']
resp = resp["stages"]
print title
steps = {}
i = 1
for r in resp:
	for step in r['steps']:
		if step['item_type'] == "Video":
			steps[str(i) + '. ' + step['item']['title']] = step['item']['id']
			download_video(title, str(i) + '. ' + step['item']['title'], step['item']['id'])
			# print str(i) + '. ' + step['item']['title']
			i += 1
# print resp