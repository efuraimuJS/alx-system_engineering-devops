#!/usr/bin/python3
"""Return Employee todo list progress for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    done_tasks = [task for task in todos if task.get("completed")]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(done_tasks), len(todos)
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
