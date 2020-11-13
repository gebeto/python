import requests
import json
from bs4 import BeautifulSoup


def get_thumb(video_id):
    url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"


def get_all_videos():
    response = requests.get("https://www.youtube.com/channel/UCrUF_-DjA00wDXYarG3DYBw/videos")
    content = response.text
    # soup = BeautifulSoup(content, "html.parser")
    # titles = soup.find("a", {"id": "video-title"})
    # print(content)
    json_start = "{" + content.split('window["ytInitialData"] = {')[1]
    json_data = json_start.split("};")[0] + "}"
    tabls = json.loads(json_data)["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]
    videos_tab = tabls[1]
    videos_raw = videos_tab["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["gridRenderer"]["items"]
    videos = [v["gridVideoRenderer"] for v in videos_raw]
    json.dump(videos, open("videos.json", "w"), indent=4, ensure_ascii=False)


get_all_videos()