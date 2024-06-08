import csv
import json
import os
import itertools
import queue

import requests

to_request = queue.Queue()
after_request = queue.Queue()


class User:
    def __init__(self, email: str) -> None:
        self.email = email

    def get_id(self) -> None:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/")
        for data in response.json():
            if data["email"] == self.email:
                self.id = data["id"]
                break

    def get_posts(self) -> None:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{self.id}/posts").json()
        self.posts = response

    def get_albums(self) -> None:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{self.id}/albums").json()
        self.albums = response

    def get_todos(self) -> None:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{self.id}/todos").json()
        self.todos = response


def get_users_from_file(filename: str) -> None:
    try:
        if not os.path.exists("users"):
            os.mkdir("./users")
        with open(f"{filename}", mode="r", encoding="utf8") as file:
            data = csv.reader(file)
            for d in itertools.chain(*data):
                if d:
                    user = User(email=d)
                    to_request.put(user)
    except FileExistsError:
        raise FileExistsError(f"Проверьте существование файла -> {filename} в корне проекта")
    except FileNotFoundError:
        raise FileNotFoundError(f"Проверьте правильность написания пути до файла  -> {filename}")


def save_user_to_file(user: User) -> None:
    with open(f"users/{user.id}.json", mode="w", encoding="utf8") as file:
        data = {
            "posts": user.posts,
            "albums": user.albums,
            "todos": user.todos
        }
        json.dump(data, file)


def process() -> None:
    try:
        while not to_request.empty():
            user = to_request.get()
            user.get_id()
            if user.__dict__.get("id"):
                user.get_posts()
                user.get_albums()
                user.get_todos()
                save_user_to_file(user)
    except Exception as error:
        print(error)


def main() -> None:
    get_users_from_file("example.csv")
    process()


if __name__ == "__main__":
    main()