# -*- coding: utf-8 -*-

import webbrowser
import requests
import json
import sys

from audioREC import rec

class self():
    FILE = None
    # ACCESS_TOKEN = json.load(open("VKdata.json","r"))["access_token"]
    # USER = requests.get("https://api.vk.com/method/users.get?name_case=nom&access_token=%s&v=5.53&lang=en"%ACCESS_TOKEN).json()["response"][0]
    # USER_ID = USER["id"]


def getAudio(textt, lang="ru"):
    header = {
        "User-Agent": "GoogleTranslate/5.5.55004 (iPhone; iOS 10.2; ru; iPhone6,1)"
	}
    url = "https://translate.google.com/translate_tts?client=it&tl=%s&q=%s&hl=ru&total=1&idx=0&textlen=%s&prev=target&ie=UTF-8" % (lang, textt, len(textt))
    f = open("google.mp3", "wb")
    f.write(requests.get(url, headers=header).content)
    f.close()


def selectFile(file=False):
    # filePath = raw_input("Enter file path: ")
    filePath = "google.mp3"
    if file:
        filePath = file
    print filePath
    if filePath:
        self.FILE = open(filePath, "rb")


def getUploadServer(c_context=None):
    url = "https://api.vk.com/method/docs.getUploadServer"
    data = {
        "lang": "en",
        "type": "audio_message",
        "access_token": c_context.ACCESS_TOKEN,
        "v": "5.54"
    }
    response = requests.post(url, data=data).json()["response"]["upload_url"]
    return response


def upload(c_context=None):
    files = {"file": self.FILE}
    url = getUploadServer(c_context=c_context)
    response = requests.post(url, files=files).json()#["file"]
    # response = requests.post("http://httpbin.org/post", files=files).json()#["file"]
    print response
    return response["file"]

# getAudio('hello')
# selectFile()
# upload()

def docsSave(c_context=None):
    url = "https://api.vk.com/method/docs.save"
    data = {
        "title": "audio.mp3",
        "lang": "ru",
        "file": upload(c_context=c_context),
        "access_token": c_context.ACCESS_TOKEN,
        "v": "5.54"
    }
    response = requests.post(url, data=data).json()
    print response
    return "doc%s_%s"%(response["response"][0]["owner_id"], response["response"][0]["id"])


def sendAudioMessage(chat_id, c_context=None):
    doc = docsSave(c_context=c_context)
    #url = "https://api.vk.com/method/messages.send?peer_id=%s&attachment=%s&access_token=%s&v=5.54"%(raw_input("Enter chat id: "), doc, self.ACCESS_TOKEN)
    # url = "https://api.vk.com/method/messages.send?chat_id=%s&attachment=%s&access_token=%s&v=5.54"%("18", doc, self.ACCESS_TOKEN)
    # url = "https://api.vk.com/method/messages.send?user_id=%s&attachment=%s&access_token=%s&v=5.54"%("122912752", doc, self.ACCESS_TOKEN)
    # url = "https://api.vk.com/method/messages.send?chat_id=%s&attachment=%s&access_token=%s&v=5.54"%("49", doc, self.ACCESS_TOKEN)
    # url = "https://api.vk.com/method/messages.send?chat_id=%s&attachment=%s&access_token=%s&v=5.54"%("43", doc, self.ACCESS_TOKEN)
    # url = "https://api.vk.com/method/messages.send?chat_id=%s&attachment=%s&access_token=%s&v=5.54"%("31", doc, self.ACCESS_TOKEN)
    url = "https://api.vk.com/method/messages.send?peer_id=%s&attachment=%s&access_token=%s&v=5.54"%(chat_id, doc, c_context.ACCESS_TOKEN)
    response = requests.get(url).json()
    c_context.record_btn.setEnabled(True)
    print response
