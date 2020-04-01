## Introduction
- Defining Functions
- Variable Scope
- Documentation
- Lambda Expressions
- Iterators and Generators

## Defining Functions
```python
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
cylinder_volume(10, 3)

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
cylinder_volume(10, 7) #the 7 will simply overwrite the default value of 5
cylinder_volume(height=10, radius=7)
```

## Variable Scope
```python
word = "hello"
def some_function():
    print(word)
some_function()

egg_count = 0
def buy_eggs():
    egg_count += 12 #error
buy_eggs()

str1 = 'Functions are important programming concepts.'
def print_fn():
    str1 = 'Variable scope is an important concept.' #works fine
    print(str1)
print_fn()
```

## [Documentation](https://www.python.org/dev/peps/pep-0257/)
```python
def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area

def population_density(population, land_area):
    """Calculate the population density of an area.
    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.
    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area
```

## Lambda Expressions
```python
multiply = lambda x, y: x * y
multiply(4, 7)

numbers = [[34, 63, 88, 71, 29],
            [90, 78, 51, 27, 45],
            [63, 37, 85, 46, 22],
            [51, 22, 34, 11, 18]]
averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

cities = ["New York City", "Los Angeles",   
            "Chicago", "Mountain View", 
            "Denver", "Boston"]
short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
```
#### map()
- Is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable
#### filter()
- is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True

## [yield and generators](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

## [How to write a function](https://www.youtube.com/watch?v=rrBJVMyD-Gs&feature=youtu.be)