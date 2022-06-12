from flask import Blueprint, render_template, request, jsonify

#from exceptions import DataFileBrokenException
from functions import *
import logging

#logging.basicConfig(filename="logs/api.log", level=logging.INFO)

post_blueprint = Blueprint('post_blueprint', __name__, template_folder="templates")

@post_blueprint.route("/post/<int:pk>")
def post_page(pk):
    """ загрузка страницы поста по его pk"""
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    count = len(comments)
    return render_template("post.html", post=post, pk=pk, comments=comments, count=count)


@post_blueprint.route("/api/posts")
def full_list_json():
    logging.basicConfig(filename="logs/api.log", format="%(asctime)s [%(levelname)s] : %(message)s", level=logging.INFO)
    data = load_posts()
    return jsonify(data)


@post_blueprint.route("/api/posts/<int:post_id>")
def post_json_by_id(post_id):
    logging.basicConfig(filename="logs/api.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    data = get_post_by_pk(post_id)
    return jsonify(data)
