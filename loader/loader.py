# Загрузчик постов.
import logging

from flask import Blueprint, render_template, request

from loader.utils import *
from utils import *

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")

logging.basicConfig(filename='log.log', level=logging.INFO)


@loader_blueprint.route("/post")
def page_post_upload():
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_new_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        logging.info('Отсутствует часть данных')
        return 'Отсутствует часть данных'
    logging.info('Добaвляется пост')
    posts_list = get_posts_from_json(POST_PATH)
    try:
        picture_way = f'{UPLOAD_FOLDER}/{picture.filename}'
        post_add = {"pic": picture_way, "content": content}
        save_post_to_json(posts_list, post_add)
        save_picture(picture)
        logging.info('Пост добавлен')
        return render_template('post_uploaded.html', post=post_add)
    except DataJsonError:
        return 'Пост не добавлен, ошибка записи данных.'
