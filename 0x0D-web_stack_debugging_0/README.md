# 0x0D. Web Stack Debugging #0

### Background Context

The Webstack debugging series is designed to train you in the fine art of debugging. The unpredictable nature of computers and software requires a strong ability to diagnose and resolve issues efficiently.

Mastering web stack debugging is essential for Full-Stack Software Engineers, demanding practice to excel. This series presents broken or bugged web stacks for you to fix, ultimately aiming to craft a Bash script that rectifies the web stack's state. Initially, however, you'll engage in manual fixes to understand the underlying problems.

### Scenario

Your task is to prepare a server according to the following requirements:

- Must have a copy of the `/etc/passwd` file in `/tmp`
- Must contain a file named `/tmp/isworking` with the string "OK"

These conditions simulate prerequisites for a web application's functionality.

#### Example Workflow

```bash
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
# Docker pulls the image and runs the container
vagrant@vagrant:~$ docker ps
# Lists running containers, showing the new one is up
vagrant@vagrant:~$ docker exec -ti <container_id> /bin/bash
# Accesses the container's bash shell
root@<container_id>:/# cp /etc/passwd /tmp/
root@<container_id>:/# echo OK > /tmp/isworking
# Creates the necessary files within the container
Tasks
0. Give me a page!
Objective: Get Apache to run on the container and return a page containing "Hello Holberton" when querying the root.

Example:

bash
Copy code
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
# Runs the Docker container
vagrant@vagrant:~$ curl 0:8080
# Expected to return "Hello Holberton"
Initially, you may receive an error, but after debugging, the correct page content should be displayed.

Repository:

GitHub: alx-system_engineering-devops
Directory: 0x0D-web_stack_debugging_0
File: 0-give_me_a_page