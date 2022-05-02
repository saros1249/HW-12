# Общие функции.
import json

from exeption import *


def get_posts_from_json(path):
    """
    Функция считывает посты из post.json
    :param Путь к файлу
    :return Список словарей.
    """
    try:
        with open(path, encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return DataJsonError
