from PyQt5 import QtCore, QtGui, QtWidgets


class SettingsUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 234)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.showHidden = QtWidgets.QCheckBox(self.centralwidget)
        self.showHidden.setGeometry(QtCore.QRect(10, 30, 344, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.showHidden.setFont(font)
        self.showHidden.setObjectName("showHidden")
        self.defendFromDeleting = QtWidgets.QCheckBox(self.centralwidget)
        self.defendFromDeleting.setGeometry(QtCore.QRect(10, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.defendFromDeleting.setFont(font)
        self.defendFromDeleting.setObjectName("defendFromDeleting")
        self.deleteWindowsCount = QtWidgets.QSpinBox(self.centralwidget)
        self.deleteWindowsCount.setEnabled(True)
        self.deleteWindowsCount.setGeometry(QtCore.QRect(10, 70, 41, 31))
        self.deleteWindowsCount.setMinimum(1)
        self.deleteWindowsCount.setMaximum(5)
        self.deleteWindowsCount.setObjectName("deleteWindowsCount")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showHidden.setText(_translate("MainWindow", "Показать/Скрыть скрытые папки"))
        self.defendFromDeleting.setText(_translate("MainWindow", "Защита от удаления"))
        self.label.setText(_translate("MainWindow", "Кол-во подтверждений при удалении"))
