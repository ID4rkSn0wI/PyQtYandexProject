import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from classes.ChangeLogin import ChangeLogin
from classes.ChangePassword import ChangePassword
from classes.EditPermissions import EditPermissions
from ui.AccountSettingsUi import AccountSettingsUi


class AccountSettings(QMainWindow, AccountSettingsUi):
    def __init__(self, user_name, user_password, parent=None, edit=False):
        """
        Инициализация класса:
        1) Подключение Ui.
        2) Подключение кнопок к функциям.

        :param parent: QMainWindow
        """

        super().__init__(parent)
        self.setupUi(self)
        self.user_name = user_name
        self.user_password = user_password
        self.parent = parent
        self.is_shown = False
        self.update()
        self.changeLoginButton.clicked.connect(self.change_login)
        self.changePasswordButton.clicked.connect(self.change_password)
        self.showHideButton.clicked.connect(self.show_hide_password)
        self.logOutButton.clicked.connect(self.log_out)
        if user_name == 'admin' and user_password == 'admin':
            self.image.setPixmap(QPixmap("images/admin.jpg").scaled(80, 80, Qt.KeepAspectRatio))
            self.editPermissionsButton.show()
            self.editPermissionsButton.clicked.connect(self.edit_permissions)
        else:
            self.image.setPixmap(QPixmap("images/user.jpg").scaled(80, 80, Qt.KeepAspectRatio))
        if edit:
            self.create_new.setEnabled(True)
            self.cut_copy_paste.setEnabled(True)
            self.rename.setEnabled(True)
            self.delete.setEnabled(True)

    def update(self):
        """
        Обновляет данные.

        :return: None
        """

        con = sqlite3.connect("users.sqlite")
        cur = con.cursor()
        result = list(cur.execute(f"SELECT * FROM Users WHERE login = '{self.user_name}' AND "
                                  f"password = '{self.user_password}'"))[0][3:]
        cur.close()
        self.login.setText(self.user_name)
        self.password.setText(self.user_password if self.is_shown else '*' * len(self.user_password))
        self.create_new.setChecked(result[0])
        self.cut_copy_paste.setChecked(result[1])
        self.rename.setChecked(result[2])
        self.delete.setChecked(result[3])

    def changed_combobox(self):
        """
        Обновляет данные о правах пользователя в базе данных.

        :return: None
        """

        con = sqlite3.connect("users.sqlite")
        cur = con.cursor()
        cur.execute(f"UPDATE Users SET create = {1 if self.create_new.isChecked() else 0} AND "
                    f"cut_copy_paste = {1 if self.cut_copy_paste.isChecked() else 0} AND "
                    f"rename = {1 if self.rename.isChecked() else 0} AND delete = {1 if self.delete.isChecked() else 0}"
                    f" WHERE login = '{self.login.text()}'")
        con.commit()
        cur.close()

    def change_login(self):
        """
        Меняет логин.

        :return: None
        """

        con = sqlite3.connect("users.sqlite")
        cur = con.cursor()
        result = list(map(lambda x: x[0], cur.execute(f"SELECT login FROM Users")))
        cur.close()
        change_login_instance = ChangeLogin(result, self.user_name, self.user_password, self, self.parent)
        change_login_instance.show()

    def change_password(self):
        """
        Меняет пароль.

        :return: None
        """

        change_password_instance = ChangePassword(self.user_name, self.user_password, self, self.parent)
        change_password_instance.show()

    def show_hide_password(self):
        """
        Показывает/Скрывает пароль

        :return: None
        """

        self.is_shown = False if self.is_shown else True
        self.update()

    def log_out(self):
        """
        Выходит из аккаунта

        :return: None
        """

        self.parent.log_out()
        self.close()

    def edit_permissions(self):
        """
        Управление правами пользователей админом.

        :return: None
        """

        edit_permissions_instance = EditPermissions(self)
        edit_permissions_instance.show()
