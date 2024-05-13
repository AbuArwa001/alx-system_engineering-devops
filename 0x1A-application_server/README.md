# 0x1A. Application Server

## Concepts

For this project, you should review the following concepts:

- Web Server
- Server
- Web stack debugging

## Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project, you will add this piece to your infrastructure, plug it into your Nginx, and make it serve your Airbnb clone project.

## Resources

**Read or watch:**

- Application server vs web server
- How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
- Running Gunicorn
- Upstart documentation

## Requirements

### General

- A `README.md` file, at the root of the folder of the project, is mandatory.
- Everything Python-related must be done using `python3`.
- All config files must have comments.

### Bash Scripts

- All your files will be interpreted on Ubuntu 16.04 LTS.
- All your files should end with a new line.
- All your Bash script files must be executable.
- Your Bash script must pass Shellcheck without any error.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

## Servers

| Name          | Username | IP            | State   |
|---------------|----------|---------------|---------|
| 312646-web-01 | ubuntu   | 34.204.81.253 | running |
| 312646-web-02 | ubuntu   | 52.87.154.218 | running |
| 312646-lb-01  | ubuntu   | 54.159.28.29  | running |

## Tasks

### 0. Set up development with Python

**Requirements:**

- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
- Install the `net-tools` package on your server: `sudo apt install -y net-tools`
- Git clone your `AirBnB_clone_v2` on your web-01 server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
- Your Flask application object must be named `app`. This will allow us to run and check your code.

**Example:**

Window 1: ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route

Serving Flask app “0-hello_route” (lazy loading)
Environment: production WARNING: Do not use the development server in a production environment. Use a production WSGI server instead.
Debug mode: off
Running on http://0.0.0.0:5000/ (Press CTRL+C to quit) 35.231.193.217 - - [02/May/2019 22:19:42] “GET /airbnb-onepage/ HTTP/1.1” 200 -
Window 2: ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/ Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$


**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x1A-application_server`
- File: `README.md`