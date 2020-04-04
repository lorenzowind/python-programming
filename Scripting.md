## Introduction
- Python Installation and Environment Setup
- Running and Editing Python Scripts
- Interacting with User Input
- Handling Exceptions
- Reading and Writing Files
- Importing Local, Standard, and Third-Party Modules
- Experimenting with an Interpreter

## Python Installation
```
python --version
```
- [Shell Workshop](https://www.udacity.com/course/shell-workshop--ud206)
- [Anaconda - Python Data Science Platform](https://www.anaconda.com/distribution/#windows)
    - [Guide](https://classroom.udacity.com/courses/ud1111)
    - [Tutorial](https://get.anaconda.com/distribution/tutorial/)
- [Managing environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Atom](https://atom.io/)

## Running and Editing
```
python first_script.py

python
```

## Raw Input
```python
num = int(input("Enter an integer"))
print("hello" * num)

result = eval(input("Enter an expression: ")) #if inputs 2 * 3 =, this outputs 6
print(result)
```

## Errors and Excpetions
- Syntax errors:  occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python
- Exceptions: occur when unexpected things happen during execution of a program, even if the code is syntactically correct

### Handling Errors
- `try`: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
- `except`: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
- `else`: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
- `finally`: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

### [Specifying Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
```python
try:
    # some code
except ValueError:
    # some code

try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
```

## [Reading and Writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
```python
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r')) #too many open files
    print(i)

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

#We're the knights of the round table
#We dance whenever we're able
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())
print(camelot_lines)
["We're the knights of the round table", "We dance whenever we're able"]
```
- If you open an existing file in writing mode, any content that it had contained previously will be deleted. If you're interested in adding to an existing file, without deleting its content, you should use the append ('a') mode instead of write.
- The with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file

## Importing Local Scripts
```python
import useful_functions
useful_functions.add_five([1, 2, 3, 4])

import useful_functions as uf
uf.add_five([1, 2, 3, 4])
```
- To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an if `__name__` == `"__main__"` block. Or alternatively, include them in a function called main() and call this in the if main block.

## [The Standard Library](https://docs.python.org/3/library/)
```python
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
#def generate_password():
    #return ''.join(random.sample(word_list,3))
```
- [New modules](https://pymotw.com/3/)
- [Math](https://docs.python.org/3.6/library/math.html)
- [Random](https://docs.python.org/3/library/random.html)
- `csv`: very convenient for reading and writing csv files
- `collections`: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
- `random`: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
- `string`: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
- `re`: pattern-matching in strings via regular expressions
- `math`: some standard mathematical functions
- `os`: interacting with operating systems
- `os.path`: submodule of os for manipulating path names
- `sys`: work directly with the Python interpreter
- `json`: good for reading and writing json files (good for web work)

## Techniques for Importing Modules
```python
from module_name import object_name

from module_name import first_object, second_object

import module_name as new_name

from module_name import object_name as new_name

from module_name import * #do not do this
import module_name #do this

import package_name.submodule_name
```

## Third-Party Libraries
- To install a package using pip, just enter "pip install" followed by the name of the package in your command line like this: `pip install package_name`

#### Using a `requirements.txt` File
```
pip install -r requirements.txt
```
- Larger Python programs might depend on dozens of third party packages. To make it easier to share these programs, programmers often list a project's dependencies in a file called requirements.txt

#### Useful Third-Party Packages
- IPython - A better interactive Python interpreter
- requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
- Flask - a lightweight framework for making web applications and APIs.
- Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
- Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
- pytest - extends Python's builtin assertions and unittest module.
- PyYAML - For reading and writing YAML files.
- NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
- pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
- matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
- ggplot - Another 2D plotting library, based on R's ggplot2 library.
- Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- pyglet - A cross-platform application framework intended for game development.
- Pygame - A set of Python modules designed for writing games.
- pytz - World Timezone Definitions for Python

## Interpreter
```
>>> type(5.23)
<class 'float'>

>>> def cylinder_volume(height, radius):
...         pi = 3.14159
...         return height * pi * radius ** 2

>>> cylinder_volume(10, 3)
282.7431
```
- Entering the command `python` in terminal
- To quit use exit() or ctrl-Z

#### [IPython](https://ipython.org/ipython-doc/3/interactive/tutorial.html)
- tab completion
- `?` for details about an object
- `!` to execute system shell commands
- syntax highlighting!

## Online Resources
1. The Python Tutorial - This section of the official documentation surveys Python's syntax and standard library
2. The Python Language and Library References - The Language Reference and Library Reference are more technical than the tutorial, but they are the definitive sources of truth.
3. Third-Party Library Documentation - Third-party libraries publish their documentation on their own websites, and often times at https://readthedocs.org/.
4. The websites and blogs of prominent experts - The previous resources are primary sources, meaning that they are documentation from the same people who wrote the code being documented. 
5. StackOverflow - This is a good place to find out more about your question or discover alternative search terms
6. Bug Trackers - Sometimes you'll encounter a problem so rare, or so new, that no one has addressed it on StackOverflow.
7. Random Web Forums - Sometimes your search yields references to forums that haven't been active since 2004, or some similarly ancient time.

#### Seven steps to interviews
- Clarifying the question
- Generating inputs & outputs
- Generating test cases
- Brainstorming
- Runtime Analysis
- Coding
- Debugging