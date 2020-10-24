import requests

"""
REQ
curl -v -X POST 'http://service.kiwimobility.com/user/sign-with-phone'
 -H 'Accept: application/json, text/plain, */*'
 -H 'Content-Length: 46'
 -H 'Content-Type: application/json;charset=utf-8'
 -H 'Accept-Language: en-us'
 -H 'Accept-Encoding: gzip, deflate'
 -H 'Cookie:'

RES
{"id": 11111}





REQ
curl -v -X POST 'http://service.kiwimobility.com/user/verify'
 -H 'Accept: application/json, text/plain, */*'
 -H 'Content-Length: 30'
 -H 'Content-Type: application/json;charset=utf-8'
 -H 'Accept-Language: en-us'
 -H 'Accept-Encoding: gzip, deflate'
 -H 'Cookie:'

RES
{"token": "TOKEN"}




REQ
curl -v -X GET 'http://service.kiwimobility.com/vehicle/search?latitude=49.844730516318464&longitude=24.007530360235208&zoneId=45'
 -H 'Accept-Language: en-us'
 -H 'Accept: application/json, text/plain, */*'
 -H 'Authorization: Bearer TOKEN'
 -H 'Accept-Encoding: gzip, deflate'
 -H 'Cookie:'
"""

url = "http://service.kiwimobility.com/vehicle/search?latitude=49.844730516318464&longitude=24.007530360235208&zoneId=45"
token = "TOKEN"


def available_scooters():
    response = requests.get(url, headers={
        "Accept-Language": "en-us",
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {token}",
        "Accept-Encoding": "gzip, deflate",
    })
    data = response.json()
    return data
