# 0x18. Webstack Monitoring

## Concepts

Students should familiarize themselves with the following concepts for this project:

- Monitoring
- Server

## Background Context

In today's data-driven tech industry, monitoring software systems is crucial. This project focuses on implementing tools to monitor server operations.

Web stack monitoring is categorized into:

- **Application Monitoring**: Ensuring running software behaves as expected.
- **Server Monitoring**: Ensuring servers are not overloaded (CPU, memory, disk, network).

## Resources

Students are encouraged to read or watch:

- What is server monitoring?
- What is application monitoring?
- System monitoring by Google
- Nginx logging and monitoring

## Learning Objectives

By the end of this project, students should be able to explain:

- The necessity of monitoring
- The two main areas of monitoring
- The purpose of access and error logs in a web server like Nginx

## Requirements

### General

- Editors: vi, vim, emacs
- Environment: Ubuntu 16.04 LTS
- All files must end with a new line
- All Bash scripts must be executable and pass Shellcheck without errors
- Bash scripts must start with `#!/usr/bin/env bash` and include a comment explaining their purpose

### Servers

| Name          | Username | IP            | State   |
|---------------|----------|---------------|---------|
| 312646-web-01 | ubuntu   | 34.204.81.253 | running |
| 312646-web-02 | ubuntu   | 52.87.154.218 | running |
| 312646-lb-01  | ubuntu   | 54.159.28.29  | running |

## Tasks

### 0. Sign up for Datadog and install datadog-agent

- Sign up for Datadog (US1 region)
- Install datadog-agent on web-01
- Create an application key
- Add DataDog API and application keys to your Intranet profile
- Ensure web-01 is visible in Datadog as XX-web-01

### 1. Monitor some metrics

- Set up monitors for read and write requests per second

### 2. Create a dashboard

- Create a dashboard with at least 4 widgets
- Save the dashboard_id in `2-setup_datadog`

## Repository

- **GitHub**: alx-system_engineering-devops
- **Directory**: 0x18-webstack_monitoring
- **Files**: Various, including `2-setup_datadog`

---

