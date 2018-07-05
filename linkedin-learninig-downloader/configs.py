import os
import requests

cookie = ''
try:
	cookie = requests.get('https://gebeto.github.io/LINKEDIN_COOKIE.txt').content
	print "COOKIE LOADED FROM SERVER"
except:
	try:
		cookie = open('%s/COOKIE.txt' % os.path.dirname(__file__)).read()
	except:
		cookie = open('COOKIE.txt').read()
		print "COOKIE LOADED FROM FILE"

auth_headers = {
	"Csrf-Token": "ajax:1046650925137765397",
	"x-li-lang": "en_US",
	"Accept-Language": "en-us",
	"Accept-Encoding": "gzip, deflate",
	"X-RestLi-Protocol-Version": "2.0.0",
	"x-lil-intl-library": "en_US",
	"User-Agent": "Learning/0.3.338 CFNetwork/808.2.16 Darwin/16.3.0",
	"Cookie": cookie,
	"X-LI-Track": '{"orientation":"P","osName":"iOS","clientVersion":"0.3.338","timezoneOffset":"3","osVersion":"10.2","appId":"com.linkedin.Learning","locale":"en_UA","deviceType":"iphone","deviceId":"133BCE1E-B07B-4AB5-8D2C-7ECC0BBB561D","clientMinorVersion":"1.1.26","language":"en-UA","model":"iphone6_1","carrier":"Kyivstar","clientTimestamp":1500033620876}',
}

get_video_url = "https://www.linkedin.com/learning-api/detailedCourses/%(course_id)s/detailedVideos/%(video_id)s"
get_course_url = "https://www.linkedin.com/learning-api/detailedCourses/%(course_id)s"
get_bookmarts_url = "https://www.linkedin.com/learning-api/listedBookmarks?q=listedBookmarks&start=0&count=30"



'Accept: */*'
'X-RestLi-Protocol-Version: 2.0.0'
'x-lil-intl-library: en_US'
'X-LI-Track: {"orientation":"P","osName":"iOS","clientVersion":"0.3.338","timezoneOffset":"3","osVersion":"10.2","appId":"com.linkedin.Learning","locale":"en_UA","deviceType":"iphone","deviceId":"133BCE1E-B07B-4AB5-8D2C-7ECC0BBB561D","clientMinorVersion":"1.1.26","language":"en-UA","model":"iphone6_1","carrier":"Kyivstar","clientTimestamp":1500105495529}'
'Csrf-Token: ajax:1046650925137765397'
'x-li-lang: en_US'
'Accept-Language: en-us'
'Accept-Encoding: gzip, deflate'
'Cookie: '