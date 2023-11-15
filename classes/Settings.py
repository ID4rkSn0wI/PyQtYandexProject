from PyQt5.QtWidgets import QMainWindow

from ui.SettingsUi import SettingsUi


class Settings(QMainWindow, SettingsUi):
    def __init__(self, parent=None):
        """
        Инициализация

        :param parent:
        :return None
        """
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.showHidden.stateChanged.connect(self.show_hidden)
        self.deleteWindowsCount.valueChanged.connect(self.set_delete_windows_count)
        self.defendFromDeleting.stateChanged.connect(self.defend_from_deleting)

    def show_hidden(self):
        """
        Показывает/Скрывает скрытые папки.

        :return: None
        """

        self.parent.if_show_hidden = False if self.parent.if_show_hidden else True
        self.parent.show_hidden()

    def set_delete_windows_count(self):
        """
        Устанавливает кол-во всплывающих окон с подтверждением действия при удалении.

        :return: None
        """

        number = self.deleteWindowsCount.value()
        self.parent.delete_windows_count = number

    def defend_from_deleting(self):
        """
        Устанавливает/Убирает защиту от удаления

        :return: None
        """

        self.parent.defend_from_deleting = False if self.parent.defend_from_deleting else True
