# 0x13. Firewall
## Project Details

## Background Context
Without a firewall, your servers are exposed to various security threats.

## Resources
- What is a firewall

## More Info
Using `telnet` to check open sockets is an essential skill for debugging network communication between software.

**Warning:** Be cautious with firewall rules. Incorrect settings, especially for SSH (port 22), can lock you out of your server.

## Quiz Questions
Congratulations on completing the quiz!

## Servers
| Name         | Username | IP            | State   |
|--------------|----------|---------------|---------|
| 312646-web-01| ubuntu   | 34.204.81.253 | running |
| 312646-web-02| ubuntu   | 52.87.154.218 | running |
| 312646-lb-01 | ubuntu   | 54.159.28.29  | running |

## Tasks
### 0. Block all incoming traffic but
**Mandatory**

Install and configure UFW on web-01 to block all incoming traffic except for TCP ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).

**Commands Used:**
