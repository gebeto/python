from aiohttp import web, ClientSession
import json


consumer_key = "93469-2d3aed9244846a9aa468dbcf"
redirect_uri = "http://localhost:8080/redirect"


async def post_request(url, json_data):
	async with ClientSession(json_serialize=json.dumps) as session:
		async with session.post(url, json=json_data, headers={"X-Accept": "application/json"}) as response:
			if response.status != 200:
				return None
			resp = await response.json()
	return resp


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
	return web.json_response(auth)

app = web.Application()
app.add_routes([
	web.get('/auth', handle_auth),
	web.get('/redirect/{code}', handle_redirect),
])

if __name__ == '__main__':
	web.run_app(app)

