import sublime, sublime_plugin
import json
import webbrowser
import urllib.request
import urllib.parse
from threading import Thread


class HowdyHoPostCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.access_token = sublime.load_settings("HowdyHoPost.sublime-settings").get("access_token")
		if len(self.access_token) < 10:
			menu = ["Получить токен авторизации"]
			self.window.show_quick_panel(menu, self.authorization_select)
		else:
			menu = ["Создать пост", "Создать с браузера"]
			self.window.show_quick_panel(menu, self.post_creation_variant_selected)


	def create_post(self):
		self.window.show_input_panel('Текст поста', '', self.post_text_entered, self.post_text_changed, self.post_text_canceled)

	
	def post_text_entered(self, text):
		print(text)
		self.window.status_message("Создание поста...");
		post_url = "https://api.vk.com/method/wall.post?" + urllib.parse.urlencode({
			"owner_id": "-84392011",
			"message": text,
			"access_token": self.access_token,
			"v": "5.63",
		})
		def async(subl):
			response = str(urllib.request.urlopen(post_url).read())
			subl.post_id = response.split('post_id":')[1].split("}")[0]
			print(response)

			subl.window.show_quick_panel(["Открыть созданый пост"], subl.open_created_post)
			subl.window.status_message("Пост создан успешно!");
		Thread(target=async, args={self}).start()



	def open_created_post(self, index):
		if index == 0:
			post_url = "https://vk.com/howdyho_net?w=wall-84392011_%s" % self.post_id
			webbrowser.open(post_url)


	def post_text_changed(self, text):
		# print(text)
		pass


	def post_text_canceled(self, text):
		print(text)


	def post_creation_variant_selected(self, index):
		print(index)
		if index == 0:
			self.create_post()
		if index == 1:
			webbrowser.open("https://vk.com/howdyho_net")


	def authorization_select(self, index):
		if index == 0:
			auth = "https://oauth.vk.com/authorize?client_id=5744830&v=5.7&scope=messages,photos,wall,groups&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token"
			webbrowser.open(auth)



