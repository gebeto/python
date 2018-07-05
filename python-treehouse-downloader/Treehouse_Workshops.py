import json, requests, webbrowser, Tkinter, ttk, threading

url = "https://api.teamtreehouse.com/workshops"
header = {
	"Connection": "keep-alive",
	"X-BUNDLE-IDENTIFIER": "com.teamtreehouse.Treehouse",
	"Accept": "application/vnd.treehouse.v1",
	"User-Agent": "Treehouse iOS (Build 3591; iPhone; iOS 9.2; Scale/2.00)",
	"Accept-Language": "uk-UA;q=1, en-UA;q=0.9, ru-UA;q=0.8, uk;q=0.7, en-US;q=0.6",
	"Authorization": "Bearer 32ff0c7a105a60f2441509daf688d224955ef88e419289445ac4182332a0b437",
	"Accept-Encoding": "gzip, deflate"
}

def getVideoLink(id_):
	url = "https://api.teamtreehouse.com/videos/"+str(id_)
	resp = requests.get(url, headers=header).json()["video_urls"]
	videos = {
		"medium": resp["medium_resolution"],
		"high": resp["high_resolution"]
	}
	return videos["high"]

def getWorkshops():
	ret = {}
	workshops = requests.get(url, headers=header).json()
	for workshop in workshops:
		ret[workshop["title"]] = []
		for urls in workshop["workshop_videos"]:
			ret[workshop["title"]].append((urls["video"]["title"], str(urls["video"]["id"])))
	return ret

def setVideos(event):
	global videos
	videos = {}
	videosCB["values"] = [titles for titles, ids in workshops_dict[workshopsCB.get()]]
	for tit, ids in workshops_dict[workshopsCB.get()]:
		videos.update({tit:ids})

def openVideo(event):
	root.update()
	url = getVideoLink(videos[videosCB.get()])
	webbrowser.open(url)


workshops_dict = getWorkshops()
workshops_list = workshops_dict.keys()

root = Tkinter.Tk()
root.title("Treehouse Workshops by Slavik Nychkalo")
workshopsCB = ttk.Combobox(root, values=workshops_list, width=60); workshopsCB.set("Workshops")
videosCB = ttk.Combobox(root, width=60); videosCB.set("Videos")

workshopsCB.bind("<<ComboboxSelected>>", setVideos)
videosCB.bind("<<ComboboxSelected>>", openVideo)

Tkinter.Label(root, text="Select a Workshop and then select a Video\nthen Video will opened in your browser").pack()
workshopsCB.pack()
videosCB.pack()
root.mainloop()
