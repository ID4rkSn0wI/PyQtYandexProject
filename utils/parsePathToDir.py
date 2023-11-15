import os

from utils.parsePath import parse_path


def parse_path_to_dir(path):
    """
    Парсит путь в вид, состоящий только из папок

    :param path:
    :return: Преобразованный путь: str
    """
    path = parse_path(path)
    if not os.path.isdir(path):
        path = '/'.join(path.split('/')[:-1])
    return path
