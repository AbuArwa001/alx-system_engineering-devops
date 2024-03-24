# 0x0B. SSH

This project is part of the ALX Software Engineering curriculum under the "SE Foundations" track. It focuses on SSH (Secure Shell), a crucial tool for managing networks, servers, and DevOps tasks securely over an unsecured network.

## Background Context

For this project, you've been given access to an Ubuntu server hosted in a distant datacenter. Similar to an earlier application process level, you'll connect using SSH. However, instead of using a password, you'll utilize an RSA key for authentication. Your server has been configured with the public key you created in a previous project, which can be found on your intranet profile.

Your server information is available in the "my servers" section of the intranet. It includes the IP and the username required for SSH connections.

**Note:** The server runs on Ubuntu 20.04 LTS.

## Resources

**Read or watch:**

- What is a (physical) server? ([Text](https://en.wikipedia.org/wiki/Server_(computing)) | [Video](https://www.youtube.com/watch?v=B1ANfsDyjeA))
- [SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [SSH Config File](https://www.ssh.com/ssh/config/)
- [Public Key Authentication for SSH](https://www.ssh.com/ssh/public-key-authentication)
- [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
- [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc) (Long but highly informative)

**For reference:**

- Understanding the SSH Encryption and Connection Process
- [Secure Shell Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
- [IETF RFC 4251](https://tools.ietf.org/html/rfc4251) (Description of the SSH Protocol)

**Man or help:**

- `ssh`
- `ssh-keygen`
- `env`

## Learning Objectives

After completing this project, you should be able to explain:

- What is a server and where servers usually live.
- The purpose and secure use of SSH.
- How to create an SSH RSA key pair.
- How to connect to a remote host using an SSH RSA key pair.
- The advantage of using `#!/usr/bin/env bash` over `/bin/bash`.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`.
- All your files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- All your Bash script files must be executable.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

## Tasks

### 0. Use a private key

Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

**Requirements:**

- Only use `ssh` single-character flags.
- You cannot use `-l`.
- You do not need to handle the case of a private key protected by a passphrase.

**Example:**

```bash
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
``
## Tasks

### 0. Use a Private Key

Create a script to connect to your server using SSH with a specified private key.

- **File:** `0-use_a_private_key`

### 1. Create an SSH Key Pair

Craft a Bash script that generates an RSA key pair.

- **Requirements:**
  - Private key named `school`.
  - Key strength set to 4096 bits.
  - Key protected by the passphrase `betty`.

- **File:** `1-create_ssh_key_pair`

### 2. Client Configuration File

Modify the local SSH client configuration to meet specific requirements.

- **Requirements:**
  - Configure to use the private key `~/.ssh/school`.
  - Refuse password authentication.

- **File:** `2-ssh_config`

### 3. Let Me In!

Add a provided SSH public key to your server to allow connections from the `ubuntu` user.

## Files

- `0-use_a_private_key`: Script to connect using a private key.
- `1-create_ssh_key_pair`: Script to create an RSA key pair.
- `2-ssh_config`: SSH client configuration file.
- `README.md`: Project documentation.

## Author

[Khalfan Athman]

## Acknowledgments

- ALX-SE School for the project guidelines.
- The open-source community for the invaluable resources.