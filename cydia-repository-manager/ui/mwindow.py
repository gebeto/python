# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwindow.ui'
#
# Created: Sun Mar 05 22:07:45 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 10, 311, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.TweakInfo = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.TweakInfo.setContentsMargins(0, 0, 0, 0)
        self.TweakInfo.setObjectName("TweakInfo")
        self.nameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setWordWrap(False)
        self.nameLabel.setObjectName("nameLabel")
        self.TweakInfo.addWidget(self.nameLabel)
        self.fieldsLayout = QtGui.QVBoxLayout()
        self.fieldsLayout.setObjectName("fieldsLayout")
        self.nameLayout = QtGui.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.nameLayout.addWidget(self.label_2)
        self.nameInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.nameLayout.addWidget(self.nameInput)
        self.fieldsLayout.addLayout(self.nameLayout)
        self.versionLayout = QtGui.QHBoxLayout()
        self.versionLayout.setObjectName("versionLayout")
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.versionLayout.addWidget(self.label_5)
        self.versionInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.versionInput.setObjectName("versionInput")
        self.versionLayout.addWidget(self.versionInput)
        self.fieldsLayout.addLayout(self.versionLayout)
        self.packageLayout = QtGui.QHBoxLayout()
        self.packageLayout.setObjectName("packageLayout")
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.packageLayout.addWidget(self.label_3)
        self.packageInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.packageInput.setObjectName("packageInput")
        self.packageLayout.addWidget(self.packageInput)
        self.fieldsLayout.addLayout(self.packageLayout)
        self.sectionLayout = QtGui.QHBoxLayout()
        self.sectionLayout.setObjectName("sectionLayout")
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.sectionLayout.addWidget(self.label_6)
        self.sectionInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.sectionInput.setObjectName("sectionInput")
        self.sectionLayout.addWidget(self.sectionInput)
        self.fieldsLayout.addLayout(self.sectionLayout)
        self.authorLayout = QtGui.QHBoxLayout()
        self.authorLayout.setObjectName("authorLayout")
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.authorLayout.addWidget(self.label_7)
        self.authorInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.authorInput.setObjectName("authorInput")
        self.authorLayout.addWidget(self.authorInput)
        self.fieldsLayout.addLayout(self.authorLayout)
        self.filePathLayout = QtGui.QHBoxLayout()
        self.filePathLayout.setObjectName("filePathLayout")
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.filePathLayout.addWidget(self.label_8)
        self.filePathInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.filePathInput.setObjectName("filePathInput")
        self.filePathLayout.addWidget(self.filePathInput)
        self.fieldsLayout.addLayout(self.filePathLayout)
        self.descriptionTextInput = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.descriptionTextInput.setObjectName("descriptionTextInput")
        self.fieldsLayout.addWidget(self.descriptionTextInput)
        self.TweakInfo.addLayout(self.fieldsLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.saveButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.TweakInfo.addLayout(self.horizontalLayout)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(200, 370, 160, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 261, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.TweaksList = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.TweaksList.setContentsMargins(0, 0, 0, 0)
        self.TweaksList.setObjectName("TweaksList")
        self.packagesListWidget = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.packagesListWidget.setObjectName("packagesListWidget")
        self.TweaksList.addWidget(self.packagesListWidget)
        self.addtweakButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.addtweakButton.setObjectName("addtweakButton")
        self.TweaksList.addWidget(self.addtweakButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Cydia Repo Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Section", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.addtweakButton.setText(QtGui.QApplication.translate("MainWindow", "Add tweak", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))

