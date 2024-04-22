#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import json
import sys
from urllib import request


def run():
    """Returns information about his/her TODO list progress"""
    url = f'https://jsonplaceholder.typicode.com/users/{int(sys.argv[1])}'
    req = request.Request(url)
    with request.urlopen(req) as response:
        user = response.read().decode('utf-8')
    tasks = f'https://jsonplaceholder.typicode.com/todos/'
    req = request.Request(tasks)
    with request.urlopen(req) as response:
        todos = response.read().decode('utf-8')

    loded = json.loads(todos)
    user_tasks = {}
    EMPLOYEE = json.loads(user)
    for key, val in EMPLOYEE.items():
        if key == 'username':
            umn = val
            break
    list_user_tasks = []
    for task in loded:
        if task['userId'] == int(sys.argv[1]):
            otut ={"task": f"{task['title']}", "completed":f"{task['completed']}", "username":f"{umn}"}
            list_user_tasks.append(otut)        
    user_tasks = {sys.argv[1]: list_user_tasks}
    json_object = json.dumps(user_tasks)
    with open(f"{sys.argv[1]}.json","w") as out:
        out.write(json_object)


if __name__ == "__main__":
    run()
