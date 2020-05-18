## Linear Search - O(n)

## Binary Search - O(log(n))

### n * (1/2)^s = 1 -> log(n) = s
- s is the number of steps and n is the array size

### Implementation
```python
def binary_search(array, target):
    '''
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_index = 0
    end_index = len(array) - 1
    
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2 # integer division in Python 3
        
        mid_element = array[mid_index]
        
        if target == mid_element: # we have found the element
            return mid_index
        
        elif target < mid_element: # the target is less than mid element
            end_index = mid_index - 1 # we will only search in the left half
        
        else: # the target is greater than mid element
            start_index = mid_element + 1 # we will search only in the right half
    
    return -1

def binary_search_recursive(array, target):
    '''
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
```
### Binary search variation
```python
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)

def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index

# Native implementation of binary search in the `contains` function.
def contains(target, source):
    if len(source) == 0:
        return False
    center = (len(source)-1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains(target, source[center+1:])
    else:
        return contains(target, source[:center])
```

## [Comparison of computational complexity](https://commons.wikimedia.org/wiki/File:Comparison_computational_complexity.svg)

### n! > 2^n > n^2 > n * log(n) > n > sqrt(2) > log(n) > 1

## Tries

### Trie using a class
```python
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word
```

### Trie using default dictionary
```python
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

            current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word
```

## Priority Queue
- It is similar to a regular queue, except that each element in the queue has a priority associated with it. A regular queue is a FIFO data structure, meaning that the first element to be added to the queue is also the first to be removed.
- With a priority queue, this order of removal is instead based on the priority. Depending on how we choose to set up the priority queue, we either remove the element with the most priority, or an element of the least priority.

## Heaps
- Complete Binary Tree: A complete binary tree is a special type of binary tree in which all levels must be filled except for the last level. Moreover, in the last level, the elements must be filled from left to right.
1. Max number of nodes in hth level =  2(ℎ−1) 
2. Also, we can calculate the max number of nodes from 1st level to hth level =  2ℎ−1 
3. Similarly, we can calculate the min number of nodes from 1st level to hth level = 2(ℎ−1)
4. Insert and remove operation will have the time complexity O(log(n)) = height h

- Heap Order Property:
1. Min Heap - In the case of min heaps, for each node, the parent node must be smaller than both the child nodes. It's okay even if one or both of the child nodes do not exists. However if they do exist, the value of the parent node must be smaller. Also note that it does not matter if the left node is greater than the right node or vice versa. The only important condition is that the root node must be smaller than both it's child nodes
2. Max Heap - For max heaps, this condition is exactly reversed. For each node, the value of the parent node must be larger than both the child nodes.

### Heaps with arrays
```python
class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        self.cbt[self.next_index] = data
        
        current_index = self.next_index
        
        if current_index >= 1:
            parent_index = (current_index - 1) // 2

            while self.cbt[current_index] < self.cbt[parent_index]:
                current_index, parent_index = self.up_heapfy(current_index, parent_index)

        self.next_index += 1

        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        """
        Remove and return the element at the top of the heap
        """
        if self.size() == 0:
            return None
        
        to_remove = self.cbt[0]
        
        self.cbt[0] = self.cbt[self.next_index - 1]
        
        current_index = 0
        left_child_index = self.cbt[2 * (current_index + 1)] 
        right_child_index = self.cbt[2 * (current_index + 2)]
        
        while True:
            
            if left_child_index is not None and right_child_index is not None:
                if self.cbt[current_index] > left_child_index or self.cbt[current_index] > right_child_index:
                    index = min(left_child_index, right_child_index)
                    current_index, left_child_index, right_child_index = self.down_heapfy(current_index, index)
                else:
                    break
            
            elif left_child_index is not None and right_child_index is None:
                if self.cbt[current_index] > left_child_index:
                    current_index, left_child_index, right_child_index = self.down_heapfy(current_index, left_child_index)
                else:
                    break
                    
            elif left_child_index is None and right_child_index is not None:
                if self.cbt[current_index] > right_child_index:
                    current_index, left_child_index, right_child_index = self.down_heapfy(current_index, right_child_index)
                else:
                    break
            
            else:
                break

        self.next_index -= 1
        
        return to_remove
    
    def down_heapfy(self, current_index, index):
        aux = self.cbt[index]
        self.cbt[index] = self.cbt[current_index]
        self.cbt[current_index] = aux
        
        current_index = index
        left_child_index = self.cbt[2 * (current_index + 1)] 
        right_child_index = self.cbt[2 * (current_index + 2)]
        
        return current_index, left_child_index, right_child_index

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def up_heapfy(self, current_index, parent_index):
        aux = self.cbt[parent_index]
        self.cbt[parent_index] = self.cbt[current_index]
        self.cbt[current_index] = aux

        parent_index = (current_index - 1) // 2

        return current_index, parent_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]
```

## Red Black Tree
1. All nodes have a color
2. All nodes have two children (use NULL nodes)
3. All NULL nodes are colored black
4. If a node is red, its children must be black
5. The root node must be black (optional)
6. Every path to its descendant NULL nodes must contain the same number of black nodes

### Implementation
```python
class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color
        
    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')
        
    def __iter__(self):
        yield from self.root.__iter__()
        
    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):    
        # Case 1
        if node.parent == None:
            return
        
        # Case 2
        if node.parent.color == 'black':
            return
        
        # Case 3
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))
        
        gp = grandparent(node)        
        # Small change, if there is no grandparent, cases 4 and 5
        # won't apply
        if gp == None:
            return
        
        # Case 4
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # Case 5
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p
```