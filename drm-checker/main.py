import requests
import re


def test_drm(filename):
	url = "https://albert.apple.com/deviceservices/drmHandshake"
	headers = {
		"Content-Type": "application/x-apple-plist",
		"Accept": "application/xml",
		"User-Agent": "iTunes/12.6.4 (Macintosh; OS X 10.13.6) AppleWebKit/605.3.8",
		# "Accept-Encoding": "gzip",
		# "Connection": "close",
		# "Content-Length": "27886",
	}
	response = requests.post(url, headers=headers, data=open(filename, "r").read())
	# print response
	return response




xml1 = open("1.xml", "r").read()
xml2_base64 = xml1.split("<data>\n")[1].split("</data>")[0]
xml2 = xml2_base64.decode("base64")
json_base64 = xml2.split("<data>\n")[1].split("</data>")[0]
json1 = json_base64.decode("base64")
json2 = json1.replace(
	'"udid":"ca20051db15a9c3ad6903629a94c64b7b17c8051"',
	'"udid":"ca20051db15a9c3ad6903629a94c64b7b17c8051"'
)

new_json_base64_raw = "".join(json2.encode("base64").split("\n"))
new_json_base64 = "\t" + "\n\t".join(re.findall(r"[\w\W]{,68}", new_json_base64_raw))

new_xml2 = xml2.replace(json_base64, new_json_base64)
open("new/xml2.xml", "w").write(new_xml2)
new_xml2_base64_raw = "".join(new_xml2.encode("base64").split("\n")) + "\n\t"
new_xml1 = xml1.replace(xml2_base64, new_xml2_base64_raw)
open("new/xml1.xml", "w").write(new_xml1)


res = test_drm("new/xml1.xml")
print res.text