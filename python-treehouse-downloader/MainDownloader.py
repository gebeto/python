import requests
import os
import time

header = {
    "Connection": "keep-alive",
    "X-BUNDLE-IDENTIFIER": "com.teamtreehouse.Treehouse",
    "Accept": "application/vnd.treehouse.v1",
    "1": "X-Jailbroken",
    "User-Agent": "Treehouse iOS (Build 3869; iPhone; iOS 10.2; Scale/2.00)",
    "Accept-Language": "ru-UA;q=1, en-UA;q=0.9, uk-UA;q=0.8, en-US;q=0.7",
    "Authorization": "Bearer 981eae928e17bd20e3350b8de054f91bfcbcf1530d1cd6922c07029a921113b1",
    "Accept-Encoding": "gzip, deflate",
}


def get_syllabi_title(iD):
    url = "https://api.teamtreehouse.com/syllabi/" + str(iD)
    resp = requests.get(url, headers=header).json()
    print " - " + resp["title"]


def get_bonus_content_series():
    url = "https://api.teamtreehouse.com/bonus_content_series"
    resp = requests.get(url, headers=header).json()
    return resp


def get_all_courses():
    url = "https://api.teamtreehouse.com/syllabi"
    resp = requests.get(url, headers=header).json()
    return resp


def get_topic_of_courle(course):
    return str(course["topics"][0]["name"]) + " -- " + str(course["id"]) + " -- " + str(course["title"])


def get_course_list_in_file(courses):
    result = []
    for course in courses:
        result.append(get_topic_of_courle(course))
    result.sort()
    open("list.txt", "w")
    for each in result:
        open("list.txt", "a").write(each + "\n")


def create_topic_dir(topic):
    try:
        os.mkdir(topic)
    except:
        pass


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


def download(name, url):
    try:
        f = open(name + ".mp4", "rb")
        f.seek(0, 2)
        if f.tell() < 1000:
            print error
    except:
        open(name + ".mp4", "wb").write(requests.get(url).content)


def download_video(course, index, path, title, video_id):
    path = path.strip()
    course = course.strip()
    url = "https://api.teamtreehouse.com/videos/" + str(video_id)
    resp = requests.get(url, headers=header).json()
    create_topic_dir(path + "/" + course)
    ttitle = title.replace(u"\u2019", "'")
    ttitle = ttitle.replace(u"\u201c", "'")
    ttitle = ttitle.replace(u"\u201d", "'")
    try:
        print "  %s" % (index + ttitle + ".mp4")
    except:
        print "  SOME ERROR WITH PRINTING NAME"
    download(path + "/" + course + "/" + index + title,
             resp["video_urls"]["high_resolution"])


def get_learn_adventures():
    url = "https://api.teamtreehouse.com/library"
    resp = requests.get(url, headers=header).json()["learning_adventures"]
    for i, each in enumerate(resp):
        print str(i) + ". " + each["title"]
    return resp


def download_course(iD):
    url = "https://api.teamtreehouse.com/syllabi/" + str(iD)
    resp = requests.get(url, headers=header).json()
    path = resp["topics"][0]["name"]
    create_topic_dir(path)  # Creating TOPIC folder
    i = 1
    for stage in resp["stages"]:
        print str(i) + ".", fix_file_name(stage["title"])
        j = 1
        for step in stage["steps"]:
            if step["item_type"] == "Video":
                # print "  %d.%d. %s" % (i, j, step["item"]["title"])
                download_video(
                    fix_file_name(resp["title"]),
                    "%d.%d. " % (i, j),
                    path,
                    fix_file_name(step["item"]["title"]),
                    step["item"]["id"]
                )
                j += 1
        i += 1
while 1:
    menu = raw_input(
        "\n1. Show topics with key\n2. Single course downloader\n3. All topic courses download\n4. Download pack of courses\n>> ")
    print ""
    if menu == "1":
        key = raw_input("\nEnter topic: ")
        for each in open("list.txt").read().split("\n"):
            if each.lower().find(key.lower()) > -1:
                print each
        print ""

    elif menu == "2":
        name = raw_input("Enter course id: ")
        download_course(name)

    elif menu == "3":
        name = raw_input("Enter topic name: ")
        for each in open("list.txt").read().split("\n"):
            course = each.split(" -- ")
            if len(course) == 3:
                if course[0] == name:
                    print course[2]
                    print "DOWNLOADING"
                    downloading = True
                    while downloading:
                        download_course(course[1])
                        downloading = False
    elif menu == "4":
        serie = get_learn_adventures()
        num = input("Index of serie: ")
        for each in serie[num]["syllabi"]:
            get_syllabi_title(each["syllabus_id"])
        if (raw_input("Download the serie of courses? y/n: ") == "y"):
            for each in serie[num]["syllabi"]:
                download_course(each["syllabus_id"])

    elif menu == "5":
        get_course_list_in_file(get_all_courses())
