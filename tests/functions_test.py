import pytest
from functions import *
from app import app

        # """ Проверки функций """
def test_get_posts_all():   # выводит список постов
    assert type(get_posts_all()) == list, "На выходе не список"


def test_get_posts_by_pk(): # выводит словарь
    assert type(get_post_by_pk(5)) == dict, "На выходе не словарь"


def test_get_comments_by_post_id(): #  вывод ошибки ValueError
    with pytest.raises(ValueError):
        get_comments_by_post_id(10)


def test_get_post_by_user():    #   вывод ошибки ValueError
    with pytest.raises(ValueError):
        get_post_by_user("carl")


def test_search_for_posts():    # поиск по ключевому слову "утром"
    assert len(search_for_posts("утром")) == 2, "утром имеет 2 результата поиска"


def test_app(): # ошибка 404
    response = app.test_client().get('/meow')
    assert response.status_code == 404


def test_api_posts():   # проверка ендпоинта
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list, "Не список"


def test_api_post_by_pk():  # проверка ендпоинта
    response = app.test_client().get('/api/posts/3')
    assert type(response.json) == dict, "Не словарь"


def must_fields(post):  # ф-я проверки наличия полей
    fields = ['poster_name', 'poster_avatar', 'pic',
              'content', 'views_count', 'likes_count', 'pk']
    for field in fields:
        assert field in post.keys(), f"Нет поля \"{field}\""

def test_api_fields_posts():    # во всех постах
    posts = get_posts_all()
    for post in posts:
        must_fields(post)

def test_api_fields_post_by_pk():   # в одном посте по рк
    post = get_post_by_pk(5)
    must_fields(post)
