#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import json
import sys
from urllib import request


def run():
    """Returns information about his/her TODO list progress"""
    url = f'https://jsonplaceholder.typicode.com/users'
    req = request.Request(url)
    with request.urlopen(req) as response:
        users = response.read().decode('utf-8')
    tasks = f'https://jsonplaceholder.typicode.com/todos/'
    req = request.Request(tasks)
    with request.urlopen(req) as response:
        todos = response.read().decode('utf-8')

    loded = json.loads(todos)
    user_tasks = {}
    EMPLOYEES = json.loads(users)
    list_user_tasks = []
    all_users = {}
    for user in EMPLOYEES:
        umn = user['username']
        user_id = user['id']
        list_user_tasks = []
        for task in loded:
            if task['userId'] == user_id:
                otut = {"task": f"{task['title']}",
                        "completed": task['completed'], "username": f"{umn}"}
                list_user_tasks.append(otut)
        all_users.update({user_id: list_user_tasks})
    # user_tasks = {sys.argv[1]: list_user_tasks}
    json_object = json.dumps(all_users)
    with open("todo_all_employees.json", "w") as out:
        out.write(json_object)


if __name__ == "__main__":
    run()
