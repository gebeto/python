import webbrowser
import Tkinter
import ttk
import requests

course_videos_ids = []

header = {
	"Connection": "keep-alive",
	"X-BUNDLE-IDENTIFIER": "com.teamtreehouse.Treehouse",
	"Accept": "application/vnd.treehouse.v1",
	"User-Agent": "Treehouse iOS (Build 3591; iPhone; iOS 9.2; Scale/2.00)",
	"Accept-Language": "uk-UA;q=1, en-UA;q=0.9, ru-UA;q=0.8, uk;q=0.7, en-US;q=0.6",
	"Authorization": "Bearer 32ff0c7a105a60f2441509daf688d224955ef88e419289445ac4182332a0b437",
	"Accept-Encoding": "gzip, deflate"
}

def download(path, name, url):
	try:
		f = open(path+"/"+name+".mp4", "rb")
		f.seek(0,2)
		if f.tell()<1000:
			print error
	except:
		open(path+"/"+name+".mp4", "wb").write(requests.get(url).content)

def getCourses():
	courses = {}
	url = "https://api.teamtreehouse.com/library"
	resp = requests.get(url, headers=header).json()["courses"][0]["syllabi"]
	for each in resp:
		topic = each["topics"][0]["name"]
		courses[topic] = {}
	for each in resp:
		topic = each["topics"][0]["name"]
		courses[topic].update({each["title"]: {
			"name": each["title"],
			"id": each["id"],
			"updated": each["updated_at"],
			"skill_level": each["skill_level"],
			"description": each["description"]
		}})
	return courses

def getCourse(course_id):
	course = {}
	resp = requests.get("https://api.teamtreehouse.com/syllabi/%s"%str(course_id), headers=header).json()
	course.update({"name": resp["title"]})
	course.update({"count": 0})
	course.update({"video_ids": {}})
	course.update({"description": {}})
	course.update({"keys": []})
	cnt = 0
	for stage in resp["stages"]:
		for step in stage["steps"]:
			if step["item"]["type"] == "Video":
				cnt += 1
				course["count"] += 1
				course["keys"].append(str(cnt)+". "+step["item"]["title"])
				course["description"].update({
						str(cnt)+". "+step["item"]["title"]: step["item"]["description"]
					})
				course["video_ids"].update({
						str(cnt)+". "+step["item"]["title"]: step["item"]["id"]
					})
	return course

def getVideoLink(id_):
	url = "https://api.teamtreehouse.com/videos/"+str(id_)
	resp = requests.get(url, headers=header).json()["video_urls"]
	videos = {
		"medium": resp["medium_resolution"],
		"high": resp["high_resolution"]
	}
	return videos

def sorting(mas):
	for i in range(0, len(mas)):
		pass

COURSES = getCourses()
topic = ""
video_ids = {}
course = ""
courseDescription = ""
videoDescription = ""
quality = "high"

def comboTopics_event(event):
	global topic
	topic = comboTopics.get()
	comboCourses["values"] = COURSES[topic].keys()

def comboCourses_event(event):
	global video_ids, videoDescription, courseDescription, course, course_videos_ids
	comboCourse.set("loading...")
	root.update()
	course = comboCourses.get()
	courseId = COURSES[topic][course]["id"]
	courseDescription = COURSES[topic][course]["description"]
	content_Course = getCourse(courseId)
	video_ids = content_Course["video_ids"]
	course_videos_ids = content_Course #-------------------------------
	videoDescription = content_Course["description"]
	comboCourse["values"] = content_Course["keys"]
	description.delete(0.0, Tkinter.END)
	description.insert(Tkinter.CURRENT, courseDescription)
	comboCourse.set("")

def comboCourse_event(event):
	url = getVideoLink(video_ids[comboCourse.get()])[quality]
	description.delete(0.0, Tkinter.END)
	description.insert(Tkinter.CURRENT, videoDescription[comboCourse.get()])
	webbrowser.open(url)

def medium():
	global quality
	quality = "medium"

def high():
	global quality
	quality = "high"

def name_fixer(name):
	name = name.replace(":", ";")
	name = name.replace("?", ".")
	name = name.replace('"', "'")
	name = name.replace('/', "~")
	return name

def downloadWindow():
	import os, threading
	win = Tkinter.Tk()
	#win.attributes("-toolwindow",1)
	folder = comboCourses.get()
	try:
		os.mkdir(folder)
	except:
		pass
	def CIRCLE():
		for each in course_videos_ids["keys"]:
			#print each
			Tkinter.Label(win, text=each).pack()
			download(folder, name_fixer(each), getVideoLink(course_videos_ids["video_ids"][each])[quality])
		Tkinter.Label(win, text="!!!!DONE!!!!").pack()
	t1 = threading.Thread(target=CIRCLE)
	t1.start()
	win.mainloop()

root = Tkinter.Tk()
root.title("Treehouse by SlavikNychkalo")
root.geometry("392x250")
root.resizable(width=False, height=False)
#root.attributes("-toolwindow",1)

# FORM
comboTopics = ttk.Combobox(root, values=COURSES.keys(), width=25)
comboCourses = ttk.Combobox(root, width=25)
comboCourse = ttk.Combobox(root, width=25)
description = Tkinter.Text(root, height=11, width=55)
qualityHigh = Tkinter.Radiobutton(root, value=2, text="High (720p)", command=high, indicatoron=0)
qualityMedium = Tkinter.Radiobutton(root, value=1, text="Medium (360p)", command=medium, indicatoron=0);

# BINDS
comboTopics.bind("<<ComboboxSelected>>", comboTopics_event)
comboCourses.bind("<<ComboboxSelected>>", comboCourses_event)
comboCourse.bind("<<ComboboxSelected>>", comboCourse_event)

# PACK
Tkinter.Label(root, text="Topic").place(x=4, y=5)
comboTopics.place(x=50, y=5)
Tkinter.Label(root, text="Course").place(x=4, y=30)
comboCourses.place(x=50, y=30)
Tkinter.Label(root, text="Video").place(x=4, y=55)
comboCourse.place(x=50, y=55)
description.place(y=80)
Tkinter.Label(root, text="Quality").place(x=299)
qualityHigh.place(x=286, y=22)
qualityHigh.select()
qualityMedium.place(x=276, y=50)
Tkinter.Button(root, text="Download Course", command=downloadWindow).place(x=280, y=220)

root.mainloop()
