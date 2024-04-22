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
    EMPLOYEE = json.loads(user)
    NUMBER_OF_DONE_TASKS = sum(1 for i in loded if i['completed']
                               and i['userId'] == int(sys.argv[1]))
    TOTAL_NUMBER_OF_TASK = sum(1 for i in loded
                               if i['userId'] == int(sys.argv[1]))
    for key, val in EMPLOYEE.items():
        if key == 'name':
            EMPLOYEE_NAME = val
            break
    print(f'Employee {EMPLOYEE_NAME} is done with\
tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASK}):')
    for i in loded:
        if i['completed'] and i['userId'] == int(sys.argv[1]):
            print(f"\t {i['title']}")


if __name__ == "__main__":
    run()
