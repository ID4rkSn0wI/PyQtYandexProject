import sqlite3

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from ui.ChangePasswordUi import ChangePasswordUi


class ChangePassword(QMainWindow, ChangePasswordUi):
    def __init__(self, login, cur_password, parent=None, grand_parent=None):
        """
        Инициализация класса:
        1) Подключение Ui.
        2) Подключение кнопок к функциям.
        3) Создание классовых переменных

        :param parent: QMainWindow
        """

        super().__init__(parent)
        self.setupUi(self)
        self.cur_password = cur_password
        self.login = login
        self.parent = parent
        self.grand_parent = grand_parent
        self.changeButton.clicked.connect(self.change_password)

    def change_password(self):
        """
        Проверяет пароль и меняет его.

        :return:
        """

        if self.current_password.text() != self.cur_password:
            QMessageBox.critical(self, "Внимание ", 'Вы ввели неверный текущий пароль.', QMessageBox.Ok)
        elif self.new_password.text() != self.confirm_new_password.text():
            QMessageBox.critical(self, "Внимание ", 'Вы ввели другой пароль в подтверждении пароля.', QMessageBox.Ok)
        else:
            self.parent.user_password = self.new_password.text()
            con = sqlite3.connect("users.sqlite")
            cur = con.cursor()
            cur.execute(f"UPDATE Users SET password = '{self.new_password.text()}' WHERE login = '{self.login}'")
            con.commit()
            cur.close()
            self.parent.update()
