# 0x10. HTTPS SSL

## Background Context

In today's digital age, securing website traffic is not just an option; it's a necessity. Unsecured HTTP traffic can be intercepted, monitored, or manipulated by attackers, jeopardizing the integrity and confidentiality of the data exchanged between a user and the website. HTTPS and SSL/TLS protocols transform the web into a safer place, encrypting the data in transit and ensuring that users connect to the authentic site.

## Resources

- [What is HTTPS?](https://www.instantssl.com/http-vs-https)
- [What are the 2 main elements that SSL is providing?](https://www.ssl.com/faqs/what-is-an-ssl-certificate/)
- [HAProxy SSL termination on Ubuntu 16.04](https://serversforhackers.com/c/using-ssl-certificates-with-haproxy)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)

### man or help:
- `awk`
- `dig`

## Learning Objectives

Upon completing this project, you'll be able to explain the following concepts without the need to look them up:

### General
- The two main roles of HTTPS SSL
- The purpose of encrypting traffic
- What SSL termination means

## Requirements

### General
- You may use `vi`, `vim`, or `emacs` as your editor.
- All files will be interpreted on Ubuntu 16.04 LTS.
- All your files should end with a new line.
- A README.md file, at the root of the folder of the project, is mandatory.
- All your Bash script files must be executable.
- Your Bash scripts must pass Shellcheck (version 0.3.7) without any errors.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining the script's purpose.

## Tasks

### 0. World Wide Web

Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Additionally, add other subdomains for convenience, and write a Bash script to display information about these subdomains.

#### Requirements:

- Add the subdomain `www` to point to your `lb-01` IP.
- Add subdomains `lb-01`, `web-01`, and `web-02`, pointing them to their respective IPs.
- The Bash script should accept a domain name as a mandatory argument and a subdomain as an optional one.
- Output should be in the format: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`.
- Use `awk` and at least one Bash function.
- You do not need to handle empty parameters, nonexistent domain names, or subdomains.

### 1. HAproxy SSL Termination

Configure HAproxy to terminate SSL, meaning it will handle encrypted traffic, decrypt it, and forward it to its intended destination.

#### Requirements:

- HAproxy must listen on port TCP 443.
- HAproxy must accept and serve encrypted traffic.
- The server must return the root of your web server upon querying your domain.
- Include your HAproxy configuration file (`/etc/haproxy/haproxy.cfg`).

SSL termination is crucial for securing data in transit, especially for websites handling sensitive information. By completing this project, you'll gain a deeper understanding of how to implement HTTPS and SSL termination, significantly enhancing web security.
