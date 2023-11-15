import sqlite3

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from classes.ChangeAccountSettings import ChangeAccountSettings
from ui.EditPermissionsUi import EditPermissionsUi


class EditPermissions(QMainWindow, EditPermissionsUi):
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
        self.findButton.clicked.connect(self.find)
        self.editButton.clicked.connect(self.edit)
        self.deleteButton.clicked.connect(self.delete)

    def find(self):
        """
        Ищет пользователей в базе данных.

        :return: None
        """

        con = sqlite3.connect("users.sqlite")
        cur = con.cursor()
        result = list(cur.execute(f"SELECT login, password FROM Users WHERE login LIKE '{self.find_login.text()}%'"))
        result = list(filter(lambda x: x[0] != 'admin' or x[1] != 'admin', result))
        if result:
            self.statusbar.showMessage(f"Нашлось {len(result)} пользователей с таким логином.")
            self.resultWidget.setColumnCount(2)
            self.resultWidget.setRowCount(len(result))
            for i, v in enumerate(result):
                self.resultWidget.setItem(i, 0, QTableWidgetItem(v[0]))
                self.resultWidget.setItem(i, 1, QTableWidgetItem(v[1]))
        else:
            self.resultWidget.clear()
            self.statusbar.showMessage("Пользователей с таким логином не нашлось.")
        cur.close()
        con.close()

    def edit(self):
        """
        Управляет настройками пользователя.

        :return: None
        """

        login = self.resultWidget.item(self.resultWidget.selectedItems()[0].row(), 0).text()
        password = self.resultWidget.item(self.resultWidget.selectedItems()[0].row(), 1).text()
        user_settings = ChangeAccountSettings(login, password, self, True)
        user_settings.show()
        self.find()

    def delete(self):
        """
        Удаляет выбранного пользователя.

        :return: None
        """

        login = self.resultWidget.item(self.resultWidget.selectedItems()[0].row(), 0).text()
        password = self.resultWidget.item(self.resultWidget.selectedItems()[0].row(), 1).text()
        question_line = f"Вы действительно хотите удалить пользователя с логином {login}?"
        answer = QMessageBox.question(self, 'Внимание', question_line, QMessageBox.Yes, QMessageBox.No)
        if answer == QMessageBox.Yes:
            con = sqlite3.connect("users.sqlite")
            cur = con.cursor()
            cur.execute(f"DELETE FROM Users WHERE login = '{login}' AND password = '{password}'")
            con.commit()
            cur.execute(f"INSERT INTO DeletedUsers(login, password) VALUES({login}, {password})")
            con.commit()
            con.close()
            self.find()
