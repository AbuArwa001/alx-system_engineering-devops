# 0X14-MYSQL

## Overview
This curriculum covers MySQL installation, setup, and management tasks for system administrators and DevOps engineers. It includes hands-on exercises to reinforce learning objectives.

### Resources
#### Read/Watch:
- [What is a primary-replica cluster](#)
- [MySQL primary replica setup](#)
- [Build a robust database backup strategy](#)

#### Manuals/Help:
- `mysqldump`

### Learning Objectives
By the end of this project, you should be able to explain the following concepts without external assistance:
- **General**
  - The main role of a database
  - Database replica and its purpose
  - Importance of storing database backups in different physical locations
  - Operations required to verify database backup strategy effectiveness

### Copyright & Plagiarism
- Solutions must be created independently to meet learning objectives.
- No content from this project can be published.
- Plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- **Allowed Editors:** vi, vim, emacs
- **Interpretation Environment:** Ubuntu 16.04 LTS
- **Line Ending:** All files should end with a new line
- **Mandatory Files:**
  - README.md
  - All Bash scripts must be executable
  - Bash scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without errors
  - The first line of Bash scripts should be `#!/usr/bin/env bash`
  - The second line of Bash scripts should be a comment explaining the script's purpose
- **Servers:**
  - See server details in the table below

### Tasks
#### 0. Install MySQL
- **Description:** Install MySQL 5.7.x on web-01 and web-02 servers
- **Additional Requirements:** Ensure SSH configuration task #3 for web-01 and web-02 is completed
- **Repository:** alx-system_engineering-devops/0x14-mysql

#### 1. Let us in!
- **Description:** Create MySQL user holberton_user with specific permissions on both web-01 and web-02
- **Additional Requirements:** Ensure SSH configuration task #3 for web-01 and web-02 is completed
- **Repository:** alx-system_engineering-devops/0x14-mysql

#### 2. If only you could see what I've seen with your eyes
- **Description:** Create a database and table on web-01 for replication setup
- **Additional Requirements:** Ensure holberton_user has SELECT permissions
- **Repository:** alx-system_engineering-devops/0x14-mysql

#### 3. Quite an experience to live in fear, isn't it?
- **Description:** Create a new user for replica server on web-01
- **Additional Requirements:** Ensure holberton_user has SELECT privileges on mysql.user table
- **Repository:** alx-system_engineering-devops/0x14-mysql

#### 4. Setup a Primary-Replica infrastructure using MySQL
- **Description:** Setup Primary-Replica infrastructure with MySQL
- **Requirements:**
  - MySQL primary hosted on web-01
  - MySQL replica hosted on web-02
  - Replication setup for the MySQL database named tyrell_corp
- **Repository:** alx-system_engineering-devops/0x14-mysql
- **Files:** 4-mysql_configuration_primary, 4-mysql_configuration_replica

#### 5. MySQL backup
- **Description:** Write a Bash script for MySQL backup
- **Requirements:**
  - MySQL dump containing all databases
  - Dump file compressed to a tar.gz archive with specific name format
  - Script accepting MySQL root user password as argument
- **Repository:** alx-system_engineering-devops/0x14-mysql
- **File:** 5-mysql_backup

### Servers
| Name          | Username | IP            | State   |
|---------------|----------|---------------|---------|
| 312646-web-01 | ubuntu   | 34.204.81.253 | running |
| 312646-web-02 | ubuntu   | 52.87.154.218 | running |
| 312646-lb-01  | ubuntu   | 54.159.28.29  | running |

---

Copyright © 2024 ALX. All rights reserved.
