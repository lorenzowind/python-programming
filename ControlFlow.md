## Introduction
- Conditional Statements
- Boolean Expressions
- For and While Loops
- Break and Continue
- Zip and Enumerate
- List Comprehensions

## Conditional Statements
```python
if ... :
    ...
elif ... :
    ...
else:
    ...
```
- (Indentantion)[https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces]

## Boolean Expressions
```python
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
```
#### Considered False in Python
- constants defined to be false: `None` and `False`
- zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- empty sequences and collections: `'""`, `()`, `[]`, `{}`, `set()`, `range(0)`

## For Loops
```python
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)

for i in range(3):
    print("Hello!")

range(start=0, stop, step=1)

for index in range(len(cities)):
    cities[index] = cities[index].title()
```

### Building Dictionaries
```python
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
```

#### Iterating
```python
for key in cast:
    print(key)

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
```

## While Loops
```python
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand)  < 17:
    hand.append(card_deck.pop())
```

## [For Loops vs. While Loops](https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python)
- for loops are ideal when the number of iterations is known or finite.
    - When you have an iterable collection (list, string, set, tuple, dictionary)
    `for name in names:`
    - When you want to iterate through a loop for a definite number of times, using range()
    `for i in range(5):`
- while loops are ideal when the iterations need to continue until a condition is met.
    - When you want to use comparison operators
    `while count <= 100:`
    - When you want to loop based on receiving specific user input.
    `while user_input == 'y':`

## Break, Continue
- `break` terminates a loop
- `continue` skips one iteration of a loop

## Zip and Enumerate
- `zip` returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables
```python
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
```
- `enumerate` is a built in function that returns an iterator of tuples containing indices and values of a list.
```python
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
```

## List Comprehensions
```python
capitalized_cities = [city.title() for city in cities]

squares = [x**2 for x in range(9) if x % 2 == 0]

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
```