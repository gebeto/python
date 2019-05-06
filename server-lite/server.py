from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json

PORT_NUMBER = 8080


content_types = {
	"application/json": json.dumps,
	"text/html": str,
}


routes = {}


def prepare_query(query_string):
	res = {}
	if not query_string: return res
	for pare in query_string.split("&"):
		splitted = pare.split("=")
		key = splitted.pop(0) if splitted else None
		if key:
			value = splitted.pop(0) if splitted else None
			if value:
				res[key] = value
	return res


class route(object):
	def __init__(self, path, content_type="text/html", *args):
		self.path = path
		self.content_type = content_type

	def __call__(self, route_handler):
		def handler(request, query):
			request.send_response(200)
			request.send_header('Content-type', self.content_type)
			request.end_headers()
			preparer = content_types[self.content_type]
			return preparer(route_handler(prepare_query(query)))
		routes[self.path] = handler
		return handler


class ServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		splitted_path = self.path.split("?")
		path = splitted_path.pop(0) if splitted_path else None
		query = splitted_path.pop(0) if splitted_path else None
		route = routes.get(path)
		if route == None:
			self.send_response(404)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write("404")
		else:
			response = route(self, query)
			self.wfile.write(response)
		return


def start_server(PORT_NUMBER):
	try:
		server = HTTPServer(('', PORT_NUMBER), ServerHandler)
		print 'Started httpserver on port ', PORT_NUMBER
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()


@route(path="/")
def hello(query):
	return "Heeeelllo" +  json.dumps(query)

@route(path="/hey")
def hey(query):
	return "HEEEY" + json.dumps(query)

@route(path="/json", content_type="application/json")
def json(query):
	return query


start_server(PORT_NUMBER)