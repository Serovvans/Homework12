import logging

from flask import Blueprint, render_template, request
from main.functions import search_posts


logger_info = logging.getLogger("info")
formatter = logging.Formatter("%(asctime)s : %(message)s")
logger_info.addHandler(logging.FileHandler("info_log.txt"))


main_blueprint = Blueprint(
    "main_blueprint",
    __name__,
    template_folder="templates"
)


@main_blueprint.route("/")
def page_index():
    return render_template("index.html")


@main_blueprint.route("/search/", methods=["GET"])
def page_search():
    key = request.args.get("s")
    if not key:
        return "Ключ не введён"
    logger_info.info(f"Выполнен поиск по ключу {key}")
    posts = search_posts(key)

    return render_template("post_list.html", key=key, posts=posts)
