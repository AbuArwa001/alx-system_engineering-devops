# Project: 0x05 Processes and Signals

## Overview

This project focuses on understanding processes and signals in Linux, with an emphasis on Bash scripting. The tasks involve writing Bash scripts to perform various actions related to processes and signals.

## Project Details

### Learning Objectives

By the end of this project, participants are expected to understand:

- What a PID (Process ID) is.
- What a process is and how to find its PID.
- How to kill a process using signals.
- Basics of signals and the two signals that cannot be ignored.

### Resources

Read or watch:

- Linux PID
- Linux process
- Linux signal
- Process management in Linux

Refer to man or help for:

- ps
- pgrep
- pkill
- kill
- exit
- trap

For further understanding, you can explore [this article](https://en.wikipedia.org/wiki/Signal_(IPC)).

### Tasks

1. **What is my PID**
   - Write a Bash script that displays its own PID.

2. **List your processes**
   - Write a Bash script that displays a list of currently running processes.
   - Requirements:
     - Must show all processes for all users, including those without a TTY.
     - Display in a user-oriented format.
     - Show process hierarchy.

3. **Show your Bash PID**
   - Write a Bash script that displays lines containing the word "bash," allowing you to easily get the PID of your Bash process.
   - Requirements:
     - You cannot use pgrep.
     - The third line of your script must be `# shellcheck disable=SC2009`.

4. **Show your Bash PID made easy**
   - Write a Bash script that displays the PID, along with the process name, of processes whose name contains the word "bash."
   - Requirements:
     - You cannot use ps.

5. **To infinity and beyond**
   - Write a Bash script that displays "To infinity and beyond" indefinitely.
   - Requirements:
     - In between each iteration of the loop, add a `sleep`.

6. **Don't stop me now!**
   - Write a Bash script that stops the "To infinity and beyond" process.

7. **Stop me if you can**
   - Write a Bash script that stops the "To infinity and beyond" process without using `kill` or `killall`.

8. **Highlander**
   - Write a Bash script that displays "To infinity and beyond" indefinitely.
   - Requirements:
     - Display "I am invincible!!!" when receiving a SIGTERM signal.
     - Create a copy of the script to kill the process.

9. **Beheaded process**
   - Write a Bash script that kills the process created in the Highlander task.
