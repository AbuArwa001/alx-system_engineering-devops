# 0x15. API

## Background Context

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources
Read or watch:

- [Friends don’t let friends program in shell script](https://blog.danslimmon.com/2019/07/15/friends-dont-let-friends-program-in-shell-script/)
- [What is an API](https://www.webopedia.com/TERM/A/API.html)
- [What is an API? In English, please](https://medium.com/@perrysetgo/what-exactly-is-an-api-69f36968a41f)
- [What is a REST API](https://www.restapitutorial.com/lessons/whatisrest.html)
- [What are microservices](https://microservices.io/)
- [PEP8 Python style](https://www.python.org/dev/peps/pep-0008/) - having a clean code respecting style guide is really appreciated in the industry

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use `get` to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Tasks
### 0. Gather data from an API (mandatory)
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list progress in this exact format:


### 1. Export to CSV (mandatory)
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv

### 2. Export to JSON (mandatory)
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

- Records all tasks that are owned by this employee
- Format must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
- File name must be: USER_ID.json
