# Главная страница и поиск.
import logging

from flask import Blueprint, render_template, request

from config import POST_PATH
from main.utils import search_post_by_substring
from utils import get_posts_from_json

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

logging.basicConfig(filename='log.log', level=logging.INFO)


@main_blueprint.route("/")
def page_index():
    logging.info('Открытие главной страницы')
    return render_template('index.html')


@main_blueprint.route("/search")
def page_search_posts():
    s = request.args.get('s')
    logging.info('Выполняется поиск.')
    try:
        posts = get_posts_from_json(POST_PATH)
    except DataJsonError:
        return "Не открывается файл постов"
    posts_filtered = search_post_by_substring(s, posts)
    return render_template('post_list.html', s=s, posts=posts_filtered)
