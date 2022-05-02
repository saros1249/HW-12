# Функции загрузчика постов

import json

from config import *


def save_post_to_json(posts, post_add):
    """
    Функция добавляет пост и перезаписывает posts.json.
    """
    try:
        posts_list = posts
        posts_list.append(post_add)
        with open(POST_PATH, 'w', encoding='utf-8') as file:
            json.dump(posts_list, file, ensure_ascii=False, indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        return DataJsonError


def save_picture(picture):
    """
    Функция проверяет и сохраняет изображение в папку загрузок.
    """
    allowed_type = ['img', 'png', 'gif', 'jpeg']
    picture_type = picture.filename.split('.')[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f'Неверный формат изображения. Допустимые форматв: {allowed_type}')
    picture_way = f'{UPLOAD_FOLDER}/{picture.filename}'
    picture.save(picture_way)
