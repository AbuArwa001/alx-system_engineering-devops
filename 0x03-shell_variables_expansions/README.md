# 0x03. Shell, init files, variables and expansions
## Learning Objectives

* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

  -  What happens when you type $ ls -l *.txt

### Shell Initialization Files

    What are the /etc/profile file and the /etc/profile.d directory
    What is the ~/.bashrc file

### Variables

    - What is the difference between a local and a global variable
    - What is a reserved variable
    - How to create, update and delete shell variables
    - What are the roles of the following reserved variables: HOME, PATH, PS1
    - What are special parameters
    - What is the special parameter $??

### Expansions

    - What is expansion and how to use them
    - What is the difference between single and double quotes and how to use them properly
    - How to do command substitution with $() and backticks

### Shell Arithmetic

    How to perform arithmetic operations with the shell

### The alias Command

    - How to create an alias
    - How to list aliases
    - How to temporarily disable an alias

### Other help pages

    - How to execute commands from a file in the current shell
    
## **Table of contents**

1. ![**Tasks 0 - <o>**]()
2. ![**Task 1 - Hello you**](#task-1-hello-you)

#### Tasks 0 - <o> ####

* Create a script that creates an alias.

   - Name: ls
   - Value: rm *
~~~
julien@ubuntu:/tmp/0x03$ ls
0-alias  file1  file2
julien@ubuntu:/tmp/0x03$ source ./0-alias 
julien@ubuntu:/tmp/0x03$ ls
julien@ubuntu:/tmp/0x03$ \ls
julien@ubuntu:/tmp/0x03$ 
~~~

#### Task 1 - Hello you ####
* Create a script that prints hello user, where user is the current Linux user.
~~~
julien@ubuntu:/tmp/0x03$ id
uid=1000(julien) gid=1000(julien) groups=1000(julien),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
julien@ubuntu:/tmp/0x03$ ./1-hello_you 
hello julien
julien@ubuntu:/tmp/0x03$ 
~~~

