import sqlite3

from PyQt5.QtWidgets import QMainWindow

from ui.RegistrationUi import RegistrationUi


class Registration(QMainWindow, RegistrationUi):
    def __init__(self, parent=None):
        """
        Инициализация класса:
        1) Подключение Ui.
        2) Подключение кнопок к функциям.

        :param parent: QMainWindow
        """

        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.registrationButton.clicked.connect(self.check_data)

    def check_data(self):
        """
        Проверяет логин в базе данных, если он существует, то выводит сообщение, если нет, то сохраняет аккаунт в
        базу данных

        :return: None
        """

        if not self.password.text():
            self.statusbar.showMessage("Вы не ввели пароль.")
        elif self.password.text() != self.confirm_password.text():
            self.statusbar.showMessage("У вас введены разные пароли.")
        else:
            con = sqlite3.connect("users.sqlite")
            cur = con.cursor()
            result = cur.execute(f"SELECT * FROM Users WHERE login = '{self.login.text()}'").fetchall()
            con.close()
            if result:
                self.statusbar.showMessage("Такой логин уже существует.")
            else:
                con = sqlite3.connect("users.sqlite")
                cur = con.cursor()
                cur.execute(f"INSERT INTO Users(login, password) VALUES({self.login.text()}, {self.password.text()})")
                con.commit()
                con.close()
                self.parent.login.setText(self.login.text())
                self.parent.password.setText(self.password.text())
                self.close()
