#!/usr/bin/python3
"""A script to export data in the CSV format for a given employee ID."""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    username = user.get("username")
    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username, task.get("completed"),
                             task.get("title")])
