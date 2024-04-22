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
    no_d_tsks = sum(1 for i in loded if i['completed']
                               and i['userId'] == int(sys.argv[1]))
    ttl_tsk = sum(1 for i in loded
                               if i['userId'] == int(sys.argv[1]))
    for key, val in EMPLOYEE.items():
        if key == 'name':
            emn = val
            break
    output = "Employee {} is done with tasks({}/{}):".format(emn, no_d_tsks, ttl_tsk)
    print(output)
    for i in loded:
        if i['completed'] and i['userId'] == int(sys.argv[1]):
            print(f"\t {i['title']}")


if __name__ == "__main__":
    run()
