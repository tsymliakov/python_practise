"""
Решения заданий по занятиям о JSON
"""


import requests
import json


def save_json_to_file(response):
    """
    Задание 2.6.1. Требуется получить JSON с API и сохранить его в файл.
    """
    with open("response.json", "w") as f:
        json.dump(json.loads(response.text), f, indent=2)


def get_unique_users_count(response):
    """
    Задание 2.6.2. Требуется посчитать количество уникальных пользователей
    """
    unique_users_id = set()

    for record in json.loads(response.text):
        unique_users_id.add(record["userId"])

    return len(unique_users_id)


def get_tasks_status(response):
    """
    Задание 2.6.3. Требуется посчитать для каждого пользователя суммарное число
    задач и количество выполненных задач
    """
    data = json.loads(response.text)
    users = dict()

    for record in data:
        if not users.get(record["userId"]):
            users[record["userId"]] = {"num": 0, "completed": 0}

        users[record["userId"]]["num"] += 1
        users[record["userId"]]["completed"] += int(record["completed"])

    return users


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    save_json_to_file(response)

    unique_users_count = get_unique_users_count(response)

    print(f"Количество уникальных пользователей: {unique_users_count}")

    tasks_status = get_tasks_status(response)

    print(f"Общее количество задач пользователей и число выполненных:\n{json.dumps(tasks_status, indent=2)}")
