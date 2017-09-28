import os
import sys
import json
import urllib
import socket
import requests

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.config import Configurator

from wsgiref.simple_server import make_server

import rozetka

here = os.path.dirname(os.path.abspath(__file__))

def priceFilter(products, priceFrom, priceTo):
	# res = []
	# for product in products:
	# 	if (float(product["price"]) > priceFrom and float(product["price"]) < priceTo):
	# 		res.append(product)
	res = [product for product in products if (float(product["price"]) > priceFrom and float(product["price"]) < priceTo)]
	return sorted(res, key=lambda x: float(x["price"]))


# views
@view_config(route_name='index', renderer='index.mako')
def list_view(request):
	if "url" in request.params:
		print request.params
		url = urllib.unquote(request.params["url"])
		print url
		# Try parse from url
		try:
			responseJson = rozetka.getJson("http://" + url)
			# print responseJson
			if "json" in request.params:
				print "JSON"
				return Response(json.dumps(responseJson), content_type="application/json")
			return {"products": sorted(responseJson, key=lambda x: float(x["price"]))}
		except:
			# products = json.load(open("stabilizers.json"))
			return {'error': 1}
			
	return {'products': {}}


if __name__ == '__main__':
	# configuration settings
	settings = {}
	settings['reload_all'] = True
	settings['debug_all'] = True
	settings['mako.directories'] = os.path.join(here, 'templates')
	# settings['mako.directories'] = 'templates'

	# configuration setup
	config = Configurator(settings=settings)
	
	# add mako templating
	config.include('pyramid_mako')

	# routes setup
	config.add_route('index', '/')
	
	# static view setup
	config.add_static_view('static', os.path.join(here, 'static'))
	
	# scan for @view_config and @subscriber decorators
	config.scan()

	# serve app
	app = config.make_wsgi_app()
	if sys.argv[-1] == "-local" or len(sys.argv) == 1:
		server = make_server('0.0.0.0', 8080, app)
		print "Server started on: http://localhost:8080"
	elif sys.argv[-1] == "-wifi":
		server = make_server(socket.gethostbyname(socket.gethostname()), 8080, app)
		print "Server started on: http://%s:8080" % socket.gethostbyname(socket.gethostname())

	# server = make_server('192.168.0.102', 80, app)
	server.serve_forever()