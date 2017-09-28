from PySide.QtCore import *
from PySide.QtGui import *
from ui.main_window import Ui_Form
from ui.mwindow import Ui_MainWindow
from Packages import Packages


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.packages = Packages('./repo/Packages.bz2')

		# Fill
		print len(self.packages)
		for package in sorted(self.packages.packages.keys()):
			self.packagesListWidget.addItem(package)

		# Connect
		self.packagesListWidget.itemClicked.connect(self.updateInfoView)


	def updateInfoView(self, item):
		cur = self.packages[str(item.text())]
		print cur.name
		self.nameLabel.setText(cur.name)



		self.nameInput.clear()
		self.nameInput.insert(cur.package['Name'].decode('utf8'))

		self.versionInput.clear()
		self.versionInput.insert(cur.package['Version'].decode('utf8'))

		self.packageInput.clear()
		self.packageInput.insert(cur.package['Package'].decode('utf8'))

		self.sectionInput.clear()
		self.sectionInput.insert(cur.package['Section'].decode('utf8'))

		self.authorInput.clear()
		self.authorInput.insert(cur.package['Author'].decode('utf8'))

		self.filePathInput.clear()
		self.filePathInput.insert(cur.package['Filename'].decode('utf8'))

		self.descriptionTextInput.clear()
		self.descriptionTextInput.insertPlainText(cur.package['Description'].decode('utf8'))

app = QApplication([])
w = MainWindow()
w.show()
app.exec_()

