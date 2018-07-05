import sublime, sublime_plugin, sublime_api
from . import requests

class GetTaskCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings('JavaRush.sublime-settings')
        self.sessionID = settings.get('sessionID')
        self.taskKey = self.get_task_names(self.get_tasks())
        self.tasks = list(self.taskKey.keys())
        if self.tasks == []:
            self.tasks = None
        if type(self.tasks) == list:
            self.window.show_quick_panel(self.tasks, self.on_done)
        elif self.tasks == None:
            self.window.show_quick_panel(['Задачек больше нету! Молодец:)'], None)
        else:
            sublime.error_message('Что то пошло не так...')

    def get_task_names(self, taskKeys):
        result = {}
        for taskKey in taskKeys:
            title = self.get_task(taskKey)["title"]
            result[title] = taskKey
            # print(title)
        return result

    def on_done(self, selected):
        if selected == -1:
            return

        self.taskKeyIndex = selected
        TASK = self.get_task(self.taskKey[self.tasks[self.taskKeyIndex]])
        view = sublime.active_window().new_file()
        view.run_command('append', {
                'characters': str(TASK["template"][0]["ContentCode"])
                })
        view.set_syntax_file("Java.sublime-syntax")
        view.set_name(TASK["template"][0]["FileName"])
        print(self.taskKey[self.tasks[self.taskKeyIndex]])

    def get_tasks(self):
        url = "http://javarush.ru/api/rest/task/list.json?sessionId=%s"%self.sessionID
        resp = []
        try:
            resp = requests.get(url).json()
        except:
            sublime.error_message('Подключение к интернету отсутствует!')
        tasks = []
        for each in resp:
            tasks.append(each["taskKey"])
        return tasks

    def get_task(self, taskKey):
        '''
            taskKey:
            title:
            description:
            template[]
            gold:
            silver:
            availible
        '''
        url = "http://javarush.ru/api/rest/task/template/%s.json?sessionId=%s"%(taskKey,self.sessionID)
        resp = requests.get(url).json()
        return resp

class SendTaskCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings('JavaRush.sublime-settings')
        self.view = sublime.active_window().active_view()
        
        self.sessionID = settings.get('sessionID')
        self.url = "http://javarush.ru/api/rest/task/validate.json?sessionId=%s"%self.sessionID
        self.codeRequest = self.view.substr(sublime.Region(0, self.view.size()))
        self.taskKey = ",".join(self.codeRequest.split(";")[0].split(".")[-3::])
        self.Package = self.codeRequest.split(";")[0].split(" ")[1]
        self.inData = ""

        #print(self.view.name());print(sessionID);print(taskKey);print(codeRequest);print(Package)
        self.window.show_input_panel("(SHIFT+ENTER - перевод на новую строку) ВВОД С КЛАВИАТУРЫ:", "", self.on_done, self.on_change, self.on_cancel)
        self.window.status_message("ВЫ МОЖЕТЕ УВЕЛИЧИТЬ ЗОНУ ВВОДА РАСТЯНУВ ЕЕ МЫШКОЙ КАК ЛЮБОЕ ОКНО")


    def on_done(self, text):
        print(text)
        self.inData = text
        self.data = {
            "FileName": self.view.name(),
            "sessionId": self.sessionID,
            "taskKey": self.taskKey,
            "Package": self.Package,
            "inData": self.inData,
            "ContentCode": self.codeRequest
        }
        print(self.data)
        self.resp = requests.post(self.url, json=self.data)
        self.response_processing(self.resp.json())

    def on_change(self, text):
        pass

    def on_cancel(self):
        self.on_done("")

    def response_processing(self, response):
        resp = response["Result"]
        print(resp)
        if resp["compilationOutput"] == None or not resp["compilationOutput"]:
            if resp["validationStatus"] == "INVALID":
                onMessage = ""
                onMessage += "Программа скомпилировалась но работает НЕ ВЕРНО!\n\n"
                onMessage += "Вывод консоли:\n\n" + str(response["Result"]["runOutput"])
                # sublime.error_message(onMessage)
                self.create_panel(onMessage)
            elif resp["validationStatus"] == "UNKNOWN_ERROR":
                self.create_panel("Неизвесная ошибка!\nВозьмите задание заново!")
            elif resp["validationStatus"] == "SUCCESS":
                onMessage = ""
                onMessage += "УСПЕХ! ВСЕ ВЕРНО!\n\n"
                onMessage += "Вывод консоли:\n\n" + str(response["Result"]["runOutput"])
                # sublime.message_dialog(onMessage)
                self.create_panel(onMessage)
        else:
            onMessage = "Ошибка компиляции!!\n\n"+str(resp["compilationOutput"])
            self.create_panel(onMessage)
            
    def create_panel(self, text):
        self.output_view = self.window.get_output_panel("textarea")
        self.window.run_command("show_panel", {"panel": "output.textarea"})
        self.output_view.set_read_only(False)
        self.output_view.run_command("append", {"characters": text})
        self.output_view.set_read_only(True)

