import requests


"""
REQ
curl -v -X POST 'https://api.scootapi.com/auth/request/sms-code'
-H 'samokatoapp-client: 2a0fceb8-fc66-47e9-8330-f6e1d21c7c80'
-H 'samokatoapp-version: 11'
-H 'samokatoapp-platform: ios'
-H 'samokatoapp-appversion: 1.6.3'
-H 'samokatoapp-tenant: f56a90e4-893b-414e-ba52-a51591a0e909'
-H 'Content-Type: application/json'
-H 'Cookie:'
-d '{"phoneNumber":"380970067238"}'

RES
PPPP

REQ
curl -v -X POST 'https://api.scootapi.com/auth/login/sms-code'
 -H 'samokatoapp-platform: ios'
 -H 'Content-Type: application/json'
 -H 'Accept: */*'
 -H 'samokatoapp-client: 2a0fceb8-fc66-47e9-8330-f6e1d21c7c80'
 -H 'samokatoapp-appversion: 1.6.3'
 -H 'samokatoapp-tenant: f56a90e4-893b-414e-ba52-a51591a0e909'
 -H 'Accept-Language: en-us'
 -H 'Content-Length: 47'
 -H 'Accept-Encoding: gzip, deflate, br'
 -H 'samokatoapp-version: 11'

RES
PPPPP


REQ
curl -v -X GET 'https://api.scootapi.com/scooters/available?latitude=49.842957&latitudeDelta=0.0043&longitude=24.031111&longitudeDelta=0.0034'
 -H 'samokatoapp-platform: ios'
 -H 'Accept: */*'
 -H 'samokatoapp-client: 2a0fceb8-fc66-47e9-8330-f6e1d21c7c80'
 -H 'samokatoapp-tenant: f56a90e4-893b-414e-ba52-a51591a0e909'
 -H 'samokatoapp-appversion: 1.6.3'
 -H 'Accept-Language: en-us'
 -H 'Authorization: Bearer TOKEN'
 -H 'Accept-Encoding: gzip, deflate, br'
 -H 'samokatoapp-version: 11'
 -H 'Cookie:'

RES
PPPP

"""


url = "https://api.scootapi.com/scooters/available?latitude=49.81733283089336&latitudeDelta=0.25261966210327813&longitude=24.025546610355377&longitudeDelta=0.22012084722518566"
token = "TOKEN"


def available_scooters():
    response = requests.get(url, headers={
        "Authorization": f"Bearer {token}",
        "samokatoapp-platform": "ios",
        "Accept": "*/*",
        "samokatoapp-client": "2a0fceb8-fc66-47e9-8330-f6e1d21c7c80",
        "samokatoapp-tenant": "f56a90e4-893b-414e-ba52-a51591a0e909",
        "samokatoapp-appversion": "1.6.3",
        "Accept-Language": "en-us",
        "Accept-Encoding": "gzip, deflate, br",
        "samokatoapp-version": "11",
    })
    data = response.json()
    return data
