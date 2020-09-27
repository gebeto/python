from aiohttp import ClientSession
import json


consumer_key = "93469-2d3aed9244846a9aa468dbcf"


async def post_request(url, json_data):
	async with ClientSession(json_serialize=json.dumps) as session:
		async with session.post(url, json=json_data, headers={"X-Accept": "application/json"}) as response:
			if response.status != 200:
				return None
			resp = await response.json()
	return resp


async def get_request(url):
	async with ClientSession(json_serialize=json.dumps) as session:
		async with session.get(url, headers={"X-Accept": "application/json"}) as response:
			if response.status != 200:
				return None
			resp = await response.json()
	return resp