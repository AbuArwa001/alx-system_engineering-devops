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


#### Task 2 - The path to success is to take massive, determined action ####

* Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
~~~
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ source ./2-path 
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/action
julien@ubuntu:/tmp/0x03$ 
~~~

#### Task 3 - If the path be beautiful, let us not ask where it leads ####

* Create a script that counts the number of directories in the PATH.
~~~
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ . ./3-paths 
11
julien@ubuntu:/tmp/0x03$ PATH=/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:::::/hello
julien@ubuntu:/tmp/0x03$ . ./3-paths 
12
julien@ubuntu:/tmp/0x03$ 
~~~

#### Task 4 - Global variables ####

* Create a script that lists environment variables.
~~~
julien@ubuntu:/tmp/0x03$ source ./4-global_variables
CC=gcc
CDPATH=.:~:/usr/local:/usr:/
CFLAGS=-O2 -fomit-frame-pointer
COLORTERM=gnome-terminal
CXXFLAGS=-O2 -fomit-frame-pointer
DISPLAY=:0
DOMAIN=hq.garrels.be
e=
TOR=vi
FCEDIT=vi
FIGNORE=.o:~
G_BROKEN_FILENAMES=1
GDK_USE_XFT=1
GDMSESSION=Default
GNOME_DESKTOP_SESSION_ID=Default
GTK_RC_FILES=/etc/gtk/gtkrc:/nethome/franky/.gtkrc-1.2-gnome2
GWMCOLOR=darkgreen
GWMTERM=xterm
HISTFILESIZE=5000
history_control=ignoredups
HISTSIZE=2000
HOME=/nethome/franky
HOSTNAME=octarine.hq.garrels.be
INPUTRC=/etc/inputrc
IRCNAME=franky
JAVA_HOME=/usr/java/j2sdk1.4.0
LANG=en_US
LDFLAGS=-s
LD_LIBRARY_PATH=/usr/lib/mozilla:/usr/lib/mozilla/plugins
LESSCHARSET=latin1
LESS=-edfMQ
LESSOPEN=|/usr/bin/lesspipe.sh %s
LEX=flex
LOCAL_MACHINE=octarine
LOGNAME=franky
[...]
julien@ubuntu:/tmp/0x03$ 
~~~
#### Task 6 - Local variable ####

* Create a script that creates a new local variable.

   - Name: BEST
   - Value: School


#### Task 7 - Global variable ####

* Create a script that creates a new global variable.

  -  Name: BEST
  -  Value: School

#### Task 8 - Every addition to true knowledge is an addition to human power ####

* Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
~~~
julien@production-503e7013:~$ export TRUEKNOWLEDGE=1209
julien@production-503e7013:~$ ./8-true_knowledge | cat -e
1337$
julien@production-503e7013:~$
~~~