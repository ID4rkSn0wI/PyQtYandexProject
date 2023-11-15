from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize


class RegistrationUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(214, 257))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(10, 50, 191, 20))
        self.login.setText("")
        self.login.setMaxLength(32)
        self.login.setObjectName("login")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(10, 110, 191, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMaxLength(32)
        self.password.setObjectName("password")
        self.confirm_password = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password.setGeometry(QtCore.QRect(10, 170, 191, 20))
        self.confirm_password.setText("")
        self.confirm_password.setMaxLength(32)
        self.confirm_password.setObjectName("confirm_password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.registrationButton = QtWidgets.QPushButton(self.centralwidget)
        self.registrationButton.setGeometry(QtCore.QRect(40, 200, 131, 31))
        self.registrationButton.setObjectName("registrationButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
        self.label.setText(_translate("MainWindow", "Введите логин"))
        self.label_2.setText(_translate("MainWindow", "Введите пароль"))
        self.label_3.setText(_translate("MainWindow", "Подтвердите пароль"))
        self.registrationButton.setText(_translate("MainWindow", "Зарегестрироваться"))
