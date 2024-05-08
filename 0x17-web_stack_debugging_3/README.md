# 0x17. Web Stack Debugging #3 Project README

## Curriculum: SE Foundations
## Concepts

For this project, students should review the following concepts:

- Web Server
- Web stack debugging

## Background Context

When debugging, logs are not always sufficient. Sometimes the software breaks in unexpected ways, or the logs do not provide enough information. In such cases, it's necessary to delve deeper into the stack. Fortunately, Holberton students are equipped to handle this.

Wordpress is a widely-used platform that powers 26% of the web. It's common for students to encounter Wordpress in their careers, as it often runs on a LAMP stack (Linux, Apache, MySQL, and PHP).

The focus of this debugging project is a Wordpress website running on a LAMP stack.

## Requirements

### General

- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A README.md file at the root of the project folder is mandatory
- Puppet manifests must pass puppet-lint version 2.1.1 without errors
- Puppet manifests must run without error
- The first line of your Puppet manifests must be a comment explaining the manifest's purpose
- Puppet manifest files must end with the `.pp` extension
- Files will be checked with Puppet v3.4

### More Info

#### Install puppet-lint

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```