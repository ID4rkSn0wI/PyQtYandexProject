import sys

from PyQt5.QtWidgets import QApplication

from classes.Explorer import Explorer


def my_excepthook(type, value, tback):
    sys.__excepthook__(type, value, tback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Explorer()
    sys.excepthook = my_excepthook
    ex.show()
    sys.exit(app.exec_())
