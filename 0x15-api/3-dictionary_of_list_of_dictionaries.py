#!/usr/bin/python3
"""A script to export data in the JSON format for all employees."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                tasks.append({
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                })
        data[str(user_id)] = tasks

    filename = "todo_all_employees.json"

    with open(filename, mode="w") as file:
        json.dump(data, file)
