## Implementing a stack using an array
### Functionality
- `push` - adds an item to the top of the stack
- `pop` - removes an item from the top of the stack (and returns the value of that item)
- `size` - returns the size of the stack
- `top` - returns the value of the item at the top of stack (without removing that item)
- `is_empty` - returns True if the stack is empty and False otherwise
### Implementation  
```python
class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
```
### `push` method
```python
def push(self, data):
    self.arr[self.next_index] = data
    self.next_index += 1
    self.num_elements += 1
```
### Handle full capacity
```python
def push(self, data):
    if self.next_index == len(self.arr):
        print("Out of space! Increasing array capacity ...")
        self._handle_stack_capacity_full()
    
    self.arr[self.next_index] = data
    self.next_index += 1
    self.num_elements += 1

def _handle_stack_capacity_full(self):
    old_arr = self.arr

    self.arr = [0 for _ in range( 2* len(old_arr))]
    for index, element in enumerate(old_arr):
        self.arr[index] = element
```
### `size` and `is_empty` methods
```python
def size(self):
    return self.num_elements

def is_empty(self):
    return self.num_elements == 0
```
### `pop` method
```python
def pop(self):
    if self.is_empty():
        self.next_index = 0
        return None
    self.next_index -= 1
    self.num_elements -= 1
    return self.arr[self.next_index]
```

## Implementing a stack using a Linked List
### Implementation
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0
```
### `push` method
```python
def push(self, value):
    new_node = Node(value)        
    # if stack is empty
    if self.head is None:
        self.head = new_node
    else:
        new_node.next = self.head # place the new node at the head of the linked list (top)
        self.head = new_node

    self.num_elements += 1
```
### `size` and `is_empty` methods
```python
def size(self):
    return self.num_elements

def is_empty(self):
    return self.num_elements == 0
```
### `pop` method
```python
def pop(self):
    if self.is_empty():
        return
    
    value = self.head.value # copy data to a local variable
    self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
    self.num_elements -= 1
    return value
```
## Stack in python
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
```
### Reverse a stack
```python
def reverse_stack(stack):
    holder_stack = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)
    _reverse_stack_recursion(stack, holder_stack)

def _reverse_stack_recursion(stack, holder_stack):
    if holder_stack.is_empty():
        return
    popped_element = holder_stack.pop()
    _reverse_stack_recursion(stack, holder_stack)
    stack.push(popped_element)

```

## Implementing a queue using an array
### Functionality
- `enqueue` - adds data to the back of the queue
- `dequeue` - removes data from the front of the queue
- `front` - returns the element at the front of the queue
- `size` - returns the number of elements present in the queue
- `is_empty` - returns `True` if there are no elements in the queue, and `False` otherwise
- `_handle_full_capacity` - increases the capacity of the array, for cases in which the queue would otherwise overflow
### Implementation
```python
class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
```
### `enqueue` method
```python
def enqueue(self, value):
    # enqueue new element
    self.arr[self.next_index] = value
    self.queue_size += 1
    self.next_index = (self.next_index + 1) % len(self.arr)
    if self.front_index == -1:
        self.front_index = 0
```
### `size`, `is_empty`, and `front` methods
```python
def size(self):
    return self.queue_size

def is_empty(self):
    return self.size() == 0

def front(self):
    # check if queue is empty
    if self.is_empty():
        return None
    return self.arr[self.front_index]
```
### `dequeue` method
```python
def dequeue(self):
    # check if queue is empty
    if self.is_empty():
        self.front_index = -1   # resetting pointers
        self.next_index = 0
        return None

    # dequeue front element
    value = self.arr[self.front_index]
    self.front_index = (self.front_index + 1) % len(self.arr)
    self.queue_size -= 1
    return value
```
### Handle full capacity
```python
def enqueue(self, value):
    # if queue is already full --> increase capacity
    if self.queue_size == len(self.arr):
        self._handle_queue_capacity_full()

    # enqueue new element
    self.arr[self.next_index] = value
    self.queue_size += 1
    self.next_index = (self.next_index + 1) % len(self.arr)
    if self.front_index == -1:
        self.front_index = 0

def _handle_queue_capacity_full(self):
    old_arr = self.arr
    self.arr = [0 for _ in range(2 * len(old_arr))]

    index = 0

    # copy all elements from front of queue (front-index) until end
    for i in range(self.front_index, len(old_arr)):
        self.arr[index] = old_arr[i]
        index += 1

    # case: when front-index is ahead of next index
    for i in range(0, self.front_index):
        self.arr[index] = old_arr[i]
        index += 1

    # reset pointers
    self.front_index = 0
    self.next_index = index
```
## Implementing a queue using a Linked List
### implementation
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
```
### `enqueue` method
```python
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
```
### `size` and `is_empty` methods
```python
def size(self):
        return self.num_elements
    
def is_empty(self):
    return self.num_elements == 0
```
### `Dequeue` method
```python
def dequeue(self):
    if self.is_empty():
        return None
    value = self.head.value # copy the value to a local variable
    self.head = self.head.next # shift the head (i.e., the front of the queue)
    self.num_elements -= 1
    return value
```

## Queue using a stack
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        self.instorage=Stack()
        self.outstorage=Stack()
        
    def size(self):
         return self.outstorage.size() + self.instorage.size()
        
    def enqueue(self,item):
        self.instorage.push(item)
        
    def dequeue(self):
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()
    
```
## Queue in python
```python
class Queue:
    def __init__(self):
         self.storage = []
    
    def size(self):
         return len(self.storage)
    
    def enqueue(self, item):
         self.storage.append(item)

    def dequeue(self):
         return self.storage.pop(0)
```
### Reverse a queue
```python
def reverse_queue(queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())
```