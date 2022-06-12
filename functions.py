import json
import os

from classes_errors import DataFileBrokenException

from pprint import pprint as pp
class Post:
    def __init__(self, poster_name = '', poster_avatar = '',
                 pic = '', content = '', views_count = 0,
                 likes_count = 0, pk = 0):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk


def load_posts():
    """ загрузка и преобразование JSON-файла постов"""
    try:
        with open("data/data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        #        logging.info("Error load of JSON-file")
        raise DataFileBrokenException("Файл с данными постов поврежден")

def load_comments():
    """ загрузка и преобразование JSON-файла комментов"""
    try:
        with open("data/comments.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        #        logging.info("Error load of JSON-file")
        raise DataFileBrokenException("Файл с данными комментариев поврежден")


def get_posts_all():
    return load_posts()

def get_post_by_user(user_name):
    user_name = str(user_name).lower()
    user_posts = []
    posts = load_posts()
    for post in posts:
        if user_name == post["poster_name"]:
            user_posts.append(post)
    if len(user_posts) == 0:
        raise ValueError("Нет такого пользователя")
    return user_posts

def get_comments_by_post_id(post_id):
    comments_by_post_id = []
    comments = load_comments()
    for comment in comments:
        if post_id == comment["post_id"]:
            comments_by_post_id.append(comment)
    if len(comments_by_post_id) == 0:
        raise ValueError("У поста нет комментов")
    return comments_by_post_id

def search_for_posts(query):
    """ Ф-я поиска по ключевому слову"""
    query = str(query).lower()
    post_by_query = []
    posts = load_posts()
    for post in posts:
        if query in post["content"].lower():
            post_by_query.append(post)
    return post_by_query

def get_post_by_pk(pk):
    """ Возвращает пост по его pk """
    if type(pk) != int:
        raise TypeError("pk - не целое число")
    posts = load_posts()
    for post in posts:
        if pk == post["pk"]:
            return post

os.environ['USER'] = 'Артём_К'
print(os.environ.get('USER'))