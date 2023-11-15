import sqlite3

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from ui.ChangeLoginUi import ChangeLoginUi


class ChangeLogin(QMainWindow, ChangeLoginUi):
    def __init__(self, logins, login, password, parent=None, grand_parent=None):
        """
        Инициализация класса:
        1) Подключение Ui.
        2) Подключение кнопок к функциям.
        3) Создание классовых переменных

        :param parent: QMainWindow
        """

        super().__init__(parent)
        self.setupUi(self)
        self.logins = logins
        self.parent = parent
        self.user_name = login
        self.password = password
        self.grand_parent = grand_parent
        self.changeButton.clicked.connect(self.change_login)

    def change_login(self):
        """
        Проверяет логин на существование и меняет его.

        :return:
        """

        if self.login.text() in self.logins:
            QMessageBox.critical(self, "Внимание ", 'Такой логин уже существует.', QMessageBox.Ok)
        else:
            self.parent.user_name = self.login.text()
            con = sqlite3.connect("users.sqlite")
            cur = con.cursor()
            cur.execute(f"UPDATE Users SET login = '{self.login.text()}' WHERE login = '{self.user_name}'")
            con.commit()
            cur.close()
            self.parent.update()
