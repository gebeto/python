try:
    # python 2
    from BytesIO import BytesIO
except ImportError:
    # python 3
    from io import BytesIO

import requests


class TelegramSender(BytesIO):
	token = "445153754:AAHwUF7-CO3Y3qEJXh8XsV-pyqn_WcktSuk"
	chat_id = "@gebeto_music"
	api_method = None
	file = None

	def send(self):
		send_url = "https://api.telegram.org/bot%s/%s" % (self.token, self.api_method)
		resp = requests.post(send_url, data={
			"chat_id": self.chat_id,
			# "title": "Hello",
			# "performer": "",
		}, files={
			self.file: ("Generated.png", self.getvalue(), 'image/png', {'Expires': '0'}),
		})
		print resp.json()
		return resp


class TelegramPhoto(TelegramSender):
	api_method = "sendPhoto"
	file = "photo"

class TelegramDocument(TelegramSender):
	api_method = "sendDocument"
	file = "document"
