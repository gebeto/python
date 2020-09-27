from aiohttp import web, ClientSession
import json

from req import post_request, consumer_key


redirect_uri = "http://localhost:8080/redirect"


def get_auth_data():
	return json.load(open("auth.json"))

def set_auth_data(auth):
	json.dump(auth, open("auth.json", "w"), indent=4)


async def auth_request():
	return await post_request('https://getpocket.com/v3/oauth/request', {
		"consumer_key": consumer_key,
		"redirect_uri": redirect_uri,
	})

async def auth_authorize(code):
	return await post_request('https://getpocket.com/v3/oauth/authorize', {
		"consumer_key": consumer_key,
		"code": code,
	})


async def handle_auth(request):
	name = request.match_info.get('name', "Anonymous")
	auth = await auth_request()
	redirect_uri = f"http://localhost:8080/redirect/{auth['code']}"
	redirect_url = f"https://getpocket.com/auth/authorize?request_token={auth['code']}&redirect_uri={redirect_uri}"
	return web.HTTPFound(location=redirect_url)


async def handle_redirect(request):
	code = request.match_info.get("code")
	auth = await auth_authorize(code)
	if auth is None:
		return web.HTTPFound(location="/auth")
	set_auth_data(auth)
	return web.json_response(auth)

app = web.Application()
app.add_routes([
	web.get('/auth', handle_auth),
	web.get('/redirect/{code}', handle_redirect),
])

if __name__ == '__main__':
	web.run_app(app)

