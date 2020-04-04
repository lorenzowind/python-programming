## [Iterators and Generators](https://docs.python.org/3/tutorial/classes.html)
- Iterables are objects that can return one of their elements at a time, such as a list. Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator
- An iterator is an object that represents a stream of data. This is different from a list, which is also an iterable, but is not an iterator because it is not a stream of data    
- Generators are a simple way to create iterators using functions. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. You can also define iterators using classes
```python
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for x in my_range(5):
    print(x)
0 1 2 3 4
```

## Generator Expressions
```python
sq_list = [x**2 for x in range(10)] #produces a list of squares

sq_iterator = (x**2 for x in range(10)) #produces an iterator of squares
```