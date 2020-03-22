## Introduction
- Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
- Operators: Membership, Identity
- Built-In Functions or Methods

## Lists and Membership Operators
#### Lists (mutable and ordered) x Strings (immutable and ordered)
```python
list_of_random_things = [1, 3.4, 'a string', True]

>>> list_of_random_things[-1] 
True
>>> list_of_random_things[-2] 
a string

>>> list_of_random_things[1:2]
[3.4]
>>> list_of_random_things[:2]
[1, 3.4]
>>> list_of_random_things[1:]
[3.4, 'a string', True]

>>> 'in' in 'this is a string'
True
>>> 5 not in [1, 2, 3, 4, 6]
True

my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
>>> print(my_lst)
['one', 2, 3, 4, 5]

greeting = "Hello there"
greeting[0] = 'M' #error

new_str = "\n".join(["fore", "aft", "starboard", "port"])
>>> print(new_str)
fore
aft
starboard
port

letters = ['a', 'b', 'c', 'd']
letters.append('z')
>>> print(letters)
['a', 'b', 'c', 'd', 'z']

empty_list = []
empty_list = list()
```
- len() -> returns how many elements are in a list.
- max() -> returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The max function is undefined for lists that contain elements from different, incomparable types.
- min() -> returns the smallest element in a list.
- sorted() -> returns a copy of a list in order from smallest to largest, leaving the list unchanged.
- join() -> takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
- append() -> adds an element to the end of a list.

## Tuples
#### Tuples (immutable and ordered)
```python
location = (13.4125, 103.866667)
>>> print("Latitude:", location[0])
>>> print("Longitude:", location[1])

dimensions = 52, 40, 100
length, width, height = dimensions #tuple unpacking
>>> print("The dimensions are {} x {} x {}".format(length, width, height))

empty_tuple = ()
empty_tuple = tuple()
```

## Sets
#### Sets (mutable and unordered)
```python
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
>>> print(unique_nums)
{1, 2, 3, 6}

fruit = {"apple", "banana", "orange", "grapefruit"}
>>> print("watermelon" in fruit)
False
fruit.add("watermelon")
>>> print(fruit)
{'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
>>> print(fruit.pop())
"grapefruit"
>>>print(fruit)
{'orange', 'watermelon', 'banana', 'apple'}

empty_set = set()
```
- add() - add elements to sets.
- pop() - random element is removed.
- Union, intersection, and difference are easy to perform with sets

## Dictionaries and Identity Operators
#### Dictionaries ((im)mutable, unordered, and mappings of unique keys)
```python
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
>>> print(elements["helium"])
2
elements["lithium"] = 3  #insert "lithium" with a value of 3 into the dictionary
>>> print("carbon" in elements)
True
>>> print(elements.get("dilithium"))
None #can crash
n = elements.get("dilithium")
>>> print(n is None)
True
>>> print(n is not None)
False
>>> print(elements.get('kryptonite', 'There\'s no such element!'))
"There's no such element!"

empty_dict = {}
empty_dict = dict()
```
- Any immutable object (such as an integer, boolean, string, tuple) is hashable (can be used by dictionaries to track unique keys and sets to track unique values)

## Compound Data Structures
```python
elements = {"hydrogen": {"number": 1, 
                         "weight": 1.00794, 
                         "symbol": "H"},
              "helium": {"number": 2, 
                         "weight": 4.002602, 
                         "symbol": "He"}}
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
>>> print('elements = ', elements)
elements = {"hydrogen": {"number": 1,
                          "weight": 1.00794,
                          "symbol": 'H'},
               "helium": {"number": 2,
                          "weight": 4.002602,
                          "symbol": "He"}, 
               "oxygen": {"number": 8, 
                          "weight": 15.999, 
                          "symbol": "O"}}
```





