import logging

from flask import Blueprint, request, render_template
from loader.functions import is_allowed_file, add_post_to_file, add_pic_to_file

logger_info = logging.getLogger("info")
logger_error = logging.getLogger("errors")
formatter = logging.Formatter("%(asctime)s : %(message)s")

handler_info = logging.FileHandler("info_log.txt")
handler_error = logging.FileHandler("error_log.txt")
handler_info.setFormatter(formatter)
handler_error.setFormatter(formatter)

logger_info.addHandler(handler_info)
logger_error.addHandler(handler_error)

loader_blueprint = Blueprint(
    "loader_blueprint",
    __name__,
    template_folder="templates"
)


@loader_blueprint.route("/post", methods=["GET"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    if not picture:
        logger_error.error("Ошибка загрузки файла")
        return "Ошибка загрузки"
    if not is_allowed_file(picture.filename):
        logger_info.info("Загружен файл неверного формата")
        return "Формат файла не поддерживается"

    path = add_pic_to_file(picture)
    picture_url = f"http://127.0.0.1:5000/uploads/{path}"
    content = request.form.get("content")
    post = {"pic": picture_url, "content": content}
    add_post_to_file(post)
    return render_template("post_uploaded.html", post=post)
