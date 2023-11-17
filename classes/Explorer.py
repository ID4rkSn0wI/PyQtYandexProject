import csv
import os
import shutil

from send2trash import send2trash

from PyQt5.QtCore import QObject, QEvent, QDir
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QMenu, QMessageBox, QInputDialog

from classes.Find import Find
from classes.Login import Login
from classes.PathEdit import PathEdit
from classes.Settings import Settings
from classes.AccountSettings import AccountSettings
from ui.ExplorerUi import ExplorerUi
from utils.findNewName import find_new_name
from utils.parsePath import parse_path
from utils.parsePathToDir import parse_path_to_dir
from utils.parseToSend2Trash import parse_to_send2trash
from utils.randomQuestionLine import random_question_line
from utils.relative_path import resource_path
from utils.returnIndexAndPath import return_index_and_path


class Explorer(QMainWindow, ExplorerUi):
    def __init__(self):
        """
        Инициализация класса:
        * Создание классовых переменных
        * Задание моделей QTreeViewам
        * Подключение функций к QActions

        :return None
        """

        super().__init__()
        self.setupUi(self)
        self.changer = False
        self.login = ''
        self.password = ''
        self.where = None
        self.cur_path = ''
        self.back_paths = []
        self.copied_path = None
        self.is_cut = False
        self.more_questions = False
        self.if_show_hidden = False
        self.defend_from_deleting = False
        self.back_paths = []
        self.forward_paths = []
        self.delete_windows_count = 1
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath('')
        self.dirModel.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.dirView.setModel(self.dirModel)
        self.dirView.hideColumn(1)
        self.dirView.hideColumn(2)
        self.dirView.hideColumn(3)
        self.dirView.installEventFilter(self)
        self.fileModel = QFileSystemModel()
        self.fileModel.setRootPath('')
        self.fileView.setModel(self.fileModel)
        self.fileView.setIndentation(0)
        self.fileView.installEventFilter(self)
        self.fileView.expanded.connect(self.expanded)
        self.set_up_actions()
        self.check_save()

    def expanded(self):
        """
        Обрабатывает раскрытие папок

        :return: None
        """

        index = self.fileView.currentIndex()
        path = self.fileModel.filePath(index)
        self.back_paths.append(self.cur_path)
        self.cur_path = parse_path(path)
        self.fileView.collapseAll()
        self.fileView.setRootIndex(index)
        self.moveBackAction.setEnabled(True)
        self.moveUpAction.setEnabled(True)

    def eventFilter(self, obj: QObject, event: QEvent):
        """
        Обработчик событий в dirView и fileView

        :param obj: QObject
        :param event: QEvent
        :return: True/False
        """

        if obj is self.dirView:
            self.where = 1
        elif obj is self.fileView:
            self.where = 2
        if event.type() == QEvent.ContextMenu and obj is self.dirView:
            menu = self.set_up_context_menu()
            cursor = QCursor
            menu.exec_(cursor.pos())
            return True
        elif event.type() == QEvent.ContextMenu and obj is self.fileView:
            menu = self.set_up_context_menu()
            cursor = QCursor
            menu.exec_(cursor.pos())
            return True
        return False

    def set_up_context_menu(self):
        """
        Устанавливает контекстное меню.

        :return: menu: QMenu
        """

        menu = QMenu()
        menu.addAction(self.openAction)
        menu.addAction(self.createNewDirAction)
        menu.addAction(self.createNewFileAction)
        menu.addAction(self.cutAction)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.renameAction)
        menu.addAction(self.deleteAction)
        return menu

    def set_up_actions(self):
        """
        Подключает QActionы к функциям и shorcutам.

        :return: None
        """

        self.openAction.triggered.connect(self.open_function)
        self.cutAction.triggered.connect(self.cut)
        self.copyAction.triggered.connect(self.copy)
        self.pasteAction.triggered.connect(self.paste)
        self.renameAction.triggered.connect(self.rename)
        self.deleteAction.triggered.connect(self.delete)
        self.createNewDirAction.triggered.connect(self.create_new_dir)
        self.createNewFileAction.triggered.connect(self.create_new_file)
        self.moveBackAction.triggered.connect(self.move_back)
        self.moveForwardAction.triggered.connect(self.move_forward)
        self.moveUpAction.triggered.connect(self.move_up)
        self.moveMyComputeAction.triggered.connect(self.move_to_my_computer)
        self.findAction.triggered.connect(self.find)
        self.pathEditAction.triggered.connect(self.edit_path)
        self.settingsAction.triggered.connect(self.settings)
        self.pasteAction.setEnabled(False)
        self.moveUpAction.setEnabled(False)
        self.moveBackAction.setEnabled(False)
        self.moveForwardAction.setEnabled(False)
        self.copyAction.setShortcut("CTRL+C")
        self.cutAction.setShortcut("CTRL+X")
        self.pasteAction.setShortcut("CTRL+V")
        self.deleteAction.setShortcut("DEL")
        self.deleteAction.setShortcut("F2")
        self.createNewDirAction.setShortcut("CTRL+SHIFT+N")
        self.createNewFileAction.setShortcut("CTRL+N")
        self.accountSettingsAction.triggered.connect(self.user_settings)
        self.logInAction.triggered.connect(self.log_in)

    def open_function(self):
        """
        Функция перехода в папку/открытия файла/

        :return: None
        """

        cur_index, cur_path = return_index_and_path(self)
        if os.path.isdir(cur_path):
            self.back_paths.append(self.cur_path)
            self.cur_path = cur_path
            self.fileView.collapseAll()
            self.fileView.setRootIndex(self.fileModel.index(cur_path))
            self.moveBackAction.setEnabled(True)
            if self.cur_path != '':
                self.moveUpAction.setEnabled(True)
        else:
            os.startfile(cur_path)

    def cut(self):
        """
        Функция вырезания файла.

        :return: None
        """

        cur_index, cur_path = return_index_and_path(self)
        self.copied_path = cur_path
        self.is_cut = True
        self.pasteAction.setEnabled(True)

    def copy(self):
        """
        Функция копирования файла.

        :return: None
        """

        cur_index, cur_path = return_index_and_path(self)
        self.copied_path = cur_path
        self.is_cut = False
        self.pasteAction.setEnabled(True)

    def paste(self):
        """
        Функция вставки файла по пути.

        :return: None
        """

        cur_index, cur_path = return_index_and_path(self)
        if parse_path_to_dir(self.copied_path) == cur_path:
            QMessageBox.critical(self, "Ошибка ", "Выбрана та же директория что и при копировании", QMessageBox.Ok)
        else:
            try:
                if os.path.exists(cur_path + f'/{self.copied_path.split("/")[-1]}'):
                    question = (f"Обнаружены {'папки' if os.path.isdir(self.copied_path) else 'файлы'} с одинаковыми"
                                f" названиями. Вы действительно хотите заменить их?")
                    answer = QMessageBox.question(self, '', question, QMessageBox.Yes, QMessageBox.No)
                    if answer == QMessageBox.Yes:
                        send2trash(parse_to_send2trash(cur_path + f'/{self.copied_path.split("/")[-1]}'))
                        self.copy_paste(cur_path)
                else:
                    self.copy_paste(cur_path)
            except PermissionError:
                QMessageBox.critical(self, "Ошибка ", "Недостаточно прав", QMessageBox.Ok)

    def copy_paste(self, to):
        """
        Функция копирование и вставки/вырезания и вставки.

        :param to: str
        :return: None
        """

        shutil.copy2(self.copied_path, to)
        if self.is_cut:
            send2trash(parse_to_send2trash(self.copied_path))
            self.is_cut = False

    def rename(self):
        """
        Функция переименовывания файла или папки.

        :return: None
        """

        cur_index, cur_path = return_index_and_path(self)
        question_line = f"Введите новое название {'папки' if os.path.isdir(cur_path) else 'файла'}"
        new_name, ok_pressed = QInputDialog.getText(self, '', question_line)
        if ok_pressed:
            file_name = cur_path.split('/')[-1]
            extension = file_name.split('.')[-1] if len(file_name.split('.')) >= 2 else ''
            if len(new_name.split('.')) >= 2:
                extension = new_name.split('.')[-1]
                new_name = '.'.join(new_name.split('.')[:-1])
            if new_name == file_name or new_name == '.'.join(file_name.split('.')[:-1]):
                return
            new_name = find_new_name(self, new_name, cur_path, extension=extension)
            if new_name:
                os.rename(cur_path,
                          parse_path_to_dir(cur_path) + f"/{new_name}")

    def create_new_dir(self):
        """
        Функция создания новой папки по пути.

        :return: None
        """

        cur_path = return_index_and_path(self)
        new_name, ok_pressed = QInputDialog.getText(self, '', "Введите название папки")
        if ok_pressed:
            new_name = find_new_name(self, new_name, cur_path)
            if new_name:
                os.mkdir(cur_path + f'/{new_name}')

    def create_new_file(self):
        """
        Функция создания нового файла по пути.

        :return: None
        """

        cur_path = return_index_and_path(self)
        new_name, ok_pressed = QInputDialog.getText(self, '', "Введите название файла с расширением")
        if ok_pressed:
            if len(new_name.split('.')) == 1 or len(new_name.split('.')[-1]) == 0:
                QMessageBox.critical(self, "Ошибка ", "Вы не ввели расширение", QMessageBox.Ok)
            else:
                new_name = find_new_name(self, '.'.join(new_name.split('.')[:-1]),
                                         cur_path, extension=new_name.split('.')[-1])
                if new_name:
                    open(cur_path + f"/{new_name}", 'w')

    def delete(self):
        """
        Функция удаления папки/файла.

        :return: None
        """

        cur_index, cur_path = return_index_and_path(self)
        cur_path = parse_path(cur_path)
        if cur_path.startswith(parse_path(QDir.currentPath())):
            warning = f'Вы пытаетесь удалить мне что-то из проекта. Я не дам вам повторить мою же ошибку.'
            QMessageBox.critical(self, "Внимание ", warning, QMessageBox.Ok)
        elif self.defend_from_deleting:
            warning = (f'Вам запрещено удалять файлы из-за опции защиты от удаления. Если вы хотите удалить'
                       f' {"папку" if os.path.isdir(cur_path) else "файл"} {self.cur_path.split("/")[-1]}'
                       f' по пути {cur_path}, то отключите опцию защиты от удаления.')
            QMessageBox.critical(self, "Внимание ", warning, QMessageBox.Ok)
        else:
            yes = True
            for _ in range(self.delete_windows_count):
                question_line = random_question_line() + (f"{'папку' if os.path.isdir(cur_path) else 'файл'}"
                                                          f" с названием {cur_path.split('/')[-1]} по пути {cur_path}?")
                answer = QMessageBox.question(self, 'Внимание', question_line, QMessageBox.Yes, QMessageBox.No)
                if answer == QMessageBox.No:
                    yes = False
                    break
            if yes:
                send2trash(parse_to_send2trash(cur_path))

    def move_to_my_computer(self):
        """
        Функция перехода в 'Мой компьютер'.

        :return: None
        """

        my_computer_path = ''
        index = self.fileModel.index(my_computer_path)
        self.cur_path = my_computer_path
        self.fileView.collapseAll()
        self.fileView.setRootIndex(index)

    def move_back(self):
        """
        Функция перехода назад.

        :return: None
        """

        new_path = self.back_paths[-1]
        index = self.fileModel.index(new_path)
        self.forward_paths.append(self.cur_path)
        self.cur_path = new_path
        self.back_paths = self.back_paths[:-1]
        self.fileView.collapseAll()
        self.fileView.setRootIndex(index)
        if len(self.back_paths) == 0:
            self.moveBackAction.setEnabled(False)
        self.moveForwardAction.setEnabled(True)

    def move_forward(self):
        """
        Функция перехода вперёд.

        :return: None
        """

        new_path = self.forward_paths[-1]
        index = self.fileModel.index(new_path)
        self.back_paths.append(self.cur_path)
        self.cur_path = new_path
        self.forward_paths = self.forward_paths[:-1]
        self.fileView.collapseAll()
        self.fileView.setRootIndex(index)
        if len(self.forward_paths) == 0:
            self.moveForwardAction.setEnabled(False)
        self.moveBackAction.setEnabled(True)

    def move_up(self):
        """
        Функция перехода наверх.

        :return: None
        """

        cur_path = parse_path_to_dir(self.cur_path)
        if cur_path == '':
            self.moveUpAction.setEnabled(False)
            return
        if self.cur_path.split('/')[-1] == '':
            new_path = ''
        else:
            new_path = '/'.join(cur_path.split('/')[:-1])
        self.cur_path = new_path
        index = self.fileModel.index(new_path)
        if new_path == '':
            self.moveUpAction.setEnabled(False)
        self.fileView.collapseAll()
        self.fileView.setRootIndex(index)

    def show_hidden(self):
        """
        Функция показа скрытых папок и файлов.

        :return: None
        """

        if self.if_show_hidden:
            self.dirModel.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.Hidden)
            self.fileModel.setFilter(QDir.AllDirs | QDir.AllEntries | QDir.NoDotAndDotDot | QDir.Hidden)
        else:
            self.dirModel.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
            self.fileModel.setFilter(QDir.AllDirs | QDir.AllEntries | QDir.NoDotAndDotDot)

    def settings(self):
        """
        Функция открытия настроек.

        :return: None
        """

        settings = Settings(self)
        settings.show()

    def find(self):
        """
        Функция открытия поиска файлов и папок.

        :return: None
        """

        find = Find(self)
        find.show()

    def edit_path(self):
        """
        Функция открытия редактора пути.

        :return: None
        """

        edit_path = PathEdit(self)
        edit_path.show()

    def log_out(self):
        """
        Выходит из аккаунта.

        :return: None
        """

        with open(resource_path('saved_account.csv'), 'w', encoding='utf-8') as file:
            pass
        self.set_up_settings()

    def user_settings(self):
        """
        Открывает настройки пользователя.

        :return: None
        """
        if self.login and self.password:
            user_settings_instance = AccountSettings(self.login, self.password, self)
            user_settings_instance.show()

    def log_in(self):
        """
        Входит в аккаунт.

        :return: None
        """

        log_in_instance = Login(self)
        log_in_instance.show()

    def check_save(self):
        """
        Проверяет сохранены ли были данные при входе

        :return: None
        """

        with open(resource_path('saved_account.csv'), 'r', encoding='utf-8') as file:
            reader = list(csv.reader(file, delimiter=';', quotechar='"'))
            if reader:
                self.login = reader[0][0]
                self.password = reader[0][1]
                self.set_up_settings()

    def set_up_settings(self):
        """
        Меняет меню если пользователь сохранил вход, то настройки пользователя, если нет, то вход.

        :return: None
        """

        self.menu_3.clear()
        if self.changer:
            self.menu_3.addAction(self.logInAction)
        else:
            self.menu_3.addAction(self.accountSettingsAction)
        self.menu_3.addAction(self.settingsAction)
        self.changer = not self.changer
