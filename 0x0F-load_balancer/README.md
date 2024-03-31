## 0x0F. Load Balancer
### Background Context
You have been given 2 additional servers:
- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

### Resources
Read or watch:
- Introduction to load-balancing and HAproxy
- HTTP header
- Debian/Ubuntu HAProxy packages

### Requirements
- **General**
  - Allowed editors: vi, vim, emacs
  - All your files will be interpreted on Ubuntu 16.04 LTS
  - All your files should end with a new line
  - A README.md file, at the root of the folder of the project, is mandatory
  - All your Bash script files must be executable
  - Your Bash script must pass Shellcheck (version 0.3.7) without any error
  - The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
  - The second line of all your Bash scripts should be a comment explaining what is the script doing

- **Your servers**
  - Name	Username	IP	State	
  - 312646-web-01	ubuntu	34.204.81.253	running	
  - 312646-web-02	ubuntu	52.87.154.218	running	
  - 312646-lb-01	

### Tasks
1. **Double the number of webservers**
   - **Configure Nginx** so that its HTTP response contains a custom header (on web-01 and web-02)
     - The name of the custom HTTP header must be X-Served-By
     - The value of the custom HTTP header must be the hostname of the server Nginx is running on
   - Write a script (`0-custom_http_response_header`) to configure a brand new Ubuntu machine to the requirements asked in this task

2. **Install your load balancer**
   - Install and configure HAproxy on your lb-01 server
   - Configure HAproxy so that it sends traffic to web-01 and web-02, distributing requests using a roundrobin algorithm
   - Make sure that HAproxy can be managed via an init script
   - Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow the provided tutorial.

### Repo
- **GitHub repository:** alx-system_engineering-devops
- **Directory:** 0x0F-load_balancer
- **Files:** 
  - 0-custom_http_response_header
  - 1-install_load_balancer
