# Web Server Project
## Background Context

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements?
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)?

...

## Resources

Read or watch:

- How the web works
- Nginx
- How to Configure Nginx
- Child process concept page
- Root and subdomain
- HTTP requests
- HTTP redirection
- Not found HTTP response code
- Logs files on Linux

For reference:

- RFC 7231 (HTTP/1.1)
- RFC 7540 (HTTP/2)

Man or help:

- scp
- curl

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- General
  - What is the main role of a web server
  - What is a child process
  - Why web servers usually have a parent process and child processes
  - What are the main HTTP requests
- DNS
  - What DNS stands for
  - What is DNS main role
- DNS Record Types
  - A
  - CNAME
  - TXT
  - MX

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You can’t use systemctl for restarting a process

## Quiz questions

Great! You've completed the quiz successfully! Keep going!

## Your servers

| Name          | Username | IP             | State   |
|---------------|----------|----------------|---------|
| 312646-web-01 | ubuntu   | 34.204.81.253  | running |

## Tasks

1. [Transfer a file to your server](./0-transfer_file)
2. [Install nginx web server](./1-install_nginx_web_server)
3. [Setup a domain name](./2-setup_a_domain_name)
4. [Redirection](./3-redirection)
5. [Not found page 404](./4-not_found_page_404)
