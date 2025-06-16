- [Python Tutorial](https://www.geeksforgeeks.org/python-programming-language-tutorial/)
- [Interview Questions](https://www.geeksforgeeks.org/python-interview-questions/)
- [Python Quiz](https://www.geeksforgeeks.org/python-quizzes/)
- [Python Glossary](https://www.geeksforgeeks.org/python-glossary/)
- [Python Projects](https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/)
- [Practice Python](https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/)
- [Data Science With Python](https://www.geeksforgeeks.org/data-science-with-python-tutorial/)
- [Python Web Dev](https://www.geeksforgeeks.org/python-web-development-django/)
- [DSA with Python](https://www.geeksforgeeks.org/python-data-structures-and-algorithms/)
- [Python OOPs](https://www.geeksforgeeks.org/python-oops-concepts/)

Sign In

▲

[Open In App](https://geeksforgeeksapp.page.link/?link=https://www.geeksforgeeks.org/how-to-learn-python-from-scratch/?type%3Darticle%26id%3D1249523&apn=free.programming.programming&isi=1641848816&ibi=org.geeksforgeeks.GeeksforGeeksDev&efr=1)

[Next Article:\\
\\
Python Introduction\\
\\
![Next article icon](https://media.geeksforgeeks.org/auth-dashboard-uploads/ep_right.svg)](https://www.geeksforgeeks.org/introduction-to-python/)

# How to Learn Python from Scratch in 2025

Last Updated : 19 Apr, 2025

Comments

Improve

Suggest changes

13 Likes

Like

Report

Python is a general-purpose high-level programming language and is widely used among the developers’ community. Python was mainly developed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code.

![Learn Python from Scratch](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200623173636/Python-Tutorial1.png)

If you are new to programming and want to learn Python Programming from Scratch, then this complete 2024 Python course guide is here to help you. Whether you are an experienced programmer or new to the programming world, this guide will help you with the knowledge and resources needed to get started with Python Language.

## Key features of Python

[Python](https://www.geeksforgeeks.org/python-programming-language/) has many reasons for being popular and in demand. A few of the reasons are mentioned below.

- Emphasis on **code readability, shorter codes, ease of writing**.
- Programmers can express logical concepts intarted with Pyth **fewer lines of code** in comparison to languages such as C++ or Java.
- Python **supports multiple programming paradigms**, like object-oriented, imperative and functional programming or procedural.
- It provides **extensive support libraries**(Django for web development, Pandas for data analytics etc)
- **Dynamically typed language**(Data type is based on value assigned)
- Philosophy is “Simplicity is the best”.

### Application Areas

![python-applications](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200623173727/python-applications.png)

## Getting started with Python Programming –

Python is a lot easier to code and learn. Python programs can be written on any plain text editor like notepad, notepad++, or anything of that sort. One can also use an online IDE for writing Python codes or can even install one on their system to make it more feasible to write these codes because IDEs provide a lot of features like intuitive code editor, debugger, compiler, etc.

To begin with, writing Python Codes and performing various intriguing and useful operations, one must have Python installed on their System. This can be done by following the step by step instructions provided below:

### What if Python already exists? Let’s check

Windows don’t come with Python preinstalled, it needs to be installed explicitly. But unlike windows, most of the Linux OS have Python pre-installed, also macOS comes with Python pre-installed.

To check if your device is pre-installed with Python or not, just go to **Command Line**(For **Windows**, search for **cmd** in the Run dialog( + **R**), for **Linux** open the terminal using **`Ctrl+Alt+T`**, for **macOS** use

**`control+Option+Shift+T`**.

Now run the following command:

**For Python2**

```
python --version

```

**For Python3**

```
python3 --version

```

If Python is already installed, it will generate a message with the Python version available.

![learn python](https://media.geeksforgeeks.org/wp-content/uploads/20191223181123/python-tutorial-1.png)

### Download and Installation

Before starting with the installation process, you need to download it. For that all versions of Python for Windows, Linux, and MacOS are available on [python.org](https://www.python.org/).

- Windows
- Linux
- MacOS

[![How-to-install-Python-for-windows-11](https://media.geeksforgeeks.org/wp-content/uploads/20191223185006/How-to-install-Python-for-windows-11.png)](https://www.python.org/downloads/windows/)

Download the Python and follow the further instructions for the installation of Python.

**Beginning the installation.**

- Windows
- Linux
- MacOS

- Run the Python Installer from `downloads` folder. Make sure to mark Add Python 3.7 to PATH otherwise you will have to do it explicitly.

It will start installing python on windows.

![python-install-windows-1](https://media.geeksforgeeks.org/wp-content/uploads/20191223185205/python-install-windows-1.png)
- **After installation is complete click on Close.**

**Bingo..!! Python is installed. Now go to windows and type IDLE.**

![python-install-windows-23](https://media.geeksforgeeks.org/wp-content/uploads/20191227104318/python-install-windows-23.png)

### How to run a Python program

Let’s consider a simple Hello World Program.

Python`
# Python program to print
# Hello World

print("Hello World")
`

```
# Python program to print
```

```
# Hello World
```

```

```

```
print("Hello World")
```

**Output**

```
Hello World

```

Generally, there are two ways to run a Python program.

- **Using IDEs:** You can use various IDEs(Pycharm, Jupyter Notebook, etc.) which can be used to run Python programs.
- **Using Command-Line:** You can also use command line options to run a Python program. Below steps demonstrate how to run a Python program on Command line in Windows/Unix Operating System:

### Windows

Open Commandline and then to compile the code type **python HelloWorld.py**. If your code has no error then it will execute properly and output will be displayed.

![python-hellow-world-windows](https://media.geeksforgeeks.org/wp-content/uploads/20191227121240/python-hellow-world-windows.png)

### Unix/Linux

Open Terminal of your Unix/Linux OS and then to compile the code type **python HelloWorld.py**. If your code has no error then it will execute properly and output will be displayed.

![python-linux-hello-world](https://media.geeksforgeeks.org/wp-content/uploads/20191223194209/python-linux-hello-world.png)

## Fundamentals of Python

### Python Indentation

Python uses [indentation](https://www.geeksforgeeks.org/indentation-in-python/) to highlight the blocks of code. Whitespace is used for indentation in Python. All statements with the same distance to the right belong to the same block of code. If a block has to be more deeply nested, it is simply indented further to the right. You can understand it better by looking at the following lines of code.

Python`
# Python program showing
# indentation

site = 'gfg'

if site == 'gfg':
    print('Logging on to geeksforgeeks...')
else:
    print('retype the URL.')
print('All set !')
`

```
# Python program showing
```

```
# indentation
```

```

```

```
site = 'gfg'
```

```

```

```
if site == 'gfg':
```

```
    print('Logging on to geeksforgeeks...')
```

```
else:
```

```
    print('retype the URL.')
```

```
print('All set !')
```

**Output**

```
Logging on to geeksforgeeks...
All set !

```

The lines `print(‘Logging on to geeksforgeeks…’)` and `print(‘retype the URL.’)` are two separate code blocks. The two blocks of code in our example if-statement are both indented four spaces. The final `print(‘All set!’)` is not indented, and so it does not belong to the else-block.

### Python Comments

Comments are useful information that the developers provide to make the reader understand the source code. It explains the logic or a part of it used in the code. There are two types of comment in Python:

**Single line comments:** Python single line comment starts with hashtag symbol with no white spaces.

Python`
# This is a comment
# Print “GeeksforGeeks !” to console
print("GeeksforGeeks")
`

```
# This is a comment
```

```
# Print “GeeksforGeeks !” to console
```

```
print("GeeksforGeeks")
```

**Output**

```
GeeksforGeeks

```

**Multi-line string as comment:** Python multi-line comment is a piece of text enclosed in a delimiter (“””) on each end of the comment.

Python`
"""
This would be a multiline comment in Python that
spans several lines and describes geeksforgeeks.
A Computer Science portal for geeks. It contains
well written, well thought
and well-explained computer science
and programming articles,
quizzes and more.
…
"""
print("GeeksForGeeks")
`

```
"""
```

```
This would be a multiline comment in Python that
```

```
spans several lines and describes geeksforgeeks.
```

```
A Computer Science portal for geeks. It contains
```

```
well written, well thought
```

```
and well-explained computer science
```

```
and programming articles,
```

```
quizzes and more.
```

```
…
```

```
"""
```

```
print("GeeksForGeeks")
```

**Output**

```
GeeksForGeeks

```

**Note:** For more information, refer  [Comments in Python](https://www.geeksforgeeks.org/statement-indentation-and-comment-in-python/).

### Variables

[Variables](https://www.geeksforgeeks.org/python-variables/) in Python are not “statically typed”. We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it.

Python`
#!/usr/bin/python

# An integer assignment
age = 45

# A floating point
salary = 1456.8

# A string
name = "John"

print(age)
print(salary)
print(name)
`

```
#!/usr/bin/python
```

```

```

```
# An integer assignment
```

```
age = 45
```

```

```

```
# A floating point
```

```
salary = 1456.8
```

```

```

```
# A string
```

```
name = "John"
```

```

```

```
print(age)
```

```
print(salary)
```

```
print(name)
```

**Output**

```
45
1456.8
John

```

### Operators

[Operators](https://www.geeksforgeeks.org/basic-operators-python/) are the main building block of any programming language. Operators allow the programmer to perform different kinds of operations on operands. These operators can be categorized based upon their different functionality:

**Arithmetic operators**: Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.

Python`
# Examples of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b
# Subtraction of numbers
sub = a - b
# Multiplication of number
mul = a * b
# Division(float) of number
div1 = a / b
# Division(floor) of number
div2 = a // b
# Modulo of both number
mod = a % b

# print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
`

```
# Examples of Arithmetic Operator
```

```
a = 9
```

```
b = 4
```

```

```

```
# Addition of numbers
```

```
add = a + b
```

```
# Subtraction of numbers
```

```
sub = a - b
```

```
# Multiplication of number
```

```
mul = a * b
```

```
# Division(float) of number
```

```
div1 = a / b
```

```
# Division(floor) of number
```

```
div2 = a // b
```

```
# Modulo of both number
```

```
mod = a % b
```

```

```

```
# print results
```

```
print(add)
```

```
print(sub)
```

```
print(mul)
```

```
print(div1)
```

```
print(div2)
```

```
print(mod)
```

**Output**

```
13
5
36
2.25
2
1

```

**Relational Operators:** Relational operators compares the values. It either returns True or False according to the condition.

Python`
# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)
`

```
# Examples of Relational Operators
```

```
a = 13
```

```
b = 33
```

```

```

```
# a > b is False
```

```
print(a > b)
```

```

```

```
# a < b is True
```

```
print(a < b)
```

```

```

```
# a == b is False
```

```
print(a == b)
```

```

```

```
# a != b is True
```

```
print(a != b)
```

```

```

```
# a >= b is False
```

```
print(a >= b)
```

```

```

```
# a <= b is True
```

```
print(a <= b)
```

**Output**

```
False
True
False
True
False
True

```

[**Logical Operators:**](https://www.geeksforgeeks.org/python-logical-operators-with-examples-improvement-needed/) Logical operators perform Logical AND, Logical OR and Logical NOT operations.

Python`
# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)
`

```
# Examples of Logical Operator
```

```
a = True
```

```
b = False
```

```

```

```
# Print a and b is False
```

```
print(a and b)
```

```

```

```
# Print a or b is True
```

```
print(a or b)
```

```

```

```
# Print not a is False
```

```
print(not a)
```

**Output:**

```
False
True
False
```

[**Bitwise operators:**](https://www.geeksforgeeks.org/python-bitwise-operators/) Bitwise operator acts on bits and performs bit by bit operation.

Python`
# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)
`

```
# Examples of Bitwise operators
```

```
a = 10
```

```
b = 4
```

```

```

```
# Print bitwise AND operation
```

```
print(a & b)
```

```

```

```
# Print bitwise OR operation
```

```
print(a | b)
```

```

```

```
# Print bitwise NOT operation
```

```
print(~a)
```

```

```

```
# print bitwise XOR operation
```

```
print(a ^ b)
```

```

```

```
# print bitwise right shift operation
```

```
print(a >> 2)
```

```

```

```
# print bitwise left shift operation
```

```
print(a << 2)
```

**Output:**

```
0
14
-11
14
2
40
```

**Assignment operators:** Assignment operators are used to assign values to the variables.

**Special operators:** Special operators are of two types-

- Identity operator that contains `is` and `is not`.
- Membership operator that contains `in` and `not in`.

Python`
# Examples of Identity and
# Membership operator


a1 = 'GeeksforGeeks'
b1 = 'GeeksforGeeks'

# Identity operator
print(a1 is not b1)
print(a1 is b1)

# Membership operator
print("G" in a1)
print("N" not in b1)
`

```
# Examples of Identity and
```

```
# Membership operator
```

```

```

```

```

```
a1 = 'GeeksforGeeks'
```

```
b1 = 'GeeksforGeeks'
```

```

```

```
# Identity operator
```

```
print(a1 is not b1)
```

```
print(a1 is b1)
```

```

```

```
# Membership operator
```

```
print("G" in a1)
```

```
print("N" not in b1)
```

**Output:**

```
False
True
True
True
```

## Basics of Input/Output

### Taking input from user –

Python provides us with two inbuilt functions to read the input from the keyboard.

- **raw\_input():** This function works in older version (like Python 2.x). This function takes exactly what is typed from the keyboard, convert it to string and then return it to the variable in which we want to store. For example:

Python`
# Python program showing
# a use of raw_input()

g = raw_input("Enter your name : ")
print g
`

```
# Python program showing
```

```
# a use of raw_input()
```

```

```

```
g = raw_input("Enter your name : ")
```

```
print g
```

- **input():** This function first takes the input from the user and then evaluates the expression, which means Python automatically identifies whether the user entered a string or a number or list. For example:

Python`
# Python program showing
# a use of input()

val = input("Enter your value: ")
print(val)
`

```
# Python program showing
```

```
# a use of input()
```

```

```

```
val = input("Enter your value: ")
```

```
print(val)
```

**Note:** For more information, refer [Python `input()` and `raw_input()`](https://www.geeksforgeeks.org/difference-between-input-and-raw_input-functions-in-python/).

### Printing output to console –

The simplest way to produce output is using the `print()` function where you can pass zero or more expressions separated by commas. This function converts the expressions you pass into a string before writing to the screen.

Python`
# Python 3.x program showing
# how to print data on
# a screen

# One object is passed
print("GeeksForGeeks")

x = 5
# Two objects are passed
print("x =", x)

# code for disabling the softspace feature
print('G', 'F', 'G', sep ='')

# using end argument
print("Python", end = '@')
print("GeeksforGeeks")
`

```
# Python 3.x program showing
```

```
# how to print data on
```

```
# a screen
```

```

```

```
# One object is passed
```

```
print("GeeksForGeeks")
```

```

```

```
x = 5
```

```
# Two objects are passed
```

```
print("x =", x)
```

```

```

```
# code for disabling the softspace feature
```

```
print('G', 'F', 'G', sep ='')
```

```

```

```
# using end argument
```

```
print("Python", end = '@')
```

```
print("GeeksforGeeks")
```

**Output:**

```
GeeksForGeeks
x = 5
GFG
Python@GeeksforGeeks
```

## Data Types

[Data types](https://www.geeksforgeeks.org/python-data-types/) are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

![Python-data-structure](https://media.geeksforgeeks.org/wp-content/uploads/20191224133121/Python-data-structure1.jpg)

### Numeric

In Python, numeric data type represent the data which has numeric value. Numeric value can be interger, floating number or even complex numbers. These values are defined as `int`, `float` and `complex` class in Python.

Python`
# Python program to
# demonstrate numeric value

print("Type of a: ", type(5))

print("\nType of b: ", type(5.0))

c = 2 + 4j
print("\nType of c: ", type(c))
`

```
# Python program to
```

```
# demonstrate numeric value
```

```

```

```
print("Type of a: ", type(5))
```

```

```

```
print("\nType of b: ", type(5.0))
```

```

```

```
c = 2 + 4j
```

```
print("\nType of c: ", type(c))
```

**Output:**

```
Type of a:  <class 'int'>

Type of b:  <class 'float'>

Type of c:  <class 'complex'>
```

### Sequence Type

In Python, a sequence is the ordered collection of similar or different data types. Sequences allow storing multiple values in an organized and efficient fashion. There are several sequence types in Python –

- **String**
- **List**
- **Tuple**

**1) String:** A string is a collection of one or more characters put in a single quote, double-quote or triple quote. In python there is no character data type, a character is a string of length one. It is represented by `str` class. Strings in Python can be created using single quotes or double quotes or even triple quotes.

Python`
# Python Program for
# Creation of String

# String with single quotes
print('Welcome to the Geeks World')

# String with double quotes
print("I'm a Geek")

# String with triple quotes
print('''I'm a Geek and I live in a world of "Geeks"''')
`

```
# Python Program for
```

```
# Creation of String
```

```

```

```
# String with single quotes
```

```
print('Welcome to the Geeks World')
```

```

```

```
# String with double quotes
```

```
print("I'm a Geek")
```

```

```

```
# String with triple quotes
```

```
print('''I'm a Geek and I live in a world of "Geeks"''')
```

**Output:**

```
Welcome to the Geeks World
I'm a Geek
I'm a Geek and I live in a world of "Geeks"

```

**Accessing elements of string –**

![strings](https://media.geeksforgeeks.org/wp-content/uploads/20191224133852/strings11.jpg)

Python`
# Python Program to Access
# characters of String

String1 = "GeeksForGeeks"

# Printing First character
print(String1[0])

# Printing Last character
print(String1[-1])
`

```
# Python Program to Access
```

```
# characters of String
```

```

```

```
String1 = "GeeksForGeeks"
```

```

```

```
# Printing First character
```

```
print(String1[0])
```

```

```

```
# Printing Last character
```

```
print(String1[-1])
```

**Output:**

```
G
s

```

**Deleting/Updating from a String –**

In Python, Updation or deletion of characters from a String is not allowed because Strings are immutable. Only new strings can be reassigned to the same name.

Python`
# Python Program to Update / delete
# character of a String

String1 = "Hello, I'm a Geek"

# Updating a character
String1[2] = 'p'

# Deleting a character
del String1[2]
`

```
# Python Program to Update / delete
```

```
# character of a String
```

```

```

```
String1 = "Hello, I'm a Geek"
```

```

```

```
# Updating a character
```

```
String1[2] = 'p'
```

```

```

```
# Deleting a character
```

```
del String1[2]
```

**Output:**

```
Traceback (most recent call last):
File “/home/360bb1830c83a918fc78aa8979195653.py”, line 6, in
String1[2] = ‘p’
TypeError: ‘str’ object does not support item assignment

Traceback (most recent call last):
File “/home/499e96a61e19944e7e45b7a6e1276742.py”, line 8, in
del String1[2]
TypeError: ‘str’ object doesn’t support item deletion

```

**Note:** For more information, refer  [Python String](https://www.geeksforgeeks.org/python-strings/).

> **Refer to the below articles to know more about Strings:**
>
> - [String Slicing in Python](https://www.geeksforgeeks.org/string-slicing-in-python/)
> - [Python String Concatenation](https://www.geeksforgeeks.org/python-string-concatenation/)
> - [Python String Interpolation](https://www.geeksforgeeks.org/python-string-interpolation/)

**2) List:** [Lists](https://www.geeksforgeeks.org/python-list/) are just like the arrays, declared in other languages. A single list may contain DataTypes like Integers, Strings, as well as Objects. The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index. It is represented by `list` class.

Python`
# Python program to demonstrate
# Creation of List

# Creating a List
List = []
print(List)

# Creating a list of strings
List = ['GeeksForGeeks', 'Geeks']
print(List)

# Creating a Multi-Dimensional List
List = [['Geeks', 'For'], ['Geeks']]
print(List)
`

```
# Python program to demonstrate
```

```
# Creation of List
```

```

```

```
# Creating a List
```

```
List = []
```

```
print(List)
```

```

```

```
# Creating a list of strings
```

```
List = ['GeeksForGeeks', 'Geeks']
```

```
print(List)
```

```

```

```
# Creating a Multi-Dimensional List
```

```
List = [['Geeks', 'For'], ['Geeks']]
```

```
print(List)
```

**Output:**

```
[]
['GeeksForGeeks', 'Geeks']
[['Geeks', 'For'], ['Geeks']]

```

**Adding Elements to a List:** Using [`append()`](https://www.geeksforgeeks.org/append-extend-python/), [`insert()`](https://www.geeksforgeeks.org/python-list-insert/) and `extend()`

Python`
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []

# Using append()
List.append(1)
List.append(2)
print(List)

# Using insert()
List.insert(3, 12)
List.insert(0, 'Geeks')
print(List)

# Using extend()
List.extend([8, 'Geeks', 'Always'])
print(List)
`

```
# Python program to demonstrate
```

```
# Addition of elements in a List
```

```

```

```
# Creating a List
```

```
List = []
```

```

```

```
# Using append()
```

```
List.append(1)
```

```
List.append(2)
```

```
print(List)
```

```

```

```
# Using insert()
```

```
List.insert(3, 12)
```

```
List.insert(0, 'Geeks')
```

```
print(List)
```

```

```

```
# Using extend()
```

```
List.extend([8, 'Geeks', 'Always'])
```

```
print(List)
```

**Output:**

```
[1, 2]
['Geeks', 1, 2, 12]
['Geeks', 1, 2, 12, 8, 'Geeks', 'Always']

```

**Accessing elements from the List –**

Use the index operator `[ ]` to access an item in a list. In Python, negative sequence indexes represent positions from the end of the array. Instead of having to compute the offset as in `List[len(List)-3]`, it is enough to just write `List[-3]`.

Python`
# Python program to demonstrate
# accessing of element from list


List = [1, 2, 3, 4, 5, 6]

# accessing a element
print(List[0])
print(List[2])

# Negative indexing
# print the last element of list
print(List[-1])
# print the third last element of list
print(List[-3])
`

```
# Python program to demonstrate
```

```
# accessing of element from list
```

```

```

```

```

```
List = [1, 2, 3, 4, 5, 6]
```

```

```

```
# accessing a element
```

```
print(List[0])
```

```
print(List[2])
```

```

```

```
# Negative indexing
```

```
# print the last element of list
```

```
print(List[-1])
```

```
# print the third last element of list
```

```
print(List[-3])
```

**Output:**

```
1
3
6
4

```

**Removing Elements from the List:** Using [`remove()`](https://www.geeksforgeeks.org/python-list-remove/) and [`pop()`](https://www.geeksforgeeks.org/python-list-pop/)

Python`
# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6,\
        7, 8, 9, 10, 11, 12]

# using Remove() method
List.remove(5)
List.remove(6)
print(List)

# using pop()
List.pop()
print(List)
`

```
# Python program to demonstrate
```

```
# Removal of elements in a List
```

```

```

```
# Creating a List
```

```
List = [1, 2, 3, 4, 5, 6,\
```\
\
```\
        7, 8, 9, 10, 11, 12]
```

```

```

```
# using Remove() method
```

```
List.remove(5)
```

```
List.remove(6)
```

```
print(List)
```

```

```

```
# using pop()
```

```
List.pop()
```

```
print(List)
```

**Output:**

```
[1, 2, 3, 4, 7, 8, 9, 10, 11, 12]
[1, 2, 3, 4, 7, 8, 9, 10, 11]

```

**Note:** For more information, refer  [Python List](https://www.geeksforgeeks.org/python-list/).

> **Refer to the below articles to know more about List:**
>
> - [Iterate over a list in Python](https://www.geeksforgeeks.org/iterate-over-a-list-in-python/)
> - [Python List Comprehension and Slicing](https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/)

**3) Tuple:** [Tuple](https://www.geeksforgeeks.org/python-tuples/) is an ordered collection of Python objects much like a list. The important difference between a list and a tuple is that tuples are immutable. It is represented by `tuple` class. In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping of the data sequence.

Python`
# Python program to demonstrate
# creation of Set

# Creating an empty tuple
Tuple1 = ()
print (Tuple1)

# Creating a tuple of strings
print(('Geeks', 'For'))

# Creating a Tuple of list
print(tuple([1, 2, 4, 5, 6]))

# Creating a nested Tuple
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)
`

```
# Python program to demonstrate
```

```
# creation of Set
```

```

```

```
# Creating an empty tuple
```

```
Tuple1 = ()
```

```
print (Tuple1)
```

```

```

```
# Creating a tuple of strings
```

```
print(('Geeks', 'For'))
```

```

```

```
# Creating a Tuple of list
```

```
print(tuple([1, 2, 4, 5, 6]))
```

```

```

```
# Creating a nested Tuple
```

```
Tuple1 = (0, 1, 2, 3)
```

```
Tuple2 = ('python', 'geek')
```

```
Tuple3 = (Tuple1, Tuple2)
```

```
print(Tuple3)
```

**Output:**

```
()
('Geeks', 'For')
(1, 2, 4, 5, 6)
((0, 1, 2, 3), ('python', 'geek'))

```

**Accessing element of a tuple –**

Use the index operator `[ ]` to access an item in a tuple.

Python`
# Python program to
# demonstrate accessing tuple

tuple1 = tuple([1, 2, 3, 4, 5])

# Accessing element using indexing
print(tuple1[0])

# Accessing element using Negative
# Indexing
print(tuple1[-1])
`

```
# Python program to
```

```
# demonstrate accessing tuple
```

```

```

```
tuple1 = tuple([1, 2, 3, 4, 5])
```

```

```

```
# Accessing element using indexing
```

```
print(tuple1[0])
```

```

```

```
# Accessing element using Negative
```

```
# Indexing
```

```
print(tuple1[-1])
```

**Output:**

```
1
5

```

**Deleting/updating elements of tuple –**

Items of a tuple cannot be deleted as tuples are immutable in Python. Only new tuples can be reassigned to the same name.

Python`
# Python program to
# demonstrate updation / deletion
# from a tuple

tuple1 = tuple([1, 2, 3, 4, 5])

# Updating an element
tuple1[0] = -1

# Deleting an element
del tuple1[2]
`

```
# Python program to
```

```
# demonstrate updation / deletion
```

```
# from a tuple
```

```

```

```
tuple1 = tuple([1, 2, 3, 4, 5])
```

```

```

```
# Updating an element
```

```
tuple1[0] = -1
```

```

```

```
# Deleting an element
```

```
del tuple1[2]
```

**Output:**

```
Traceback (most recent call last):
  File "/home/084519a8889e9b0103b874bbbb93e1fb.py", line 11, in
    tuple1[0] = -1
TypeError: 'tuple' object does not support item assignment

Traceback (most recent call last):
  File "/home/ffb3f8be85dd393bde5d0483ff191343.py", line 12, in
    del tuple1[2]
TypeError: 'tuple' object doesn't support item deletion

```

**Note:** For more information, refer  [Python Tuples](https://www.geeksforgeeks.org/python-tuples/).

> **Refer to the below articles to know more about tuples:**
>
> - [Unpacking a Tuple in Python](http://geeksforgeeks.org/unpacking-a-tuple-in-python/)
> - [Operations on Tuples](https://www.geeksforgeeks.org/tuples-in-python/)

### Boolean

Booleans are data type with one of the two built-in values, `True` or `False`. It is denoted by the class bool.

Python`
# Python program to
# demonstrate boolean type

print(type(True))
print(1>2)
print('a'=='a')
`

```
# Python program to
```

```
# demonstrate boolean type
```

```

```

```
print(type(True))
```

```
print(1>2)
```

```
print('a'=='a')
```

**Output:**

```
<class 'bool'>
False
True

```

### Set

In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements. Sets can be created by using the built-in `set()` function with an iterable object or a sequence by placing the sequence inside curly braces `{}`, separated by ‘comma’.

Python`
# Python program to demonstrate
# Creation of Set in Python

# Creating a Set
set1 = set()

# Creating a Set of String
set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set of List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)
`

```
# Python program to demonstrate
```

```
# Creation of Set in Python
```

```

```

```
# Creating a Set
```

```
set1 = set()
```

```

```

```
# Creating a Set of String
```

```
set1 = set("GeeksForGeeks")
```

```
print(set1)
```

```

```

```
# Creating a Set of List
```

```
set1 = set(["Geeks", "For", "Geeks"])
```

```
print(set1)
```

**Output:**

```
{'o', 'r', 'k', 'G', 'e', 's', 'F'}
{'Geeks', 'For'}

```

**Adding elements:** Using [`add()`](https://www.geeksforgeeks.org/set-add-python/) and [`update()`](https://www.geeksforgeeks.org/python-set-update/)

Python`
# Python program to demonstrate
# Addition of elements in a Set


set1 = set()

# Adding to the Set using add()
set1.add(8)
set1.add((6, 7))
print(set1)

# Additio to the Set using Update()
set1.update([10, 11])
print(set1)
`

```
# Python program to demonstrate
```

```
# Addition of elements in a Set
```

```

```

```

```

```
set1 = set()
```

```

```

```
# Adding to the Set using add()
```

```
set1.add(8)
```

```
set1.add((6, 7))
```

```
print(set1)
```

```

```

```
# Additio to the Set using Update()
```

```
set1.update([10, 11])
```

```
print(set1)
```

**Output:**

```
{8, (6, 7)}
{8, 10, 11, (6, 7)}

```

**Accessing a Set:** One can loop through the set items using a `for` loop as set items cannot be accessed by referring to an index.

Python`
# Python program to demonstrate
# Accessing of elements in a set

# Creating a set
set1 = set(["Geeks", "For", "Geeks"])

# Accessing using for loop
for i in set1:
    print(i, end =" ")
`

```
# Python program to demonstrate
```

```
# Accessing of elements in a set
```

```

```

```
# Creating a set
```

```
set1 = set(["Geeks", "For", "Geeks"])
```

```

```

```
# Accessing using for loop
```

```
for i in set1:
```

```
    print(i, end =" ")
```

**Output:**

```
Geeks For

```

**Removing elements from a set:** Using [`remove()`](https://www.geeksforgeeks.org/python-remove-discard-sets/), `discard()`, [pop()](https://www.geeksforgeeks.org/python-list-pop/) and [`clear()`](https://www.geeksforgeeks.org/set-clear-python/)

Python`
# Python program to demonstrate
# Deletion of elements in a Set

set1 = set([1, 2, 3, 4, 5, 6,\
            7, 8, 9, 10, 11, 12])

# using Remove() method
set1.remove(5)
set1.remove(6)
print(set1)

# using Discard() method
set1.discard(8)
set1.discard(9)
print(set1)

# Set using the pop() method
set1.pop()
print(set1)

# Set using clear() method
set1.clear()
print(set1)
`

```
# Python program to demonstrate
```

```
# Deletion of elements in a Set
```

```

```

```
set1 = set([1, 2, 3, 4, 5, 6,\
```\
\
```\
            7, 8, 9, 10, 11, 12])
```

```

```

```
# using Remove() method
```

```
set1.remove(5)
```

```
set1.remove(6)
```

```
print(set1)
```

```

```

```
# using Discard() method
```

```
set1.discard(8)
```

```
set1.discard(9)
```

```
print(set1)
```

```

```

```
# Set using the pop() method
```

```
set1.pop()
```

```
print(set1)
```

```

```

```
# Set using clear() method
```

```
set1.clear()
```

```
print(set1)
```

**Output:**

```
{1, 2, 3, 4, 7, 8, 9, 10, 11, 12}
{1, 2, 3, 4, 7, 10, 11, 12}
{2, 3, 4, 7, 10, 11, 12}
set()

```

**Note:** For more information, refer  [Python Sets](https://www.geeksforgeeks.org/python-sets/).

> **Refer to the below articles to know more about Sets:**
>
> - [Iterate over a set in Python](https://www.geeksforgeeks.org/iterate-over-a-set-in-python/)
> - [frozenset() in Python](https://www.geeksforgeeks.org/frozenset-in-python/)

### Dictionary

[Dictionary](https://www.geeksforgeeks.org/python-dictionary/) in Python is an unordered collection of data values, used to store data values like a map. Dictionary holds `key:value` pair. Each key-value pair in a Dictionary is separated by a colon `:`, whereas each key is separated by a ‘comma’. A Dictionary can be created by placing a sequence of elements within curly `{}` braces, separated by ‘comma’.

Python`
# Creating an empty Dictionary
Dict = {}
print(Dict)

# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict)
`

```
# Creating an empty Dictionary
```

```
Dict = {}
```

```
print(Dict)
```

```

```

```
# with Integer Keys
```

```
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
```

```
print(Dict)
```

```

```

```
# with Mixed keys
```

```
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
```

```
print(Dict)
```

**Output:**

```
{}
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
{1: [1, 2, 3, 4], 'Name': 'Geeks'}

```

**Nested Dictionary:**

![Nested-Dictionary](https://media.geeksforgeeks.org/wp-content/uploads/20191224155528/Dictionary-Creation-11.jpg)

Python`
# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}

print(Dict)
`

```
# Creating a Nested Dictionary
```

```
# as shown in the below image
```

```
Dict = {1: 'Geeks', 2: 'For',
```

```
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
```

```

```

```
print(Dict)
```

**Output:**

```
{1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

```

**Note:** For more information, refer  [Python Nested Dictionary](https://www.geeksforgeeks.org/python-nested-dictionary/).

**Adding elements to a Dictionary:** One value at a time can be added to a Dictionary by defining value along with the key e.g. `Dict[Key] = ‘Value’`.

Python`
# Creating an empty Dictionary
Dict = {}

# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict)


# Updating existing Key's Value
Dict[2] = 'Welcome'
print(Dict)
`

```
# Creating an empty Dictionary
```

```
Dict = {}
```

```

```

```
# Adding elements one at a time
```

```
Dict[0] = 'Geeks'
```

```
Dict[2] = 'For'
```

```
Dict[3] = 1
```

```
print(Dict)
```

```

```

```

```

```
# Updating existing Key's Value
```

```
Dict[2] = 'Welcome'
```

```
print(Dict)
```

**Output:**

```
{0: 'Geeks', 2: 'For', 3: 1}
{0: 'Geeks', 2: 'Welcome', 3: 1}

```

**Accessing elements from a Dictionary:** In order to access the items of a dictionary refer to its key name or use [`get()`](https://www.geeksforgeeks.org/get-method-dictionaries-python/) method.

Python`
# Python program to demonstrate
# accessing an element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using key
print(Dict['name'])

# accessing a element using get()
print(Dict.get(3))
`

```
# Python program to demonstrate
```

```
# accessing an element from a Dictionary
```

```

```

```
# Creating a Dictionary
```

```
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
```

```

```

```
# accessing a element using key
```

```
print(Dict['name'])
```

```

```

```
# accessing a element using get()
```

```
print(Dict.get(3))
```

**Output:**

```
For
Geeks

```

**Removing Elements from Dictionary:** Using [`pop()`](https://www.geeksforgeeks.org/python-dictionary-pop-method/) and [`popitem()`](https://www.geeksforgeeks.org/python-dictionary-popitem-method/)

Python`
# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
       }

# using pop()
Dict.pop(5)
print(Dict)

# using popitem()
Dict.popitem()
print(Dict)
`

```
# Initial Dictionary
```

```
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
```

```
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
```

```
       }
```

```

```

```
# using pop()
```

```
Dict.pop(5)
```

```
print(Dict)
```

```

```

```
# using popitem()
```

```
Dict.popitem()
```

```
print(Dict)
```

**Output:**

```
{'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'}, 6: 'To', 7: 'Geeks'}
{6: 'To', 7: 'Geeks'}

```

**Note:** For more information, refer [Python Dictionary](https://www.geeksforgeeks.org/python-dictionary/).

> **Refer to the below articles to know more about dictionary:**
>
> - [Operations on Dictionary](https://www.geeksforgeeks.org/few-mistakes-when-using-python-dictionary/)
> - [Iterate over a dictionary in Python](https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/)

## Decision Making

Decision Making in programming is similar to decision making in real life. A programming language uses control statements to control the flow of execution of the program based on certain conditions. These are used to cause the flow of execution to advance and branch based on changes to the state of a program.

**Decision-making statements in Python**

- [if statement](https://www.geeksforgeeks.org/decision-making-python-else-nested-elif/#if)
- if..else statements
- nested if statements
- if-elif ladder

**Example 1:** To demonstrate `if` and `if-else`

Python`
# Python program to demonstrate
# decision making

a = 10
b = 15

# if to check even number
if a % 2 == 0:
    print("Even Number")

# if-else to check even or odd
if b % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
`

```
# Python program to demonstrate
```

```
# decision making
```

```

```

```
a = 10
```

```
b = 15
```

```

```

```
# if to check even number
```

```
if a % 2 == 0:
```

```
    print("Even Number")
```

```

```

```
# if-else to check even or odd
```

```
if b % 2 == 0:
```

```
    print("Even Number")
```

```
else:
```

```
    print("Odd Number")
```

**Output:**

```
Even Number
Odd Number

```

**Example 2:** To demonstrate `nested-if` and `if-elif`

Python`
# Python program to demonstrate
# decision making

a = 10

# Nested if to check whether a
# number is divisible by both 2 and 5
if a % 2 == 0:
    if a % 5 == 0:
        print("Number is divisible by both 2 and 5")

# is-elif
if (a == 11):
    print ("a is 11")
elif (a == 10):
    print ("a is 10")
else:
    print ("a is not present")
`

```
# Python program to demonstrate
```

```
# decision making
```

```

```

```
a = 10
```

```

```

```
# Nested if to check whether a
```

```
# number is divisible by both 2 and 5
```

```
if a % 2 == 0:
```

```
    if a % 5 == 0:
```

```
        print("Number is divisible by both 2 and 5")
```

```

```

```
# is-elif
```

```
if (a == 11):
```

```
    print ("a is 11")
```

```
elif (a == 10):
```

```
    print ("a is 10")
```

```
else:
```

```
    print ("a is not present")
```

**Output:**

```
Number is divisible by both 2 and 5
a is 10
```

## Control flow (Loops)

[Loops](https://www.geeksforgeeks.org/loops-in-python/) in programming come into use when we need to repeatedly execute a block of statements. For example: Suppose we want to print “Hello World” 10 times. This can be done with the help of loops. The loops in Python are:

[**While and while-else loop**](https://www.geeksforgeeks.org/python-while-loops/)![while-loop](https://media.geeksforgeeks.org/wp-content/uploads/20191226130537/while-loop1.jpg)Python``

```python3
</p><pre><code class="language-python3"></code></pre><p></p><pre></pre><p><br></p><p dir="ltr"><br></p><pre><code><span># Python program to illustrate  </span></code><br><code><span># while and while-else loop</span></code><br><code><span>i = 0</span></code><br><code><span>while (i < 3):      </span></code><br><code><span>    i = i + 1</span></code><br><code><span>    print("Hello Geek")  </span></code><br><code><span>   </span></code><br><code><span># checks if list still </span></code><br><code><span># contains any element  </span></code><br><code><span>a = [1, 2, 3, 4] </span></code><br><code><span>while a: </span></code><br><code><span>    print(a.pop()) </span></code><br><code><span>   </span></code><br><code><span>i = 10</span></code><br><code><span>while i < 12:  </span></code><br><code><span>    i += 1</span></code><br><code><span>    print(i)  </span></code><br><code><span>    break</span></code><br><code><span>else: # Not executed as there is a break  </span></code><br><code><span>    print("No Break")</span></code><br></pre><p dir="ltr"><b><strong>Output:</strong></b></p><pre><span>Hello Geek</span><br><span>Hello Geek</span><br><span>Hello Geek</span><br><span>4</span><br><span>3</span><br><span>2</span><br><span>1</span><br><span>11</span></pre><p dir="ltr"><a href="https://www.geeksforgeeks.org/python-for-loops/" target="_blank" rel="noopener"><b><strong>For and for-else loop</strong></b></a><img src="https://media.geeksforgeeks.org/wp-content/uploads/20191226130622/for-loop-python1.jpg" alt="for-loop-python" width="620" height="381" loading="lazy"></p><gfg-tabs data-run-ide="true" data-mode="light"><gfg-tab slot="tab">Python</gfg-tab><gfg-panel slot="panel" data-code-lang="python3"><pre><code class="language-python3"># Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s :
    print(i)

print("\nFor-else loop")
for i in s:
    print(i)
else: # Executed because no break in for
    print("No Break\n")

for i in s:
    print(i)
    break
else: # Not executed as there is a break
    print("No Break")

```

**Output:**

```
List Iteration
geeks
for
geeks

String Iteration
G
e
e
k
s

For-else loop
G
e
e
k
s
No Break

G
```

[**range() function:**](https://www.geeksforgeeks.org/python-range-function/) `range()` allows user to generate a series of numbers within a given range. Depending on how many arguments user is passing to the function. This function takes three arguments. **1) start:** integer starting from which the sequence of integers is to be returned

**2) stop:** integer before which the sequence of integers is to be returned.

**3) step:** integer value which determines the increment between each integer in the sequence

filter\_none![PythonRange](https://media.geeksforgeeks.org/wp-content/uploads/20191224171636/PythonRange0102-11.png)

Python`
# Python program to demonstrate
# range() function


for i in range(5):
    print(i, end =" ")
print()

for i in range(2, 9):
    print(i, end =" ")
print()

# incremented by 3
for i in range(15, 25, 3):
    print(i, end =" ")
`

```
# Python program to demonstrate
```

```
# range() function
```

```

```

```

```

```
for i in range(5):
```

```
    print(i, end =" ")
```

```
print()
```

```

```

```
for i in range(2, 9):
```

```
    print(i, end =" ")
```

```
print()
```

```

```

```
# incremented by 3
```

```
for i in range(15, 25, 3):
```

```
    print(i, end =" ")
```

**Output:**

```
0 1 2 3 4
2 3 4 5 6 7 8
15 18 21 24
```

> **Refer to the below articles to know more about Loops:**
>
> - [Understanding for-loop in Python](https://www.geeksforgeeks.org/understanding-for-loop-in-python/)
> - [Backward iteration in Python](https://www.geeksforgeeks.org/backward-iteration-in-python/)

## Loop control statements

[Loop control statements](https://www.geeksforgeeks.org/loops-and-loop-control-statements-continue-break-and-pass-in-python/) change execution from its normal sequence. Following are the loop control statements provided by Python:

- [**Break:**](https://www.geeksforgeeks.org/python-break-statement/) Break statement in Python is used to bring the control out of the loop when some external condition is triggered.
- [**Continue:**](https://www.geeksforgeeks.org/python-continue-statement/) Continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.
- [**Pass:**](https://www.geeksforgeeks.org/python-pass-statement/) Pass statement is used to write empty loops. Pass is also used for empty control statement, function and classes.

Python`
# Python program to demonstrate
# break, continue and pass

s = 'geeksforgeeks'

for letter in s:
    if letter == 'e' or letter == 's':
        break
    print(letter, end = " ")
print()

for letter in s:
    if letter == 'e' or letter == 's':
        continue
    print(letter, end = " ")
print()

for letter in s:
    if letter == 'e' or letter == 's':
        pass
    print(letter, end = " ")
`

```
# Python program to demonstrate
```

```
# break, continue and pass
```

```

```

```
s = 'geeksforgeeks'
```

```

```

```
for letter in s:
```

```
    if letter == 'e' or letter == 's':
```

```
        break
```

```
    print(letter, end = " ")
```

```
print()
```

```

```

```
for letter in s:
```

```
    if letter == 'e' or letter == 's':
```

```
        continue
```

```
    print(letter, end = " ")
```

```
print()
```

```

```

```
for letter in s:
```

```
    if letter == 'e' or letter == 's':
```

```
        pass
```

```
    print(letter, end = " ")
```

**Output:**

```
g
g k f o r g k
g e e k s f o r g e e k s
```

## Functions

[Functions](https://www.geeksforgeeks.org/functions-in-python/) are generally the block of codes or statements in a program that gives the user the ability to reuse the same code which ultimately saves the excessive use of memory, acts as a time saver and more importantly, provides better readability of the code. So basically, a function is a collection of statements that perform some specific task and return the result to the caller. A function can also perform some specific task without returning anything. In Python, `def` keyword is used to create functions.

Python`
# Python program to demonstrate
# functions


# Defining functions
def ask_user():
    print("Hello Geeks")

# Function that returns sum
# of first 10 numbers
def my_func():
    a = 0
    for i in range(1, 11):
        a = a + i
    return a

# Calling functions
ask_user()
res = my_func()
print(res)
`

```
# Python program to demonstrate
```

```
# functions
```

```

```

```

```

```
# Defining functions
```

```
def ask_user():
```

```
    print("Hello Geeks")
```

```

```

```
# Function that returns sum
```

```
# of first 10 numbers
```

```
def my_func():
```

```
    a = 0
```

```
    for i in range(1, 11):
```

```
        a = a + i
```

```
    return a
```

```

```

```
# Calling functions
```

```
ask_user()
```

```
res = my_func()
```

```
print(res)
```

**Output:**

```
Hello Geeks
55

```

### Function with arguments

- [**Default arguments:**](https://www.geeksforgeeks.org/default-arguments-in-python/) A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

Python`
# Python program to demonstrate
# default arguments


def myFun(x, y = 50):
    print("x: ", x)
    print("y: ", y)

# Driver code
myFun(10)
`

```
# Python program to demonstrate
```

```
# default arguments
```

```

```

```

```

```
def myFun(x, y = 50):
```

```
    print("x: ", x)
```

```
    print("y: ", y)
```

```

```

```
# Driver code
```

```
myFun(10)
```

**Output:**

```
('x: ', 10)
('y: ', 50)

```

- **Keyword arguments:** The idea is to allow caller to specify argument name with values so that caller does not need to remember order of parameters.

Python`
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
     print(firstname, lastname)


# Keyword arguments
student(firstname ='Geeks', lastname ='Practice')
student(lastname ='Practice', firstname ='Geeks')
`

```
# Python program to demonstrate Keyword Arguments
```

```
def student(firstname, lastname):
```

```
     print(firstname, lastname)
```

```

```

```

```

```
# Keyword arguments
```

```
student(firstname ='Geeks', lastname ='Practice')
```

```
student(lastname ='Practice', firstname ='Geeks')
```

**Output:**

```
('Geeks', 'Practice')
('Geeks', 'Practice')

```

- [**Variable length arguments:**](https://www.geeksforgeeks.org/args-kwargs-python/) In Python a function can also have variable number of arguments. This can be used in the case when we do not know in advance the number of arguments that will be passed into a function.

Python`
# Python program to demonstrate
# variable length arguments


# variable arguments
def myFun1(*argv):
    for arg in argv:
        print(arg, end =" ")

# variable keyword arguments
def myFun2(**kwargs):
    for key, value in kwargs.items():
        print ("% s == % s" %(key, value))

# Driver code
myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print()
myFun2(first ='Geeks', mid ='for', last ='Geeks')
`

```
# Python program to demonstrate
```

```
# variable length arguments
```

```

```

```

```

```
# variable arguments
```

```
def myFun1(*argv):
```

```
    for arg in argv:
```

```
        print(arg, end =" ")
```

```

```

```
# variable keyword arguments
```

```
def myFun2(**kwargs):
```

```
    for key, value in kwargs.items():
```

```
        print ("% s == % s" %(key, value))
```

```

```

```
# Driver code
```

```
myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')
```

```
print()
```

```
myFun2(first ='Geeks', mid ='for', last ='Geeks')
```

**Output:**

```
Hello Welcome to GeeksforGeeks
first == Geeks
last == Geeks
mid == for

```

**Note:** For more information, refer  [Functions in Python](https://www.geeksforgeeks.org/functions-in-python/).

> **Refer to the below articles to know more about functions:**
>
> - [Python Inner Functions](https://www.geeksforgeeks.org/python-inner-functions/)
> - [Python return statement](https://www.geeksforgeeks.org/python-return-statement/)
> - [Call function from another function](http://geeksforgeeks.org/python-call-function-from-another-function/)

### Lambda functions

In Python, the [lambda/anonymous](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/) function means that a function is without a name. The `lambda` keyword is used to create anonymous functions. Lambda function can have any number of arguments but has only one expression.

Python`
# Python code to demonstrate
# labmda function

# Cube using lambda
cube = lambda x: x * x*x
print(cube(7))

# List comprehension using lambda
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)
`

```
# Python code to demonstrate
```

```
# labmda function
```

```

```

```
# Cube using lambda
```

```
cube = lambda x: x * x*x
```

```
print(cube(7))
```

```

```

```
# List comprehension using lambda
```

```
a = [(lambda x: x * 2)(x) for x in range(5)]
```

```
print(a)
```

**Output:**

```
343
[0, 2, 4, 6, 8]

```

**Note:** For more information, refer  [Python lambda (Anonymous Functions)](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/).

## Object Oriented Programming

Object-oriented programming aims to implement real-world entities like inheritance, hiding, polymorphism, etc in programming. The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

![Python-OOPS-Concept](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200623174126/Python-OOPS-Concept.png)

### Classes and Objects

[Class](https://www.geeksforgeeks.org/python-classes-and-objects/) creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

An [Object](https://www.geeksforgeeks.org/python-classes-and-objects/) is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values.

Python`
# Python code to demonstrate
# labmda function

# Cube using lambda
cube = lambda x: x * x*x
print(cube(7))

# List comprehension using lambda
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)
`

```
# Python code to demonstrate
```

```
# labmda function
```

```

```

```
# Cube using lambda
```

```
cube = lambda x: x * x*x
```

```
print(cube(7))
```

```

```

```
# List comprehension using lambda
```

```
a = [(lambda x: x * 2)(x) for x in range(5)]
```

```
print(a)
```

**Output:**

```
mamal
I'm a mamal
I'm a dog
```

**The self**

[self](https://www.geeksforgeeks.org/self-in-python-class/) represents the instance of the class. By using the “ `self`” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.

**Note:** For more information, refer  [self in Python class](https://www.geeksforgeeks.org/self-in-python-class/).

### Constructors and Destructors

[**Constructors:**](https://www.geeksforgeeks.org/constructors-in-python/) Constructors are generally used for instantiating an object.The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created. In Python the `__init__()` method is called the constructor and is always called when an object is created. There can be two types of constructors:

- **Default constructor:** The constructor which is called implicilty and do not accept any argument.
- **Parameterized constructor:** Constructor which is called explicitly with parameters is known as parameterized constructor.

Python`
# Python program to demonstrate
# constructors


class Addition:
    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def calculate(self):
        print(self.first + self.second)

# Invoking parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()
`

```
# Python program to demonstrate
```

```
# constructors
```

```

```

```

```

```
class Addition:
```

```
    # parameterized constructor
```

```
    def __init__(self, f, s):
```

```
        self.first = f
```

```
        self.second = s
```

```

```

```
    def calculate(self):
```

```
        print(self.first + self.second)
```

```

```

```
# Invoking parameterized constructor
```

```
obj = Addition(1000, 2000)
```

```

```

```
# perform Addition
```

```
obj.calculate()
```

**Output:**

```
3000
```

[**Destructors:**](https://www.geeksforgeeks.org/destructors-in-python/) Destructors are called when an object gets destroyed. The [`__del__()`](https://www.geeksforgeeks.org/delattr-del-python/) method is a known as a destructor method in Python. It is called when all references to the object have been deleted i.e when an object is garbage collected.

Python`
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj
`

```
class Employee:
```

```

```

```
    # Initializing
```

```
    def __init__(self):
```

```
        print('Employee created.')
```

```

```

```
    # Deleting (Calling destructor)
```

```
    def __del__(self):
```

```
        print('Destructor called, Employee deleted.')
```

```

```

```
obj = Employee()
```

```
del obj
```

**Output:**

```
Employee created.
Destructor called, Employee deleted.
```

## Inheritance

Inheritance is the ability of any class to extract and use features of other classes. It is the process by which new classes called the derived classes are created from existing classes called Base classes.

Python`
# A Python program to demonstrate inheritance


class Person():

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is employee
    def isEmployee(self):
        return False


# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())
`

```
# A Python program to demonstrate inheritance
```

```

```

```

```

```
class Person():
```

```

```

```
    # Constructor
```

```
    def __init__(self, name):
```

```
        self.name = name
```

```

```

```
    # To get name
```

```
    def getName(self):
```

```
        return self.name
```

```

```

```
    # To check if this person is employee
```

```
    def isEmployee(self):
```

```
        return False
```

```

```

```

```

```
# Inherited or Sub class (Note Person in bracket)
```

```
class Employee(Person):
```

```

```

```
    # Here we return true
```

```
    def isEmployee(self):
```

```
        return True
```

```

```

```
# Driver code
```

```
emp = Person("Geek1")  # An Object of Person
```

```
print(emp.getName(), emp.isEmployee())
```

```

```

```
emp = Employee("Geek2") # An Object of Employee
```

```
print(emp.getName(), emp.isEmployee())
```

**Output:**

```
Geek1 False
Geek2 True

```

**Note:** For more information, refer  [Python inheritance](https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/).

### Encapsulation

[Encapsulation](https://www.geeksforgeeks.org/encapsulation-in-python/) describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

Python`
# Python program to demonstrate
# encapsulation

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__a)
# Driver code
obj = Derived()
`

```
# Python program to demonstrate
```

```
# encapsulation
```

```

```

```
# Creating a Base class
```

```
class Base:
```

```
    def __init__(self):
```

```
        self.a = "GeeksforGeeks"
```

```
        self.__c = "GeeksforGeeks"
```

```

```

```
# Creating a derived class
```

```
class Derived(Base):
```

```
    def __init__(self):
```

```

```

```
        # Calling constructor of
```

```
        # Base class
```

```
        Base.__init__(self)
```

```
        print("Calling private member of base class: ")
```

```
        print(self.__a)
```

```
# Driver code
```

```
obj = Derived()
```

**Output:**

```
Traceback (most recent call last):
  File "/home/5a605c59b5b88751d2b93dd5f932dbd5.py", line 20, in
    obj = Derived()
  File "/home/5a605c59b5b88751d2b93dd5f932dbd5.py", line 18, in __init__
    print(self.__a)
AttributeError: 'Derived' object has no attribute '_Derived__a'
```

### Polymorphism

[Polymorphism](https://www.geeksforgeeks.org/polymorphism-in-python/) refers to the ability of OOPs programming languages to differentiate between entities with the same name efficiently. This is done by Python with the help of the signature of these entities.

Python`
# Python program to demonstrate
# Polymorphism


class A():
    def show(self):
        print("Inside A")

class B():
    def show(self):
        print("Inside B")

# Driver's code
a = A()
a.show()
b = B()
b.show()
`

```
# Python program to demonstrate
```

```
# Polymorphism
```

```

```

```

```

```
class A():
```

```
    def show(self):
```

```
        print("Inside A")
```

```

```

```
class B():
```

```
    def show(self):
```

```
        print("Inside B")
```

```

```

```
# Driver's code
```

```
a = A()
```

```
a.show()
```

```
b = B()
```

```
b.show()
```

**Output:**

```
Inside A
Inside B

```

> **Refer to the articles to know more about OOPS:**
>
> - [Bound, unbound, and static methods in Python](https://www.geeksforgeeks.org/bound-unbound-and-static-methods-in-python/)
> - [Multiple inheritance in Python](https://www.geeksforgeeks.org/multiple-inheritance-in-python/)
> - [\_\_new\_\_ in Python](https://www.geeksforgeeks.org/__new__-in-python/)

## File Handling

[File handling](https://www.geeksforgeeks.org/file-handling-python/) is the ability of Python to handle files i.e. to read and write files along with many other file handling options. Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters and they form a text file. Each line of a file is terminated with a special character, called the **EOL or End of Line characters** like comma `{, }` or newline character.

Basic File Handling operations in Python are:

[**1) Open a file:**](https://www.geeksforgeeks.org/open-a-file-in-python/) Opening a file refers to getting the file ready either for reading or for writing. This can be done using the `open()` function. This function returns a file object and takes two arguments, one that accepts the file name and another that accepts the mode(Access Mode). Python provides six Access Modes:

| ACCESS MODE | DESCRIPTION |
| --- | --- |
| Read Only (‘r’) | Open text file for reading. The handle is positioned at the beginning of the file. |
| Read and Write (‘r+’) | Open the file for reading and writing. The handle is positioned at the beginning of the file. |
| Write Only (‘w’) | Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. |
| Write and Read (‘w+’) | Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file. |
| Append Only (‘a’) | Open the file for writing. The handle is positioned at the end of the file. |
| Append and Read (‘a+’) | Open the file for reading and writing. The handle is positioned at the end of the file. |

Python`
# Python program to demonstrate
# Polymorphism


class A():
    def show(self):
        print("Inside A")

class B():
    def show(self):
        print("Inside B")

# Driver's code
a = A()
a.show()
b = B()
b.show()
`

```
# Python program to demonstrate
```

```
# Polymorphism
```

```

```

```

```

```
class A():
```

```
    def show(self):
```

```
        print("Inside A")
```

```

```

```
class B():
```

```
    def show(self):
```

```
        print("Inside B")
```

```

```

```
# Driver's code
```

```
a = A()
```

```
a.show()
```

```
b = B()
```

```
b.show()
```

**Note:** For more information, refer  [Open a File in Python](https://www.geeksforgeeks.org/open-a-file-in-python/).

**2) Close the file:** `close()` function closes the file and frees the memory space acquired by that file.

Python`
# Opening and Closing a file "MyFile.txt"
# for object name file1.
file1 = open("MyFile.txt", "a")
file1.close()
`

```
# Opening and Closing a file "MyFile.txt"
```

```
# for object name file1.
```

```
file1 = open("MyFile.txt", "a")
```

```
file1.close()
```

[**3) Reading from a File:**](https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/) There are three ways to read data from a text file.

- **read():** Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.

```
File_object.read([n])
```

- **readline():** Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.

```
File_object.readline([n])
```

- **readlines():** Reads all the lines and return them as each line a string element in a list.

```
File_object.readlines()
```


Let’s suppose the file looks like this:

![python-file-handling](https://media.geeksforgeeks.org/wp-content/uploads/20191226153425/python-file-handling.png)

Python`
# Program to show various ways to
# read data from a file.

file1 = open("data.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
`

```
# Program to show various ways to
```

```
# read data from a file.
```

```

```

```
file1 = open("data.txt", "r+")
```

```

```

```
print("Output of Read function is ")
```

```
print(file1.read())
```

```
print()
```

```

```

```
# seek(n) takes the file handle to the nth
```

```
# bite from the beginning.
```

```
file1.seek(0)
```

```

```

```
print("Output of Readline function is ")
```

```
print(file1.readline())
```

```
print()
```

```

```

```
file1.seek(0)
```

```

```

```
# readlines function
```

```
print("Output of Readlines function is ")
```

```
print(file1.readlines())
```

```
print()
```

```
file1.close()
```

**Output:**

```
Output of Read function is
Code is like humor. When you have to explain it, its bad.

Output of Readline function is
Code is like humor. When you have to explain it, its bad.

Output of Readlines function is
['Code is like humor. When you have to explain it, its bad.']

```

**Note:** For more information, refer  [How to read from a file in Python](https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/).

[**4) Writing to a file:**](https://www.geeksforgeeks.org/writing-to-file-in-python/) There are two ways to write in a file.

- **write():** Inserts the string str1 in a single line in the text file.

```
File_object.write(str1)
```

- **writelines():** For a list of string elements, each string is inserted in the text file. Used to insert multiple strings at a single time.

```
File_object.writelines(L) for L = [str1, str2, str3]
```


Python`
# Python program to demonstrate
# writing to file

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)

# Closing file
file1.close()
`

```
# Python program to demonstrate
```

```
# writing to file
```

```

```

```
# Opening a file
```

```
file1 = open('myfile.txt', 'w')
```

```
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
```

```
s = "Hello\n"
```

```

```

```
# Writing a string to file
```

```
file1.write(s)
```

```

```

```
# Writing multiple strings
```

```
# at a time
```

```
file1.writelines(L)
```

```

```

```
# Closing file
```

```
file1.close()
```

**Output:**

![python-writing-to-file](https://media.geeksforgeeks.org/wp-content/uploads/20191226154245/python-writing-to-file.png)

**Note:** For more information, refer  [Writing to file in Python](https://www.geeksforgeeks.org/writing-to-file-in-python/).

> **Refer to the below articles to know more about File-Handling:**
>
> - [Python seek() function](https://www.geeksforgeeks.org/python-seek-function/)
> - [Python tell() function](https://www.geeksforgeeks.org/python-tell-function/)
> - [OS Module in Python](https://www.geeksforgeeks.org/os-module-python-examples/)
> - [Programs on OS module](https://www.geeksforgeeks.org/tag/python-os-module/)

## Modules and Packages

## Modules

A module is a self-contained Python file that contains Python statements and definitions, like a file named `GFG.py`, which can be considered as a module named `GFG` which can be imported with the help of [`import statement`](https://www.geeksforgeeks.org/import-module-python/).

Let’s create a simple module named GFG.

Python`
# Python program to demonstrate
# modules


# Defining a function
def Geeks():
    print("GeeksforGeeks")

# Defining a variable
location = "Noida"

# Defining a class
class Employee():

    def __init__(self, name, position):
        self. name = name
        self.position = position

    def show(self):
        print("Employee name:", self.name)
        print("Employee position:", self.position)
`

```
# Python program to demonstrate
```

```
# modules
```

```

```

```

```

```
# Defining a function
```

```
def Geeks():
```

```
    print("GeeksforGeeks")
```

```

```

```
# Defining a variable
```

```
location = "Noida"
```

```

```

```
# Defining a class
```

```
class Employee():
```

```

```

```
    def __init__(self, name, position):
```

```
        self. name = name
```

```
        self.position = position
```

```

```

```
    def show(self):
```

```
        print("Employee name:", self.name)
```

```
        print("Employee position:", self.position)
```

To use the above created module, create a new Python file in the same directory and import GFG module using the [`import`](https://www.geeksforgeeks.org/import-module-python/) statement.

Python`
# Python program to demonstrate
# modules


# Defining a function
def Geeks():
    print("GeeksforGeeks")

# Defining a variable
location = "Noida"

# Defining a class
class Employee():

    def __init__(self, name, position):
        self. name = name
        self.position = position

    def show(self):
        print("Employee name:", self.name)
        print("Employee position:", self.position)
`

```
# Python program to demonstrate
```

```
# modules
```

```

```

```

```

```
# Defining a function
```

```
def Geeks():
```

```
    print("GeeksforGeeks")
```

```

```

```
# Defining a variable
```

```
location = "Noida"
```

```

```

```
# Defining a class
```

```
class Employee():
```

```

```

```
    def __init__(self, name, position):
```

```
        self. name = name
```

```
        self.position = position
```

```

```

```
    def show(self):
```

```
        print("Employee name:", self.name)
```

```
        print("Employee position:", self.position)
```

**Output:**

```
GeeksforGeeks
Noida
Employee name: Nikhil
Employee position: Developer

```

**Note:** For more information, refer  [Python Modules](https://www.geeksforgeeks.org/python-modules/).

## Packages

Packages are a way of structuring many packages and modules which helps in a well-organized hierarchy of data set, making the directories and modules easy to access.

To create a package in Python, we need to follow these three simple steps:

- First, we create a directory and give it a package name, preferably related to its operation.
- Then we put the classes and the required functions in it.
- Finally we create an `__init__.py` file inside the directory, to let Python know that the directory is a package.

**Example:** Let’s create a package for cars.

- First we create a directory and name it Cars.
- Then we need to create modules. We will create 2 modules – BMW and AUDI.For Bmw.py






|     |
| --- |
| `# Python code to illustrate the Modules `<br>`class` `Bmw: `<br>`    ``def` `__init__(` `self` `): `<br>`        ``self` `.models ` `=` `[` `'i8'` `, ` `'x1'` `, ` `'x5'` `, ` `'x6'` `] `<br>`   `<br>`    ``def` `outModels(` `self` `): `<br>`        ``print` `(` `'These are the available models for BMW'` `) `<br>`        ``for` `model ` `in` `self` `.models: `<br>`            ``print` `(` `'\t % s '` `%` `model)` |






For Audi.py






|     |
| --- |
| `# Python code to illustrate the Module `<br>`class` `Audi: `<br>`    ``def` `__init__(` `self` `): `<br>`        ``self` `.models ` `=` `[` `'q7'` `, ` `'a6'` `, ` `'a8'` `, ` `'a3'` `] `<br>`  `<br>`    ``def` `outModels(` `self` `): `<br>`        ``print` `(` `'These are the available models for Audi'` `) `<br>`        ``for` `model ` `in` `self` `.models: `<br>`            ``print` `(` `'\t % s '` `%` `model) ` |

- Finally we create the \_\_init\_\_.py file. This file will be placed inside the Cars directory and can be left blank.

Now, let’s use the package that we created. To do this make a sample.py file in the same directory where Cars package is located and add the following code to it:

Python`
# Import classes from your brand new package
from Cars import Bmw
from Cars import Audi

# Create an object of Bmw class & call its method
ModBMW = Bmw()
ModBMW.outModels()

# Create an object of Audi class & call its method
ModAudi = Audi()
ModAudi.outModels()
`

```
# Import classes from your brand new package
```

```
from Cars import Bmw
```

```
from Cars import Audi
```

```

```

```
# Create an object of Bmw class & call its method
```

```
ModBMW = Bmw()
```

```
ModBMW.outModels()
```

```

```

```
# Create an object of Audi class & call its method
```

```
ModAudi = Audi()
```

```
ModAudi.outModels()
```

**Output:**

![python-packages1](https://media.geeksforgeeks.org/wp-content/uploads/20191226170910/python-packages1.png)

**Note:** For more information, refer  [Create and Access a Python Package](https://www.geeksforgeeks.org/create-access-python-package/).

## Regular expressions(RegEx)

[Python RegEx](https://www.geeksforgeeks.org/python-regex/) is a powerful text matching tool that uses a pre-defined pattern to match the text. It can identify the presence or absence of text by comparing it to a specific pattern, and it can also divide a pattern into one or more sub-patterns. Below is the list of metacharacters:

```
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One ore more occurrences
{}  Indicate the number of occurrences of a preceding RE
    to match.
()  Enclose a group of REs

```

The most frequently used methods are:

**re.findall():** Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found.

Python`
# A Python program to demonstrate working of
# findall()
import re


string = """Hello my Number is 123456789 and
             my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)
`

```
# A Python program to demonstrate working of
```

```
# findall()
```

```
import re
```

```

```

```

```

```
string = """Hello my Number is 123456789 and
```

```
             my friend's number is 987654321"""
```

```

```

```
# A sample regular expression to find digits.
```

```
regex = '\d+'
```

```

```

```
match = re.findall(regex, string)
```

```
print(match)
```

**Output:**

```
['123456789', '987654321']

```

In the above example, metacharacter blackslash

`‘\’`

has a very important role as it signals various sequences. If the blackslash is to be used without its special meaning as metacharacter, use

`’\\’`

.<>

```
\d   Matches any decimal digit, this is equivalent
     to the set class [0-9].
\D   Matches any non-digit character.
\s   Matches any whitespace character.
\S   Matches any non-whitespace character
\w   Matches any alphanumeric character, this is
     equivalent to the class [a-zA-Z0-9_].
\W   Matches any non-alphanumeric character.

```

**re.compile():** Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions.

Python`
# A Python program to demonstrate working of
# compile()
import re

# it is equivalent to [abcde].
p = re.compile('[a-e]')

print(p.findall("Aye, said Mr. Gibenson Stark"))
`

```
# A Python program to demonstrate working of
```

```
# compile()
```

```
import re
```

```

```

```
# it is equivalent to [abcde].
```

```
p = re.compile('[a-e]')
```

```

```

```
print(p.findall("Aye, said Mr. Gibenson Stark"))
```

**Output:**

```
['e', 'a', 'd', 'b', 'e', 'a']

```

**re.match():** This function attempts to match pattern to whole string. The re.match function returns a match object on success, None on failure.

Python`
# A Python program to demonstrate working
# of re.match().
import re


def findMonthAndDate(string):

    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print("Not a valid date")
        return

    print("Given Data: % s" % (match.group()))
    print("Month: % s" % (match.group(1)))
    print("Day: % s" % (match.group(2)))


# Driver Code
findMonthAndDate("Jun 24")
print("")
findMonthAndDate("I was born on June 24")
`

```
# A Python program to demonstrate working
```

```
# of re.match().
```

```
import re
```

```

```

```

```

```
def findMonthAndDate(string):
```

```

```

```
    regex = r"([a-zA-Z]+) (\d+)"
```

```
    match = re.match(regex, string)
```

```

```

```
    if match == None:
```

```
        print("Not a valid date")
```

```
        return
```

```

```

```
    print("Given Data: % s" % (match.group()))
```

```
    print("Month: % s" % (match.group(1)))
```

```
    print("Day: % s" % (match.group(2)))
```

```

```

```

```

```
# Driver Code
```

```
findMonthAndDate("Jun 24")
```

```
print("")
```

```
findMonthAndDate("I was born on June 24")
```

**Output:**

```
Given Data: Jun 24
Month: Jun
Day: 24

Not a valid date

```

**re.search():** This method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string.

Python`
# A Python program to demonstrate working of re.match().
import re

regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

    print("Match at index % s, % s" % (match.start(), match.end()))

    # this will print "June 24"
    print("Full match: % s" % (match.group(0)))

    # this will print "June"
    print("Month: % s" % (match.group(1)))

    # this will print "24"
    print("Day: % s" % (match.group(2)))

else:
    print("The regex pattern does not match.")
`

```
# A Python program to demonstrate working of re.match().
```

```
import re
```

```

```

```
regex = r"([a-zA-Z]+) (\d+)"
```

```

```

```
match = re.search(regex, "I was born on June 24")
```

```

```

```
if match != None:
```

```

```

```
    print("Match at index % s, % s" % (match.start(), match.end()))
```

```

```

```
    # this will print "June 24"
```

```
    print("Full match: % s" % (match.group(0)))
```

```

```

```
    # this will print "June"
```

```
    print("Month: % s" % (match.group(1)))
```

```

```

```
    # this will print "24"
```

```
    print("Day: % s" % (match.group(2)))
```

```

```

```
else:
```

```
    print("The regex pattern does not match.")
```

**Output:**

```
Match at index 14, 21
Full match: June 24
Month: June
Day: 24

```

**Note:** For more information, refer  [Regular Expression in Python](https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/).

## Exception handling

Like other languages, Python also provides the runtime errors via [exception handling](https://www.geeksforgeeks.org/python-set-5-exception-handling/) method with the help of [try-except](https://www.geeksforgeeks.org/try-except-python/).

**How try-except works?**

- First try clause is executed i.e. the code between try and except clause.
- If there is no exception, then only try clause will run, except clause is finished.
- If any exception occurred, try clause will be skipped and except clause will run.
- If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception left unhandled, then the execution stops.
- A try statement can have more than one except clause.

**Code 1:** No exception, so try clause will run.

Python`
# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)
`

```
# Python code to illustrate
```

```
# working of try()
```

```
def divide(x, y):
```

```
    try:
```

```
        result = x // y
```

```
        print("Yeah ! Your answer is :", result)
```

```
    except ZeroDivisionError:
```

```
        print("Sorry ! You are dividing by zero ")
```

```

```

```
# Look at parameters and note the working of Program
```

```
divide(3, 2)
```

**Output:**

```
Yeah ! Your answer is : 1
```

**Code 2:** There is an exception so only except clause will run.

Python`
# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 0)
`

```
# Python code to illustrate
```

```
# working of try()
```

```
def divide(x, y):
```

```
    try:
```

```
        result = x // y
```

```
        print("Yeah ! Your answer is :", result)
```

```
    except:
```

```
        print("Sorry ! You are dividing by zero ")
```

```

```

```
# Look at parameters and note the working of Program
```

```
divide(3, 0)
```

**Output:**

```
Sorry ! You are dividing by zero

```

**Else Clause:** In python, you can also use else clause on try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

Python`
# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except:
        print("Sorry ! You are dividing by zero ")
    else:
        print("No exception raised")

# Look at parameters and note the working of Program
divide(3, 2)
`

```
# Python code to illustrate
```

```
# working of try()
```

```
def divide(x, y):
```

```
    try:
```

```
        result = x // y
```

```
        print("Yeah ! Your answer is :", result)
```

```
    except:
```

```
        print("Sorry ! You are dividing by zero ")
```

```
    else:
```

```
        print("No exception raised")
```

```

```

```
# Look at parameters and note the working of Program
```

```
divide(3, 2)
```

**Output:**

```
Yeah ! Your answer is : 1
No exception raised

```

**Raising Exception:** The raise statement allows the programmer to force a specific exception to occur. This must be either an exception instance or an exception class. To know more about the list of exception class  [click here](https://www.geeksforgeeks.org/built-exceptions-python/).

Python`
# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not
`

```
# Program to depict Raising Exception
```

```

```

```
try:
```

```
    raise NameError("Hi there")  # Raise Error
```

```
except NameError:
```

```
    print("An exception")
```

```
    raise  # To determine whether the exception was raised or not
```

**Output:**

```
Traceback (most recent call last):
  File "/home/4678cd3d633b2ddf9d19fde6283f987b.py", line 4, in
    raise NameError("Hi there")  # Raise Error
NameError: Hi there

```

**Note:** For more information, refer  [Python exception handling](https://www.geeksforgeeks.org/python-set-5-exception-handling/).

Comment


More info

[Advertise with us](https://www.geeksforgeeks.org/about/contact-us/?listicles)

[Next Article](https://www.geeksforgeeks.org/introduction-to-python/)

[Python Introduction](https://www.geeksforgeeks.org/introduction-to-python/)

[![author](https://media.geeksforgeeks.org/auth/profile/hafrnnqa652n4es4s95a)](https://www.geeksforgeeks.org/user/kumar_satyam/)

[kumar\_satyam](https://www.geeksforgeeks.org/user/kumar_satyam/)

Follow

13

Improve

Article Tags :

- [Python](https://www.geeksforgeeks.org/category/programming-language/python/)

Practice Tags :

- [python](https://www.geeksforgeeks.org/explore?category=python)

### Similar Reads

[How to Learn Python from Scratch in 2025\\
\\
\\
Python is a general-purpose high-level programming language and is widely used among the developersâ€™ community. Python was mainly developed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code.If you are new to programming and want to lea\\
\\
15+ min read](https://www.geeksforgeeks.org/how-to-learn-python-from-scratch/)
[Python Introduction\\
\\
\\
Python was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with focus on code readability and its syntax allows us to express concepts in fewer lines of code.Key Features of PythonPythonâ€™s simple and readable syntax makes it beginner-frien\\
\\
3 min read](https://www.geeksforgeeks.org/introduction-to-python/)
[Python 3 basics\\
\\
\\
Python was developed by Guido van Rossum in the early 1990s and its latest version is 3.11.0, we can simply call it Python3. Python 3.0 was released in 2008. and is interpreted language i.e it's not compiled and the interpreter will check the code line by line. This article can be used to learn the\\
\\
10 min read](https://www.geeksforgeeks.org/python-3-basics/)
[Important differences between Python 2.x and Python 3.x with examples\\
\\
\\
In this article, we will see some important differences between Python 2.x and Python 3.x with the help of some examples. Differences between Python 2.x and Python 3.x Here, we will see the differences in the following libraries and modules: Division operatorprint functionUnicodexrangeError Handling\\
\\
5 min read](https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/)
[Download and Install Python 3 Latest Version\\
\\
\\
If you have started learning of Python programming, then for practice, Python installation is mandatory, and if you are looking for a guide that teaches you the whole process from downloading Python to installing it, then you are on the right path.Here in this download and install Python guide, we h\\
\\
6 min read](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/)
[Statement, Indentation and Comment in Python\\
\\
\\
Here, we will discuss Statements in Python, Indentation in Python, and Comments in Python. We will also discuss different rules and examples for Python Statement, Python Indentation, Python Comment, and the Difference Between 'Docstrings' and 'Multi-line Comments. What is Statement in Python A Pytho\\
\\
7 min read](https://www.geeksforgeeks.org/statement-indentation-and-comment-in-python/)
[Python \| Set 2 (Variables, Expressions, Conditions and Functions)\\
\\
\\
Introduction to Python has been dealt with in this article. Now, let us begin with learning python. Running your First Code in Python Python programs are not compiled, rather they are interpreted. Now, let us move to writing python code and running it. Please make sure that python is installed on th\\
\\
3 min read](https://www.geeksforgeeks.org/python-set-2-variables-expressions-conditions-and-functions/)
[Global and Local Variables in Python\\
\\
\\
Python Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only insid\\
\\
7 min read](https://www.geeksforgeeks.org/global-local-variables-python/)
[Type Conversion in Python\\
\\
\\
Python defines type conversion functions to directly convert one data type to another which is useful in day-to-day and competitive programming. This article is aimed at providing information about certain conversion functions. There are two types of Type Conversion in Python: Python Implicit Type C\\
\\
5 min read](https://www.geeksforgeeks.org/type-conversion-in-python/)
[Private Variables in Python\\
\\
\\
Prerequisite: Underscore in PythonIn Python, there is no existence of â€œPrivateâ€ instance variables that cannot be accessed except inside an object. However, a convention is being followed by most Python code and coders i.e., a name prefixed with an underscore, For e.g. \_geek should be treated as a n\\
\\
3 min read](https://www.geeksforgeeks.org/private-variables-python/)

Like13

We use cookies to ensure you have the best browsing experience on our website. By using our site, you
acknowledge that you have read and understood our
[Cookie Policy](https://www.geeksforgeeks.org/cookie-policy/) &
[Privacy Policy](https://www.geeksforgeeks.org/privacy-policy/)
Got It !


![Lightbox](https://www.geeksforgeeks.org/how-to-learn-python-from-scratch/)

Improvement

Suggest changes

Suggest Changes

Help us improve. Share your suggestions to enhance the article. Contribute your expertise and make a difference in the GeeksforGeeks portal.

![geeksforgeeks-suggest-icon](https://media.geeksforgeeks.org/auth-dashboard-uploads/suggestChangeIcon.png)

Create Improvement

Enhance the article with your expertise. Contribute to the GeeksforGeeks community and help create better learning resources for all.

![geeksforgeeks-improvement-icon](https://media.geeksforgeeks.org/auth-dashboard-uploads/createImprovementIcon.png)

Suggest Changes

min 4 words, max Words Limit:1000

## Thank You!

Your suggestions are valuable to us.

## What kind of Experience do you want to share?

[Interview Experiences](https://write.geeksforgeeks.org/posts-new?cid=e8fc46fe-75e7-4a4b-be3c-0c862d655ed0) [Admission Experiences](https://write.geeksforgeeks.org/posts-new?cid=82536bdb-84e6-4661-87c3-e77c3ac04ede) [Career Journeys](https://write.geeksforgeeks.org/posts-new?cid=5219b0b2-7671-40a0-9bda-503e28a61c31) [Work Experiences](https://write.geeksforgeeks.org/posts-new?cid=22ae3354-15b6-4dd4-a5b4-5c7a105b8a8f) [Campus Experiences](https://write.geeksforgeeks.org/posts-new?cid=c5e1ac90-9490-440a-a5fa-6180c87ab8ae) [Competitive Exam Experiences](https://write.geeksforgeeks.org/posts-new?cid=5ebb8fe9-b980-4891-af07-f2d62a9735f2)

[iframe](https://td.doubleclick.net/td/rul/796001856?random=1748613561645&cv=11&fst=1748613561645&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v877914216za200zb884918195&gcd=13l3l3R3l5l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fhow-to-learn-python-from-scratch%2F&hn=www.googleadservices.com&frm=0&tiba=How%20to%20Learn%20Python%20from%20Scratch%20in%202025%20%7C%20GeeksforGeeks&npa=0&pscdl=noapi&auid=1989085311.1748613562&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)

Login Modal \| GeeksforGeeks

# Log in

New user ?Register Now

Continue with Google

or

Username or Email

Password

Remember me

Forgot Password

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LexF0sUAAAAADiQjz9BMiSrqplrItl-tWYDSfWa&co=aHR0cHM6Ly93d3cuZ2Vla3Nmb3JnZWVrcy5vcmc6NDQz&hl=en&v=GUGrl5YkSwqiWrzO3ShIKDlu&size=normal&cb=47j9xnp66iu8)

Sign In

By creating this account, you agree to our [Privacy Policy](https://www.geeksforgeeks.org/privacy-policy/) & [Cookie Policy.](https://www.geeksforgeeks.org/legal/privacy-policy/#:~:text=the%20appropriate%20measures.-,COOKIE%20POLICY,-A%20cookie%20is)

# Create Account

Already have an account ?Log in

Continue with Google

or

Username or Email

Password

Institution / Organization

```

```

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LexF0sUAAAAADiQjz9BMiSrqplrItl-tWYDSfWa&co=aHR0cHM6Ly93d3cuZ2Vla3Nmb3JnZWVrcy5vcmc6NDQz&hl=en&v=GUGrl5YkSwqiWrzO3ShIKDlu&size=normal&cb=xcrswxnzm5ur)

Sign Up

\*Please enter your email address or userHandle.

Back to Login

Reset Password

[iframe](about:blank)[iframe](about:blank)[iframe](about:blank)[iframe](about:blank)[iframe](about:blank)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdMFNUZAAAAAIuRtzg0piOT-qXCbDF-iQiUi9KY&co=aHR0cHM6Ly93d3cuZ2Vla3Nmb3JnZWVrcy5vcmc6NDQz&hl=en&v=GUGrl5YkSwqiWrzO3ShIKDlu&size=invisible&cb=eq0sgtxdgxiu)

[iframe](https://gum.criteo.com/syncframe?origin=publishertagids&topUrl=www.geeksforgeeks.org&gdpr=0&gdpr_consent=&gpp=&gpp_sid=-1#{"bundle":{"value":"rbsAy19qeG9UY2VOM3JWRDZtendBMU5MampodXQwcDdPTyUyRjNMNkptc1RrNG9kMEQzNCUyRm9ub0dmQ21GOUFFWmFkQ1dqakhPeDE5JTJGbGwxaXdmbWdpQUlJQkoyUXRLJTJCQUJ4dDNZeVdQZHY4aWJDSmhBU3Q4TGhWWkNwYnduNjFYOHZ2c3pN","origin":3},"optout":{"value":false,"origin":0},"tld":"geeksforgeeks.org","topUrl":"www.geeksforgeeks.org","version":160,"origin":"publishertagids","requestId":"0.21743845322976818"})

[iframe](https://www.google.com/recaptcha/api2/bframe?hl=en&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6LexF0sUAAAAADiQjz9BMiSrqplrItl-tWYDSfWa)

[iframe](https://www.google.com/recaptcha/api2/bframe?hl=en&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6LexF0sUAAAAADiQjz9BMiSrqplrItl-tWYDSfWa)

[iframe](https://ep2.adtrafficquality.google/sodar/sodar2/237/runner.html)[iframe](https://www.google.com/recaptcha/api2/aframe)[iframe](https://securepubads.g.doubleclick.net/static/topics/topics_frame.html)