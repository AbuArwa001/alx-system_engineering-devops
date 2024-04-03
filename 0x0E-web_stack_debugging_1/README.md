# 0x0E. Web stack debugging #1

## Description
This project is part of the ALX Software Engineering Foundations curriculum. It involves debugging an Ubuntu container's Nginx installation to ensure it listens on port 80.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted on Ubuntu 20.04 LTS
- All files must end with a new line
- A `README.md` file at the root of the project is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without errors
- Bash scripts must run without error
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose
- Usage of `wget` is not allowed

## Tasks
### 0. Nginx likes port 80
**File**: `0-nginx_likes_port_80`

Debug the issue preventing Nginx from listening on port 80 and write a Bash script to automate the fix.

**Requirements**:
- Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs
- Script must configure the server to the above requirements

### 1. Make it sweet and short
**File**: `1-debugging_made_short`

Optimize the fix from task #0 to be shorter and more efficient.

**Requirements**:
- Bash script must be 5 lines long or less
- Must respect usual Bash script requirements
- Cannot use `;`, `&&`, or `wget`
- Cannot execute the previous script
- Service (init) must say that nginx is not running

## Author
[Khalfan Athman]
