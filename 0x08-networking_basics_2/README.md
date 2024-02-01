# 0x08. Networking basics #1

## Description

This project focuses on networking basics and involves tasks related to configuring network settings on an Ubuntu server. The tasks cover changing the home IP, resolving hostnames, and displaying active IPv4 IPs on the machine.

## Learning Objectives

Upon completion of this project, you should be able to:

- Explain the concepts of localhost, 0.0.0.0, and /etc/hosts
- Display the active network interfaces on your machine
- Configure IP resolution for specific hostnames

## Resources

Read or watch:

- What is localhost
- What is 0.0.0.0
- What is the hosts file
- Netcat examples

Man or help:

- ifconfig
- telnet
- nc
- cut

## Copyright - Plagiarism

You are expected to come up with solutions for the tasks to meet the learning objectives. No content from this project should be published, and any form of plagiarism is strictly forbidden.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- Files should end with a new line
- A README.md file at the root of the project folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.7.0 via apt-get) without any errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Tasks

### 0. Change your home IP

Write a Bash script (`0-change_your_home_IP`) that configures an Ubuntu server to meet the following requirements:

- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8

Example usage:

```bash
$ ping localhost
$ ping facebook.com
$ sudo ./0-change_your_home_IP
$ ping localhost
$ ping facebook.com
