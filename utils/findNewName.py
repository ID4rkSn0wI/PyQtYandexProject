import os
import re

from PyQt5.QtWidgets import QMessageBox

from utils.checkName import check_name
from utils.parsePathToDir import parse_path_to_dir


def find_new_name(self, new_name, cur_path, extension=None):
    """
    Подбирает название к файлу

    :param self:
    :param new_name:
    :param cur_path:
    :param extension:
    :return: None/новое название файла или папки: str
    """
    number_pattern = r'.+ \(\d+\).*'
    find_number_pattern = r"\(\d+\)"
    if not check_name(new_name + (f'.{extension}' if extension else ''), os.path.isdir(cur_path)):
        QMessageBox.critical(self, "Ошибка ", f"Вы ввели недопустимое название"
                                              f" {'папки' if os.path.isdir(cur_path) else 'файла'}", QMessageBox.Ok)
    if os.path.exists(parse_path_to_dir(cur_path) + f"/{new_name + (f'.{extension}' if extension else '')}"):
        start = 2
        if re.fullmatch(number_pattern, new_name):
            start = int(re.findall(find_number_pattern, new_name)[-1][1:-1])
        new_name = f"{new_name} ({start})"
        while os.path.exists(parse_path_to_dir(cur_path)
                             + f"/{new_name + (f'.{extension}' if extension else '')}"):
            new_name = f"{' '.join(new_name.split(' ')[:-1])} ({start})"
            start += 1
        answer = QMessageBox.question(self, 'Выбранное название уже существует',
                                      f'Вы уверены, что хотите поменять название на '
                                      f'{new_name + (f".{extension}" if extension else "")}',
                                      QMessageBox.Yes, QMessageBox.No)
        if answer == QMessageBox.Yes:
            return new_name + (f".{extension}" if extension else "")
        return None
    return new_name + (f".{extension}" if extension else "")
