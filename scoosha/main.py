import json
from pprint import pprint

from services import ewings, kiwi
from config import read_credentials, write_credentials


def json_print(data):
	print(json.dumps(data))


token = read_credentials("ewings")
if not token:
	token = ewings.login()
	write_credentials("ewings", token)

json_print(ewings.available_scooters(token))
