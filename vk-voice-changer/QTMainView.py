# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from PySide.QtGui import *
import requests, json, os
import threading
from Uploader import rec, selectFile, sendAudioMessage
import QTLogin

# rec('record.mp3', rate=20000)
# selectFile('record.mp3')
# sendAudioMessage(31)


class MainView(object):
	def setupUi(self, Window):
		Window.setObjectName("Window")
		self.verticalLayout = QtGui.QVBoxLayout(Window)
		self.horizontalLayout = QtGui.QVBoxLayout()
		self.pitch_size_layout = QtGui.QHBoxLayout()
		self.chat_id_layout = QtGui.QHBoxLayout()
		# self.dialogs_list = QtGui.QListWidget(Window)
		# self.dialogs_list.setObjectName("stickers_lw")
		# self.horizontalLayout.addWidget(self.dialogs_list)

		# ChatId control
		self.chat_id_input = QtGui.QLineEdit(Window)
		self.chat_id_title = QtGui.QLabel("Chat Id:")
		self.chat_id_layout.addWidget(self.chat_id_title)
		self.chat_id_layout.addWidget(self.chat_id_input)

		# Pinch control
		self.pitch_size = QtGui.QSlider(QtCore.Qt.Orientation.Horizontal, Window)
		self.pitch_size.setObjectName("pitch_size")
		self.horizontalLayout.addWidget(self.pitch_size)
		self.pitch_size_title = QtGui.QLabel("Pitch: ")
		self.pitch_size_layout.addWidget(self.pitch_size_title)
		self.pitch_size_input = QtGui.QLineEdit("44100")
		self.pitch_size_input.setValidator(QtGui.QIntValidator(10000, 60000))


		# Record button
		self.record_btn = QtGui.QPushButton(Window)
		self.record_btn.setObjectName("record_btn")

		self.verticalLayout.addLayout(self.chat_id_layout)
		self.pitch_size_layout.addWidget(self.pitch_size_input)
		self.horizontalLayout.addLayout(self.pitch_size_layout)
		self.horizontalLayout.addWidget(self.record_btn)
		self.verticalLayout.addLayout(self.horizontalLayout)

		self.retranslateUi(Window)
		QtCore.QMetaObject.connectSlotsByName(Window)

	def retranslateUi(self, Window):
		Window.setWindowTitle(QtGui.QApplication.translate("Window", "Voice Changer", None, QtGui.QApplication.UnicodeUTF8))
		self.record_btn.setText(QtGui.QApplication.translate("Window", "Record", None, QtGui.QApplication.UnicodeUTF8))
		self.pitch_size.setRange(10000, 60000)
		self.pitch_size.setSingleStep(1000)
		self.pitch_size.setPageStep(1000)
		self.pitch_size.setTickInterval(1000)
		self.pitch_size.setValue(44100)
		print self.pitch_size.value()

class VoiceChanger(QWidget, MainView):
	def __init__(self, ACCESS_TOKEN):
		super(VoiceChanger, self).__init__()
		self.setupUi(self)
		self.ACCESS_TOKEN = ACCESS_TOKEN
		self.PITCH = 44100
		self.PEER_ID = 0
		self.STARTED = False


		# self.dialogs_list.itemClicked.connect(self.dialog_list_item_select)
		self.record_btn.clicked.connect(self.start_recording_handler)
		self.pitch_size.valueChanged.connect(self.pitch_change_handler)
		self.pitch_size_input.textEdited.connect(self.pitch_change_handler)
		self.chat_id_input.textEdited.connect(self.chat_id_change_handler)

	def pitch_change_handler(self, val):
		self.PITCH = val
		self.pitch_size_input.setText("%s" % val)
		self.pitch_size.setValue(int(val) if val else 0)

	def chat_id_change_handler(self, val):
		self.PEER_ID = int(val) if val else 0

	def start_recording_handler(self):
		if self.STARTED:
			self.record_btn.setText('Record')
			self.STARTED = False
			return
		self.STARTED = True
		self.record_btn.setText('Stop')
		if self.PEER_ID < 1000:
			self.PEER_ID = 2000000000 + self.PEER_ID 
		def strt():
			rec('record.mp3', rate=self.PITCH, c_context=self)
			selectFile('record.mp3')
			sendAudioMessage(self.PEER_ID, c_context=self)
		threading.Thread(target=strt).start()
		print self.STARTED


def main(ACCESS_TOKEN):
	app = QApplication([])
	w = VoiceChanger(ACCESS_TOKEN)
	w.show()
	app.exec_()


if __name__ == "__main__":
	try:
		main(json.load(open('VKdata.json'))["access_token"])
	except:
		QTLogin.main()
	