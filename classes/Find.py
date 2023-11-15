import os
import re

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from ui.FindUi import FindUi
from utils.parsePath import parse_path
from utils.parsePathToDir import parse_path_to_dir


class Find(QMainWindow, FindUi):
    def __init__(self, parent=None):
        """
        Инициализация класса:
        1) Подключение Ui.
        2) Подключение кнопок к функциям.
        3) Установление колонок в таблице.

        :param parent: QMainWindow
        """

        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.findButton.clicked.connect(self.find)
        self.openButton.clicked.connect(self.open)
        self.filesWidget.setColumnCount(2)
        self.filesWidget.setHorizontalHeaderLabels(['Название', 'Путь'])

    def find(self):
        """
        Поиск файла/папки по выбранному пути.

        :return:
        """

        file_name = self.findName.text()
        find_path = self.findPath.text()
        if os.path.exists(find_path):
            self.statusbar.showMessage("")
            result = list(self.find_recursion(file_name, find_path))
            self.filesWidget.setRowCount(len(result))
            for i, path in enumerate(result):
                name = parse_path(path).split('/')[-1]
                self.filesWidget.setItem(i, 0, QTableWidgetItem(name))
                self.filesWidget.setItem(i, 1, QTableWidgetItem(parse_path(path)))
        else:
            self.statusbar.showMessage("Такого пути не существует. Введите снова")

    def find_recursion(self, file_name, folder):
        """
        Поиск файла/папки по выбранному пути.

        :param file_name: str
        :param folder: str
        :return: путь к файлу/папке
        """

        pattern = file_name.lower()
        for element in os.scandir(folder):
            if re.match(pattern, element.name.lower()):
                yield element.path
            else:
                if element.is_dir():
                    yield from self.find_recursion(file_name, element.path)

    def open(self):
        """
        Открывает выбранный путь.

        :return: None
        """

        row = self.filesWidget.selectedItems()[0].row()
        path = self.filesWidget.item(row, 1).text()
        index = self.parent.fileModel.index(parse_path_to_dir(path))
        self.parent.back_paths.append(self.parent.cur_path)
        self.parent.cur_path = path
        self.parent.collapseAll()
        self.parent.fileView.setRootIndex(index)
