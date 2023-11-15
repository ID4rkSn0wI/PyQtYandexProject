from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize


class EditPermissionsUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(434, 387))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.resultWidget.setGeometry(QtCore.QRect(10, 60, 411, 301))
        self.resultWidget.setObjectName("resultWidget")
        self.resultWidget.setColumnCount(0)
        self.resultWidget.setRowCount(0)
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.findButton.setObjectName("findButton")
        self.find_login = QtWidgets.QLineEdit(self.centralwidget)
        self.find_login.setGeometry(QtCore.QRect(140, 10, 201, 20))
        self.find_login.setObjectName("find_login")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 6, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(10, 30, 91, 23))
        self.editButton.setObjectName("editButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(110, 30, 75, 23))
        self.deleteButton.setObjectName("deleteButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Управления правами"))
        self.findButton.setText(_translate("MainWindow", "Найти"))
        self.label.setText(_translate("MainWindow", "Поиск по логину"))
        self.editButton.setText(_translate("MainWindow", "Редактировать"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
