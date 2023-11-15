import os

from PyQt5.QtWidgets import QMainWindow

from ui.PathEditUi import PathEditUi


class PathEdit(QMainWindow, PathEditUi):
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
        self.moveButton.clicked.connect(self.move_to_path)

    def move_to_path(self):
        """
        Открывает выбранный путь.

        :return: None
        """

        path = self.path.text()
        if os.path.exists(path):
            index = self.parent.fileModel.index(path)
            self.parent.back_paths.append(self.parent.cur_path)
            self.parent.fileView.collapseAll()
            self.parent.fileView.setRootIndex(index)
            self.parent.cur_path = path
        else:
            self.statusbar.showMessage("Вы ввели недействительный путь. Попробуйте снова")
