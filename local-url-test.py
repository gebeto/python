# -*- coding: utf-8 -*-
import requests
from eshopadmin.addons.Paralelizer import Paralelize


def check_auth(urls, res):
	def check_url(url):
		try:
			response = requests.get(url, timeout=1)
			auth = response.headers.get('WWW-Authenticate', None)
			if auth:
				print(url, auth)
		except: pass

	for url in urls:
		check_url(url)
	# Out[3]: {'WWW-Authenticate': 'Basic realm="Please Login"', 'Date': 'Sun, 13 Oct 2019 10:17:13 GMT', 'Connection': 'close', 'Content-Type': 'text/html'}


urls = ['http://192.168.8.{}'.format(i) for i in range(0, 256)]
p = Paralelize(urls, check_auth, threads_count=16)()
