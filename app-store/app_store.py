import json
import requests


headers = {
    "Accept-Language": "ru",
	"User-Agent": "AppStore/2.0 iOS/10.2 model/iPhone6,1 hwp/s5l8960x build/14C92 (6; dt:89)",
	# "X-Apple-Store-Front": countries['ru'],


	# 'X-Apple-I-MD-RINFO': '17106176' ,
	'Accept': '*/*' ,
	'X-Apple-Store-Front': '143469-2,29' ,
	# 'Accept-Language': 'en-us' ,
	# 'Accept-Encoding': 'gzip, deflate' ,
	# 'X-Apple-I-MD-M': 'ABd7uNUS5i/m3YmIw0jeD3pNoeIzZT993oJlj0s8SShvNa+dbYOCGRXq/ZugdLDLaAF9FoyQqXkXWo+U' ,
	# 'X-Apple-Connection-Type': '3G/UA-KYIVSTAR' ,
	# 'X-Apple-I-Client-Time': '2018-11-10T16:31:29Z' ,
	# 'X-Apple-I-MD': 'AAAABQAAABCf4tdNdE23mg0bZEIIxZnfAAAAAw==' ,
	'User-Agent': 'AppStore/2.0 iOS/10.2 model/iPhone6,1 hwp/s5l8960x build/14C92 (6; dt:89)' ,
	# 'X-Dsid': '1915677827',
}

def search(keyword, country = 'ru'):
	countries = {
		"ru": "143469-16,29",
		"us": "",
	}
	search_url = "https://search.itunes.apple.com/WebObjects/MZStore.woa/wa/search?clientApplication=Software&term={}&caller=com.apple.AppStore&version=1"
	res = requests.get(search_url.format(keyword), headers=headers).json()
	items = res['storePlatformData']['native-search-lockup']['results'].values()
	return items

def top():
	top_url = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=ru&genreId=36&l=en"
	res = requests.get(top_url, headers=headers).json()
	items = res['storePlatformData']['lockup']['results'].values()
	return items

def app(ID):
	lookup_url = "https://itunes.apple.com/ru/app/hidden-folks/id{}?l=en&mt=8'"
	res = requests.get(lookup_url.format(ID), headers=headers).json()
	items = res['storePlatformData']['product-dv']['results'].values()
	return items[0]

def categories():
	url = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/categories?cc=ru&genreId=36&l=en"
	res = requests.get(url, headers=headers).json()
	items = res['categories']
	return items

def category_apps(genreId):
	url = "https://itunes.apple.com/ru/genre/ios-photo-video/id{}?l=en&mt=8"
	res = requests.get(url.format(genreId), headers=headers).json()
	items = res['storePlatformData']['lockup']['results'].values()
	print len(items)
	return items


# ap = app('1133544923')
ap = category_apps(6008) # Photos
# print ap
json.dump(ap, open('t.json', 'w'), indent=4)