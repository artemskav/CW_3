#from requests import response
from flask import Blueprint, render_template, request, make_response

#from exceptions import DataFileBrokenException
from functions import *
import logging
import pytest
#logging.basicConfig(filename="./basic.log", level=logging.INFO)


main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

@main_blueprint.route("/")
def main_page():
    """ загрузка начальной страницы """
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/users/<poster_name>")
def page_poster(poster_name):
    """ Пост(ы) выбранного постера """
    posts = get_post_by_user(poster_name)
    return render_template("user-feed.html", posts=posts)


@main_blueprint.route("/search/")
def search_page():
    """ Поиск по постах по запросу """
    s = request.values.get("s", None)
    posts = search_for_posts(str(s))
    counter_posts = len(posts)
    return render_template("search.html", s=s, posts=posts, counter_posts=counter_posts)

# @main_blueprint.errorhandler(DataFileBrokenException)
# def error_load_file_crash(e):
#     return "Файл постов поврежден"
