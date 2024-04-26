# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


# Front основная форма.
class UI_SendMessagePage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 250)
        Form.setMinimumSize(QtCore.QSize(600, 250))
        Form.setMaximumSize(QtCore.QSize(600, 250))

        Form.setWindowIcon(QtGui.QIcon('ui/ico_main/tele.png'))

        font = QtGui.QFont()
        font.setPointSize(10)

        Form.setFont(font)

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")

        self.lowWidget = QtWidgets.QWidget(Form)
        self.lowWidget.setMinimumSize(QtCore.QSize(582, 50))
        self.lowWidget.setMaximumSize(QtCore.QSize(582, 50))
        self.lowWidget.setObjectName("lowWidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.lowWidget)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.textEditName = QtWidgets.QTextEdit(self.lowWidget)
        self.textEditName.setMinimumSize(QtCore.QSize(200, 25))
        self.textEditName.setMaximumSize(QtCore.QSize(170, 22))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.textEditName.setFont(font)
        self.textEditName.setWhatsThis("")
        self.textEditName.setAccessibleName("")
        self.textEditName.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.textEditName.setDocumentTitle("")
        self.textEditName.setObjectName("textEditName")

        self.gridLayout_2.addWidget(self.textEditName, 1, 3, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)

        self.toolButton = QtWidgets.QToolButton(self.lowWidget)
        self.toolButton.setMinimumSize(QtCore.QSize(150, 24))
        self.toolButton.setMaximumSize(QtCore.QSize(150, 24))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.toolButton.setFont(font)
        self.toolButton.setCheckable(True)
        self.toolButton.setObjectName("toolButton")

        self.gridLayout_2.addWidget(self.toolButton, 1, 0, 1, 1)

        self.pushButtonSend = QtWidgets.QPushButton(self.lowWidget)
        self.pushButtonSend.setMinimumSize(QtCore.QSize(150, 24))
        self.pushButtonSend.setMaximumSize(QtCore.QSize(150, 24))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.pushButtonSend.setFont(font)
        self.pushButtonSend.setObjectName("pushButtonSend")

        self.gridLayout_2.addWidget(self.pushButtonSend, 1, 6, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(spacerItem1, 1, 5, 1, 1)

        self.gridLayout.addWidget(self.lowWidget, 1, 0, 1, 1)

        self.topWidget = QtWidgets.QWidget(Form)
        self.topWidget.setMinimumSize(QtCore.QSize(582, 190))
        self.topWidget.setMaximumSize(QtCore.QSize(582, 190))
        self.topWidget.setObjectName("topWidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topWidget)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.labelMainInfo = QtWidgets.QLabel(self.topWidget)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.labelMainInfo.setFont(font)
        self.labelMainInfo.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.labelMainInfo.setObjectName("labelMainInfo")

        self.verticalLayout_2.addWidget(self.labelMainInfo)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(spacerItem2)

        self.labelInfo = QtWidgets.QLabel(self.topWidget)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.labelInfo.setFont(font)
        self.labelInfo.setStyleSheet("background-color: rgb(253, 255, 119, 90);")
        self.labelInfo.setObjectName("labelInfo")

        self.verticalLayout_2.addWidget(self.labelInfo)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(spacerItem3)

        self.lineEditToken = QtWidgets.QLineEdit(self.topWidget)
        self.lineEditToken.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEditToken.setMaximumSize(QtCore.QSize(16777215, 25))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.lineEditToken.setFont(font)
        self.lineEditToken.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.lineEditToken.setObjectName("lineEditToken")

        self.verticalLayout_2.addWidget(self.lineEditToken)

        self.checkBox = QtWidgets.QCheckBox(self.topWidget)
        self.checkBox.setObjectName("checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.gridLayout.addWidget(self.topWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Отправка телефонограмм"))

        self.textEditName.setPlaceholderText(_translate("Form", "Введите имя отправителя"))

        self.toolButton.setText(_translate("Form", "Прикрепить архив..."))

        self.pushButtonSend.setText(_translate("Form", "Отправить архив"))

        self.labelMainInfo.setText(_translate("Form", "Отправка архивов телефонограмм"))

        self.labelInfo.setText(_translate("Form", "- Прикрепите архив в формате (.pdf)\n"
                                                  "- Скопируйте и вставьте ключ для отправки в поле\n"
                                                  "- Для отправки введите свое имя и нажмите отправить архив\n"
                                                  " - Поле имя должно содержать только кириллицу!"))

        self.lineEditToken.setPlaceholderText(

            _translate("Form", "Вставьте полученный ключ для корректной отправки сообщения"))

        self.checkBox.setText(_translate("Form", "Запомнить ключ"))


# Окно ошибки
def errorWindow(message, text):
    error = QMessageBox()
    error.setWindowIcon(QIcon('ui/ico_main/tele.png'))
    error.setWindowTitle('Ошибка')
    error.setText(text)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
    error.setDefaultButton(QMessageBox.Ok)
    error.setDetailedText('Details : {0}'.format(message))

    buttonCancel = error.button(QMessageBox.Cancel)

    buttonCancel.setText('Отмена')

    error.exec_()


# Окно ошибки поисковой строки.
def findErrorWindow(message, text):
    findError = QMessageBox()
    findError.setWindowIcon(QIcon('ui/ico_main/tele.png'))
    findError.setWindowTitle('Ошибка')
    findError.setText(text)
    findError.setIcon(QMessageBox.Critical)
    findError.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
    findError.setDefaultButton(QMessageBox.Ok)
    findError.setDetailedText('Details : {0}'.format(message))

    buttonCancel = findError.button(QMessageBox.Cancel)

    buttonCancel.setText('Отмена')

    findError.exec_()


# Окно успешно.
def successWindow(message):
    success = QMessageBox()
    success.setWindowIcon(QIcon('ui/ico_main/tele.png'))
    success.setWindowTitle('Отправка телефонограмм')
    success.setText(message)
    success.setIcon(QMessageBox.Information)
    success.setStandardButtons(QMessageBox.Ok)

    success.exec_()


def pathDialogWindow(message):
    file = QtWidgets.QFileDialog.getOpenFileName(parent=None, caption="{0}".format(message),
                                                 directory="c:\\", filter="Все (*);;pdf (*.pdf *.pdf)",
                                                 initialFilter="pdf (*.pdf *.pdf)")

    return file
