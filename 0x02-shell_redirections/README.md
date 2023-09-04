# 0x02. Shell, I/O Redirections and filters
  * By using some special notations we can redirect the output of many commands to files, devices, and even to the input of other commands.

## Standard Output

  * Most command line programs that display their results do so by sending their results to a facility called standard output. By default, standard

### Table of Content
1. ![**Task 0 - Hello World**](#task-0---Hello-World)
2. ![**Task 1 - Confused smiley**](#task-1---Confused-smiley)
3. ![**Task 2 - Let's display a file**](#Task-2---Let's-display-a-file)
4. ![**Task 3 - What about 2?**](#task-3-What-about-2)
5. ![**Task 4 - Last lines of a file**](#task-4-Last-lines-of-a-file)
6. ![**Task 5 - I'd prefer the first ones actually**](#task-5-I'd-prefer-the-first-ones-actually)
#### Task 0 - Hello World ####

* Write a script that prints “Hello, World”, followed by a new line to the standard output.
~~~
julien@ubuntu:/tmp/h$ ./0-hello_world 
Hello, World
julien@ubuntu:/tmp/h$ ./0-hello_world | cat -e
Hello, World$
julien@ubuntu:/tmp/h$
~~~


#### Task 1 - Confused smiley ####

* Write a script that displays a confused smiley \"(Ôo)'.
~~~
julien@ubuntu:/tmp/h$ ./1-confused_smiley 
\"(Ôo)'
julien@ubuntu:/tmp/h$ 
~~~

#### Task 2 - Let's display a file ####

* Display the content of the /etc/passwd file.

###### Example: ######
~~~
$ ./2-hellofile
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
_lp:*:26:26:Printing Services:/var/spool/cups:/usr/bin/false
_postfix:*:27:27:Postfix Mail Server:/var/spool/postfix:/usr/bin/false
_scsd:*:31:31:Service Configuration Service:/var/empty:/usr/bin/false
_ces:*:32:32:Certificate Enrollment Service:/var/empty:/usr/bin/false
_mcxalr:*:54:54:MCX AppLaunch:/var/empty:/usr/bin/false
_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false
$
~~~


#### Task 3 -  What about 2? ####

* Display the content of /etc/passwd and /etc/hosts

###### Example: ######
~~~
$ ./3-twofiles
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting. Do not change this entry.
##
127.0.0.1   localhost
255.255.255.255 broadcasthost
::1 localhost
$
~~~


#### 4. Last lines of a file ###

* Display the last 10 lines of /etc/passwd

###### Example: ######
~~~
$ ./4-lastlines
_assetcache:*:235:235:Asset Cache Service:/var/empty:/usr/bin/false
_coremediaiod:*:236:236:Core Media IO Daemon:/var/empty:/usr/bin/false
_launchservicesd:*:239:239:_launchservicesd:/var/empty:/usr/bin/false
_iconservices:*:240:240:IconServices:/var/empty:/usr/bin/false
_distnote:*:241:241:DistNote:/var/empty:/usr/bin/false
_nsurlsessiond:*:242:242:NSURLSession Daemon:/var/db/nsurlsessiond:/usr/bin/false
_nsurlstoraged:*:243:243:NSURLStorage Daemon:/var/empty:/usr/bin/false
_displaypolicyd:*:244:244:Display Policy Daemon:/var/empty:/usr/bin/false
_astris:*:245:245:Astris Services:/var/db/astris:/usr/bin/false
_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false

Tips: “Thinks of it as a cat, what is at the end of it?”
~~~

#### Task 5 - I'd prefer the first ones actually ####

* Display the first 10 lines of /etc/passwd

###### Example: ######
~~~
$ ./5-firstlines
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
$
~~~