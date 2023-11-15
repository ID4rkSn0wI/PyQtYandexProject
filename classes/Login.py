import csv
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from classes.Registration import Registration
from ui.LoginUi import LoginUi


class Login(QMainWindow, LoginUi):
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
        self.loginButton.clicked.connect(self.check_login_and_password)
        self.registrationButton.clicked.connect(self.register)
        self.save_data.stateChanged.connect(self.save)
        self.should_save = False

    def check_login_and_password(self):
        """
        Функция проверки логина и пароля.

        :return: None
        """

        con = sqlite3.connect("users.sqlite")
        cur = con.cursor()
        result = cur.execute(f"SELECT * FROM Users WHERE login = '{self.login.text()}' "
                             f"AND password = '{self.password.text()}'").fetchall()
        deleted_result = list(cur.execute(f"SELECT * FROM DeletedUsers WHERE login = '{self.login.text()}' AND "
                              f"password = '{self.password.text()}'").fetchall())
        if result:
            with open('saved_account.csv', 'w', encoding='utf-8') as file:
                if self.should_save:
                    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([self.login.text(), self.password.text()])
            self.parent.login = self.login.text()
            self.parent.password = self.password.text()
            self.parent.set_up_settings()
            self.parent.user_settings()
            cur.close()
            con.close()
            self.close()
        elif deleted_result:
            warning = f'К сожалению ваш аккаунт был удалён по решению администрации.'
            QMessageBox.critical(self, "Внимание ", warning, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Внимание ", 'Вы ввели неверный логин или пароль.', QMessageBox.Ok)

    def register(self):
        """
        Открывает окно с регистрацией.

        :return: None
        """

        registration = Registration(self)
        registration.show()

    def save(self):
        """
        Сохранять данные или нет.

        :return: None
        """

        self.should_save = not self.should_save
