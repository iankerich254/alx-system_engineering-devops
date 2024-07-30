#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    all_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [{"username": username, "task": task.get("title"), "completed": task.get("completed")} for task in todos if task.get("userId") == user_id]
        all_data[str(user_id)] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(all_data, file)
