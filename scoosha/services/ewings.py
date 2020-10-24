import requests
import json


url_base = "https://api.scootapi.com"


HEADERS = {
    "Accept": "*/*",
    "samokatoapp-client": "2a0fceb8-fc66-47e9-8330-f6e1d21c7c80",
    "samokatoapp-platform": "ios",
    "Accept-Language": "en-us",
    "samokatoapp-tenant": "f56a90e4-893b-414e-ba52-a51591a0e909",
    "Content-Type": "application/json",
    "User-Agent": "E-wings/1 CFNetwork/1128.0.1 Darwin/19.6.0",
    "samokatoapp-appversion": "1.6.3",
    "samokatoapp-version": "11",
}

LVIV_LATLON = {
    "latitude": 49.81733283089336,
    "latitudeDelta": 0.25261966210327813,
    "longitude": 24.025546610355377,
    "longitudeDelta": 0.22012084722518566,
}


def request_sms(phone_number):
    url_request_sms = f"{url_base}/auth/request/sms-code"
    request = requests.post(
        url_request_sms,
        headers=HEADERS,
        data=json.dumps({
            "phoneNumber": phone_number
        })
    )
    return request.json()


def confirm_sms(phone_number, code):
    url_confirm_sms = f"{url_base}/auth/login/sms-code"
    request = requests.post(
        url_confirm_sms,
        headers=HEADERS,
        data=json.dumps({
            "phoneNumber": phone_number,
            "smsCode": code
        })
    )
    return request.json()["data"]["token"]


def login():
    phone_number = input("Phone number: ")
    data = request_sms(phone_number)
    code = input("Code from SMS: ")
    token = confirm_sms(phone_number, code)
    return token


def to_simple_shape(scooter):
    return {
        "type": "ewings",
        "id": scooter["scooterId"],
        "title": scooter["publicId"],
        "battery": scooter["batteryPercentage"],
        "location": {
            "lat": scooter["location"]["latitude"],
            "lon": scooter["location"]["longitude"],
        },
    }


def available_scooters(token):
    url_scooters = f"{url_base}/scooters/available"
    response = requests.get(
        url_scooters,
        params=LVIV_LATLON,
        headers=dict(
            HEADERS,
            Authorization=f"Bearer {token}",
        )
    )
    data = response.json()["data"]
    return [to_simple_shape(d) for d in data]
