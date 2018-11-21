import requests

filters = []
url = "https://camstore.vsco.co/2.1/camstore/ios?app_id=77357429-48A7-4E5A-A2AF-5D8C6175EFFC&app_version=v4.5.6%20%282040%29&device_model=iPhone%205s&email=bboyheadman%40gmail.com&os_version=9.2"
resp = requests.get(url).json()
for each in resp["products"]:
	try:
		for eacheach in each["presets"]:
			print eacheach["key"]
			filters.append(str(eacheach["key"]))
	except:
		pass

open('vsco.txt','w').write(str(filters).replace("'", '"'))
