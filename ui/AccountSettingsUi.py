from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize


class AccountSettingsUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(411, 476))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(160, 10, 80, 80))
        self.image.setText("")
        self.image.setObjectName("image")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login = QtWidgets.QLabel(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(90, 120, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.changeLoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeLoginButton.setGeometry(QtCore.QRect(10, 150, 161, 23))
        self.changeLoginButton.setObjectName("changeLoginButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(100, 190, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.changePasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePasswordButton.setGeometry(QtCore.QRect(10, 220, 161, 23))
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.showHideButton = QtWidgets.QPushButton(self.centralwidget)
        self.showHideButton.setGeometry(QtCore.QRect(180, 220, 111, 23))
        self.showHideButton.setObjectName("showHideButton")
        self.create_new = QtWidgets.QCheckBox(self.centralwidget)
        self.create_new.setEnabled(False)
        self.create_new.setGeometry(QtCore.QRect(20, 300, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_new.setFont(font)
        self.create_new.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cut_copy_paste = QtWidgets.QCheckBox(self.centralwidget)
        self.cut_copy_paste.setEnabled(False)
        self.cut_copy_paste.setGeometry(QtCore.QRect(20, 330, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cut_copy_paste.setFont(font)
        self.cut_copy_paste.setObjectName("checkBox_2")
        self.rename = QtWidgets.QCheckBox(self.centralwidget)
        self.rename.setEnabled(False)
        self.rename.setGeometry(QtCore.QRect(20, 360, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rename.setFont(font)
        self.rename.setObjectName("checkBox_3")
        self.delete = QtWidgets.QCheckBox(self.centralwidget)
        self.delete.setEnabled(False)
        self.delete.setGeometry(QtCore.QRect(20, 390, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete.setFont(font)
        self.delete.setObjectName("checkBox_4")
        self.editPermissionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.editPermissionsButton.setGeometry(QtCore.QRect(140, 420, 121, 23))
        self.editPermissionsButton.setObjectName("editPermissionsButton")
        self.editPermissionsButton.hide()
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setGeometry(QtCore.QRect(20, 420, 111, 23))
        self.logOutButton.setObjectName("logOutButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аккаунт"))
        self.label.setText(_translate("MainWindow", "Логин:"))
        self.login.setText(_translate("MainWindow", "login"))
        self.changeLoginButton.setText(_translate("MainWindow", "Изменить имя пользователя"))
        self.label_3.setText(_translate("MainWindow", "Пароль:"))
        self.password.setText(_translate("MainWindow", "******"))
        self.changePasswordButton.setText(_translate("MainWindow", "Изменить пароль"))
        self.showHideButton.setText(_translate("MainWindow", "Показать/Скрыть"))
        self.create_new.setText(_translate("MainWindow", "Создавать новые файлы и папки"))
        self.label_5.setText(_translate("MainWindow", "Права пользователя:"))
        self.cut_copy_paste.setText(_translate("MainWindow", "Вырезать, Копировать, Вставлять"))
        self.rename.setText(_translate("MainWindow", "Переименовывать"))
        self.delete.setText(_translate("MainWindow", "Удалять"))
        self.editPermissionsButton.setText(_translate("MainWindow", "Управление правами"))
        self.logOutButton.setText(_translate("MainWindow", "Выйти из аккаунта"))
