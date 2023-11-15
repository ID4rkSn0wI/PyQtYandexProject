import re


def parse_to_send2trash(path):
    """
    Переводит путь в вид для работы с send2trash

    :param path: str
    :return: new_path: str
    """
    new_path = re.split(r"[/\\]{1,2}", path)
    new_path = '\\'.join(new_path)
    return new_path
