## Introduction
- Data Types: Integers, Floats, Booleans, Strings
- Operators: Arithmetic, Assignment, Comparison, Logical
- Built-In Functions, Type Conversion
- Whitespace and Style Guidelines

## [Arithmetic Operators](http://mathforum.org/dr.math/faq/faq.order.operations.html)
- (+) Addition
- (-) Subtraction
- (*) Multiplication
- (/) Division
- (%) Mod (the remainder after dividing)
- (**) Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
- (//) Divides and rounds down to the nearest integer
- [Bitwise](https://wiki.python.org/moin/BitwiseOperators)

## Variables and Assignment Operators
```python
x, y, z = 3, 4, 5

my_height = 58
```
- [Reserved words](https://pentangle.net/python/handbook/node52.html)
- [Assignment operators](https://www.programiz.com/python-programming/operators)

## Integers and Floats
```python
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0

>>> print(.1 + .1 + .1 == .3)
False
```
- [Python Developers Guide](https://www.python.org/dev/peps/pep-0008/)
- [pep8 extension](https://atom.io/packages/linter-python-pep8)
- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

## Booleans, Comparisons Operators, and Logical Operators
- and -> Evaluates if all provided statements are True
- or -> Evaluates if at least one of many statements is True
- not -> Flips the Bool Value

## Strings
```python
>>> my_string = 'this is a string!'
>>> my_string2 = "this is also a string!!!"

>>> this_string = 'Simon\'s skateboard is in the garage.'

>>> print(first_word * 5)
HelloHelloHelloHelloHello

>>> first_word[0]
H
```
- [len()](https://docs.python.org/2/library/functions.html#len) -> is a built-in Python function that returns the length of an object, like a string

## Type and Type Conversion
```python
string = "10"
string_2 = "20"
result = int(string) + int(string_2)
>>> print(str(result))
"30"
```
- type() -> can be used to check the data type of any variable

## [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
```python
my_string = "sebastian thrun"

>>> my_string.islower()
True
>>> my_string.count('a')
2
>>> my_string.find('a')
3

animal = "dog"
action = "bite"
>>> print("Does your {} {}?".format(animal, action))
"Does your dog bite?"

new_str = "The cow jumped over the moon."
>>> new_str.split()
['The', 'cow', 'jumped', 'over', 'the', 'moon.']
```
- [format()](https://docs.python.org/3.6/library/string.html#format-string-syntax) -> replacements in the statement
- split() -> returns a data container called a list that contains the words from the input string. The split method has two additional arguments (sep and maxsplit). The sep argument stands for "separator". The maxsplit argument provides the maximum number of splits.