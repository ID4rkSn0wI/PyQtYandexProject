import random
from copy import copy

QUESTION_LINES = [
    "Вы действительно хотите удалить ",
    "Вы правда желаете удалить ",
    'Вы уверены, что хотите удалить ',
    'Может вы подумаете над тем, чтобы удалять ',
    "Вы действительно считаете нужным удалять ",
    'Вам не кажется странным, что вы пытаетесь удалить ',
    'Вы серьёзно хотите удалить ']

USED_LINES = []


def random_question_line():
    """
    Рандомно выбирает новый вопрос.

    :return: chosen_line: str
    """

    global QUESTION_LINES, USED_LINES
    chosen_line = random.choice(QUESTION_LINES)
    while chosen_line in USED_LINES:
        chosen_line = random.choice(QUESTION_LINES)
    USED_LINES.append(chosen_line)
    return chosen_line


def update():
    """
    Чистит содержимое USED_LINES.

    :return: None
    """

    global USED_LINES
    USED_LINES = []
