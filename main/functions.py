import json
import os

from typing import List, Dict


def load_posts() -> List[Dict]:
    """
    Загружает посты из файла
    :return: Список словарей с постами
    """
    path = os.path.join("posts.json")

    try:
        with open(path, encoding="UTF-8") as data:
            posts = json.load(data)
    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        print("Файл не найден")
    except json.JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        print("Файл не удается преобразовать")
    return posts


def search_posts(key: str) -> List[Dict]:
    """
    Ищет посты по ключу
    :param key: ключ для поиска
    :return: список подходящих постов
    """
    posts = load_posts()
    tag = key.lower()
    current_posts = []

    for post in posts:
        if post["content"].lower().find(tag) != -1:
            current_posts.append(post)

    return current_posts
