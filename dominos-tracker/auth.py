import requests

auth_url = "https://dominos.ua/api/v1/auth/login/email/"


resp = requests.post(auth_url, data={
	"email": "slavik.nychkalo@gmail.com"
})

print(resp.json())