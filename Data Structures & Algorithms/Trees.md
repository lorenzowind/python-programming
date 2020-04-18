## Node class
```python
class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
    
    def get_left_child(self):
        return self.left
    
    def set_left_child(self, node):
        self.left = node
    
    def get_right_child(self):
        return self.right
    
    def set_right_child(self, node):
        self.right = node
        
    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None
```

## Binary Tree class
```python
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root
```

## Depth First Search (DFS)
### Stack class
```python
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
```
### State class
```python
class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
```
### Pre-order with Stack
```python
def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0

    while(node):
        count +=1

        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
            
    return visit_order
```
### Pre-order with recursion
```python
def pre_order(tree):
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):
        if node:
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())
    
    traverse(root)
    return visit_order
```
### In-order with recursion
```python
def in_order(tree):
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child())
    
    traverse(root)
    return visit_order
```
### Post-order with recursion
```python
def post_order(tree):
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visit_order.append(node.get_value())
    
    traverse(root)
    return visit_order
```

## Breadth First Search (DFS)
### Queue class
```python
from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
```
### Algorithm
```python
def bfs(tree):
    visit_order = list()
    q = Queue()
    q.enq(tree.get_root())
    while len(q) != 0:
        node = q.deq()
        visit_order.append(node)
        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())
    return visit_order
```

## Binary Search Trees
### Insert with loop
```python
def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

def insert_with_loop(self,new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        while True:
            comparison = self.compare(node, new_node)
            if comparison == 0:
                node.set_value(new_node.get_value())
                break
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break
```
### Insert with recursion
```python
def insert_with_recursion(self,value):
        if self.get_root() == None:
            self.set_root(value)
            return
        self.insert_recursively(self.get_root(), Node(value))
        pass
    
def insert_recursively(self, node, new_node):
    comparison = self.compare(node, new_node)
    if comparison == 0:
        node.set_value(new_node.get_value())
    elif comparison == -1:
        if node.has_left_child():
            self.insert_recursively(node.get_left_child(), new_node)
        else:
            node.set_left_child(new_node)
    else:
        if node.has_right_child():
            self.insert_recursively(node.get_right_child(), new_node)
        else:
            node.set_right_child(new_node)
```
### Search
```python
def search(self,value):
    new_node = Node(value)
    node = self.get_root()
    if node is None:
        return False
    while True:
        comparison = self.compare(node, new_node)
        if comparison == 0:
            return True
        elif comparison == -1:
            if node.has_left_child():
                node = node.get_left_child()
            else:
                return False
        else:
            if node.has_right_child():
                node = node.get_right_child()
            else:
                return False
```
### Delete
```python
def delete(self, value):
    node_to_delete = Node(value)
    node = self.get_root()
    self.delete_recursively(node, node_to_delete)
    
def delete_recursively(self, node, node_to_delete):
    if node is None:
        return node
    comparison = self.compare(node, node_to_delete) 
    if comparison == -1: 
        node.set_left_child(self.delete_recursively(node.get_left_child(), node_to_delete)) 
    elif comparison == 1: 
        node.set_right_child(self.delete_recursively(node.get_right_child(), node_to_delete))
    else:  
        if node.get_left_child() is None: 
            temp = node.get_right_child()  
            node = None 
            return temp  
        elif node.get_right_child() is None: 
            temp = node.get_left_child()
            root = None
            return temp 
        temp = self.minValueNode(node.get_right_child())  
        node.set_value(temp.get_value())
        node.set_right_child(self.delete_recursively(node.get_right_child(), temp))
    return node
    
def minValueNode(self, node): 
    current = node 
    while current.has_left_child(): 
        current = current.get_left_child()  
    return current 
```

## Diameter of a Binary Tree
### Binary Tree class
```python
class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
```
### Convert an array to a Binary Tree
```python
from queue import Queue
def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root
```
### Algorithm
```python
def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]
    
def diameter_of_binary_tree_func(root):
    """
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root:
    :return: [height, diameter]
    """
    if root is None:
        return 0, 0

    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter
``` 

## Path from root to node
```python
def path_from_root_to_node(root, data):
    """
    Assuming data as input to find the node
    The solution can be easily changed to find a node instead of data
    :param data:
    :return:
    """
    output = path_from_node_to_root(root, data)
    return list(reversed(output))

def path_from_node_to_root(root, data):
    if root is None:
        return None

    elif root.data == data:
        return [data]

    left_answer = path_from_node_to_root(root.left, data)
    if left_answer is not None:
        left_answer.append(root.data)
        return left_answer

    right_answer = path_from_node_to_root(root.right, data)
    if right_answer is not None:
        right_answer.append(root.data)
        return right_answer
    return None
```