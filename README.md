# AirBnB Clone Project - Console

## Table of Contents:

1. Project Description
2. Command Interpreter Description
3. How to Start
4. How to Use
5. Examples
6. Author

 1.**Project Description**

This project aims to replicate the functionality of the popular accommodation booking platform Airbnb. On this project we aim to work on the backend using a console application and pythons cmd module.

 2.**Command Interpreter Description**

Command Interpreter is exactly the same as Bash shell, it provides a CLI for executing commands and operations efficiently but limited to a specific use-case. For this Project it is a vital component facilitating administrative tasks related to the management and maintenance of the application. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

 3.**How to Start**

Follow the listed steps in order
```
git clone https://github.com/TriggerJames/AirBnB_clone.git
cd into AirBnB_clone
./console.py - Interactive
echo "<command>" - Non-Interactive
```

 4.**How to Use**

The shell should work in two different ways

**Interactive mode**

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
**Non-Interactive mode: (like the Shell project in C)**

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
6.**Author**

[Kimotho James](https://github.com/TriggerJames)