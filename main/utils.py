# Функции для поиска

def search_post_by_substring(substring, posts):
    """
    Поиск по постам на вхождение подстроки
    :param Подстрока
    :param Список словарей - Посты
    :return Список - Посты с вхождением подстроки.
    """
    post_founded = []
    for post in posts:
        if substring.lower() in post['content'].lower():
            post_founded.append(post)
    return post_founded
