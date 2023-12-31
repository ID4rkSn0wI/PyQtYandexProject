from PyQt5 import QtCore, QtGui, QtWidgets


class ChangePasswordUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(264, 263)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.confirm_new_password = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_new_password.setGeometry(QtCore.QRect(10, 170, 241, 20))
        self.confirm_new_password.setText("")
        self.confirm_new_password.setMaxLength(32)
        self.confirm_new_password.setObjectName("confirm_new_password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.new_password = QtWidgets.QLineEdit(self.centralwidget)
        self.new_password.setGeometry(QtCore.QRect(10, 110, 241, 20))
        self.new_password.setMaxLength(32)
        self.new_password.setObjectName("new_password")
        self.current_password = QtWidgets.QLineEdit(self.centralwidget)
        self.current_password.setGeometry(QtCore.QRect(10, 50, 241, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_password.sizePolicy().hasHeightForWidth())
        self.current_password.setSizePolicy(sizePolicy)
        self.current_password.setMaxLength(32)
        self.current_password.setObjectName("current_password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(60, 200, 131, 31))
        self.changeButton.setObjectName("changeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сменя пароля"))
        self.label_3.setText(_translate("MainWindow", "Подтвердите новый пароль"))
        self.label.setText(_translate("MainWindow", "Введите текущий пароль"))
        self.label_2.setText(_translate("MainWindow", "Введите новый пароль"))
        self.changeButton.setText(_translate("MainWindow", "Поменять пароль"))
