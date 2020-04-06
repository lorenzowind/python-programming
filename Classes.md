## Overview
- A class is a structure in object-oriented programming that allows functions and related data to be grouped together
- an important concept is `self`, which is used to reference a class instance's own variables and functions from within the class definition
- Another important and commonly used function definition is the class initializer, `def __init__(self)`. The body of the initializer is where instance variable definitions should be added, and the initializer initializes all the variables once an instance of the class is created

## Example
```python
class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name
```