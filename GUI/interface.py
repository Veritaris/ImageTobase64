# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 523)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.selectWidget = QtWidgets.QWidget(self.centralwidget)
        self.selectWidget.setStyleSheet("background-color: rgb(68, 68, 68);")
        self.selectWidget.setObjectName("selectWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.selectWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chooseFileButton = QtWidgets.QPushButton(self.selectWidget)
        self.chooseFileButton.setMinimumSize(QtCore.QSize(140, 40))
        self.chooseFileButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chooseFileButton.setFlat(False)
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.horizontalLayout.addWidget(self.chooseFileButton)
        self.graphicsScene = QtWidgets.QGraphicsScene(self.selectWidget)
        self.graphicsView = QtWidgets.QGraphicsView(self.graphicsScene)
        self.graphicsView.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.gridLayout.addWidget(self.selectWidget, 0, 0, 1, 1)
        self.convertWidget = QtWidgets.QWidget(self.centralwidget)
        self.convertWidget.setStyleSheet("background-color: rgb(68, 68, 68);")
        self.convertWidget.setObjectName("convertWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.convertWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filePathLine = QtWidgets.QLineEdit(self.convertWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathLine.sizePolicy().hasHeightForWidth())
        self.filePathLine.setSizePolicy(sizePolicy)
        self.filePathLine.setMinimumSize(QtCore.QSize(0, 25))
        self.filePathLine.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(58, 58, 58);\n"
"border:1px solid grey")
        self.filePathLine.setAlignment(QtCore.Qt.AlignCenter)
        self.filePathLine.setReadOnly(True)
        self.filePathLine.setObjectName("filePathLine")
        self.verticalLayout.addWidget(self.filePathLine)
        self.convertButtonsLayout = QtWidgets.QHBoxLayout()
        self.convertButtonsLayout.setObjectName("convertButtonsLayout")
        self.convertFileButton = QtWidgets.QPushButton(self.convertWidget)
        self.convertFileButton.setMinimumSize(QtCore.QSize(0, 35))
        self.convertFileButton.setStyleSheet("padding-top:10px;\n"
"padding-bottom:10px;")
        self.convertFileButton.setObjectName("convertFileButton")
        self.convertButtonsLayout.addWidget(self.convertFileButton)
        self.saveConvertedFileButton = QtWidgets.QPushButton(self.convertWidget)
        self.saveConvertedFileButton.setMinimumSize(QtCore.QSize(0, 35))
        self.saveConvertedFileButton.setStyleSheet("padding-top:10px;\n"
"padding-bottom:10px;\n"
"\n"
"margin-left: 6px;\n"
"mergin-right: 6px;")
        self.saveConvertedFileButton.setObjectName("saveConvertedFileButton")
        self.convertButtonsLayout.addWidget(self.saveConvertedFileButton)
        self.verticalLayout.addLayout(self.convertButtonsLayout)
        self.convertedImage = QtWidgets.QTextEdit(self.convertWidget)
        self.convertedImage.setMaximumSize(QtCore.QSize(16777215, 250))
        self.convertedImage.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"border-radius:5px;\n"
"background-color: rgb(58, 58, 58);\n"
"border:1px solid grey")
        self.convertedImage.setReadOnly(True)
        self.convertedImage.setObjectName("convertedImage")
        self.verticalLayout.addWidget(self.convertedImage)
        self.gridLayout.addWidget(self.convertWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseFileButton.setText(_translate("MainWindow", "Choose file"))
        self.convertFileButton.setText(_translate("MainWindow", "Convert image to base64"))
        self.saveConvertedFileButton.setText(_translate("MainWindow", "Save converted image to file"))

