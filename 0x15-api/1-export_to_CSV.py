#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import csv
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
    for key, val in EMPLOYEE.items():
        if key == 'username':
            um = val
            break
    with open(f'{sys.argv[1]}.csv', 'w') as file:
        for i in loded:
            stmt = f'"{i["userId"]}","{um}","{i["completed"]}","{i["title"]}"'
            if i['userId'] == int(sys.argv[1]):
                file.write(stmt)
                file.write('\n')


if __name__ == "__main__":
    run()
