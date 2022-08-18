import os
import json

from typing import Dict


def add_post_to_file(post: Dict) -> None:
    """
    Добавляет пост в posts.json
    :param post: словарь с постом
    :return:
    """
    path = os.path.join("posts.json")
    try:
        with open(path, "r", encoding="UTF-8") as posts_file:
            all_posts = json.load(posts_file)

        all_posts.append(post)
        with open(path, "w", encoding="UTF-8") as posts_file:
            json.dump(all_posts, posts_file, ensure_ascii=False)
    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        print("Файл не найден")
    except json.JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        print("Файл не удается преобразовать")


def add_pic_to_file(picture) -> str:
    """
    Добавляет картинку в uploads
    :param picture: картинка поста
    :return:
    """
    path = os.path.join("uploads", "images", picture.filename)
    picture.save(path)
    return f"images/{picture.filename}"


def is_allowed_file(filename: str) -> bool:
    """
    Проверяет формат файла
    :param filename: полное название файла
    :return: является ли файл фотографией
    """
    allowed_extension = ["jpg", "png"]
    extension = filename.split(".")[-1]
    return extension in allowed_extension
