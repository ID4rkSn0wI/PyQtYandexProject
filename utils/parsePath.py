import re


def parse_path(path):
    """
    Парсит путь в общий вид

    :param path:
    :return: Преобразованный путь: str
    """
    parsed_path = re.split(r"[/\\]{1,2}", path)
    return '/'.join(parsed_path)
