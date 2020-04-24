import argparse
import json
import sys
import os
from datetime import datetime

if len(sys.argv) > 1:
	script, action, *message_raw = sys.argv
	message = " ".join(message_raw)
else:
	exit(0)

# print(script, action, message)


# print(action, message)

def get_data_path():
	root = os.path.dirname(__file__)
	data_path = os.path.join(root, "data.json")
	return data_path

def get_data():
	data_path = get_data_path()
	try:
		open(data_path, "r")
	except FileNotFoundError as e:
		with open(data_path, "w") as file:
			file.write(r"{}")

	try:
		return json.load(open(data_path, "r"))
	except json.decoder.JSONDecodeError as e:
		with open(data_path, "w") as file:
			file.write(r"{}")
	data = json.load(open(data_path, "r"))
	return data


def save_data(data):
	data_path = get_data_path()
	json.dump(data, open(data_path, "w"), indent=4)


def start(message):
	data = get_data()
	now = datetime.now()
	data["start_time"] = str(now.isoformat())
	data["items"] = []
	save_data(data)
	print(f"Work is started at {now.strftime('%d/%m/%y | %H:%M')}")


def done(message):
	data = get_data()
	if not message:
		return
	if "items" not in data:
		data["items"] = []
	data["items"].append({
		"time": datetime.now().isoformat(),
		"message": message,
	})
	save_data(data)


def end(args):
	data = get_data()
	start_time = datetime.fromisoformat(data['start_time'])
	end_time = datetime.now()

	if args == 'raw':
		def messages_raw():
			result = []
			for item in data['items']:
				message_list = list(item['message'])
				message_list[0] = message_list[0].upper()
				item['message'] = ''.join(message_list)
				result.append(item['message'])
			return result
		joined_raw = '. '.join(messages_raw())
		print(joined_raw)
	else:
		def messages():
			result = []
			for item in data['items']:
				time = datetime.fromisoformat(item['time']).strftime('%d/%m/%y | %H:%M')
				result.append(f"{time}\t{item['message']}")
			return result
		joined = '\n\t'.join(messages())
		print(f"""Start time:	{start_time.strftime('%d/%m/%y | %H:%M')}
End time:	{start_time.strftime('%d/%m/%y | %H:%M')}
	
	{joined}
""")

def default_action():
	print("No action!")

actions = {
	"start": start,
	"done": done,
	"end": end,
}

actions.get(action, default_action)(message)


# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))