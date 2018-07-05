from datetime import datetime
from random import random
import requests


def status_text(access_token, group_id):
	msg = str(datetime.now().time()).split('.')[0] + '\nLviv, Ukraine\n\n< '
	msg += requests.get('https://api.vk.com/method/status.get?group_id=%s&access_token=%s&v=5.63' % (group_id, access_token)).json()['response']['text']
	msg += ' />'
	return msg


def slashes():
	lab = ""
	for x in range(20): 
		for i in range(120):
			print random()
			lab += ['/', '\\', '/', '\\', '/', '\\', '/', '\\','/', '\\', ][int(random() * 10)]
		lab += '\n'
	return lab