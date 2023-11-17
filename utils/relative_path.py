import os
import sys


def resource_path(relative_path):
    """
    Возвращает путь для работы exe-файла

    :param relative_path: str
    :return: преобразованный путь: str
    """

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    if relative_path.split('.')[-1] == 'png':
        base_path = os.path.join(base_path, 'icons')
    elif relative_path.split('.')[-1] == 'jpg':
        base_path = os.path.join(base_path, 'images')

    return os.path.join(base_path, relative_path)