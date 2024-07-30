#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
