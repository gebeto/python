import requests, os, time

header = {
	"Connection": "keep-alive",
	"Cookies": "_treehouse_session=NFM1Z3V6MmZMam9XdFc0RmZFekxZaVJndkFobFNYKzY2QnpSVWtiRmJiSmN4MEZNNERzTXozdzV1S0VVcVM1UjFQb2FuSUpHZlBKdm4yV1lBM1MrZ3R1M25YNUhRaVlFN1hkeVlrN2FtcWZlMms2UkRJYkxNSzZjbGcyUVk3TGFxbkNqaFZEaERDR2h5RE9LbzlOdHpBbll2TFlpRVpDMkM4bDNGYkVlOW9MMDJEYzNLZ0ExQnlveG0vR1JHUk92U1R6cG1HTlZYaWQ3c2NPNW44dHYzUT09LS1nRHloYUhXTVZYaVlmUVpsckRmLzhnPT0%3D--5b7510bc1067b8d328af4cdbfe88cbf295429ab4; sid=7ec61071-be9a-48a8-9388-d13d9c562962",
	"X-BUNDLE-IDENTIFIER": "com.teamtreehouse.Treehouse",
	"Accept": "application/vnd.treehouse.v1",
	"User-Agent": "Treehouse iOS (Build 3591; iPhone; iOS 9.2; Scale/2.00)",
	"Accept-Language": "uk-UA;q=1, en-UA;q=0.9, ru-UA;q=0.8, uk;q=0.7, en-US;q=0.6",
	"Authorization": "Bearer 981eae928e17bd20e3350b8de054f91bfcbcf1530d1cd6922c07029a921113b1",
	"Accept-Encoding": "gzip, deflate"
}

def get_syllabi_title(iD):
	url = "https://api.teamtreehouse.com/syllabi/"+str(iD)
	resp = requests.get(url, headers=header).json()
	print " - %s"%resp["title"]

def get_learn_adventures():
	url = "https://api.teamtreehouse.com/library"
	resp = requests.get(url, headers=header).json()["learning_adventures"]
	for i, each in enumerate(resp):
		print "  %d. %s"%(i, each["title"])
	return resp



serie = get_learn_adventures()
while 1:
	num = input("\nWhat learn for(index): ")
	for each in serie[num]["syllabi"]:
		get_syllabi_title( each["syllabus_id"] )



