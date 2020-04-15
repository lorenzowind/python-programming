## Introduction
- Recursion is a technique for solving problems where the solution to a particular problem depends on the solution to a smaller instance of the same problem

## Example `power_of_2`
```python
def power_of_2(n):
    if n == 0:
        return 1
    
    return 2 * power_of_2(n - 1)

print(power_of_2(5))
```

## Call Stack - has a limit

## Slicing
### Example `sum_array` without slincing
```python
def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]
    
    return array[0] + sum_array(array[1:])

arr = [1, 2, 3, 4]
print(sum_array(arr))
```
### Example `sum_array_index` with slicing
```python
def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]
    
    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))
```
## Factorial function
```python
def factorial(n):
    """
    Calculate n!
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
	if n == 0:
        return 1  # by definition of 0!
    return n * factorial(n-1)
```

## Reverse a String
```python
def reverse_string(input):
    """
    Return reversed input string
    Args:
      input(str): string to be reversed
    Returns:
      a string that us reversed of input
    """
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        reversed_substring = reverse_string(sub_string)
        return reversed_substring + first_char
```

## Palindrome checking
```python
def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.
    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]
        # sub_input is input with first and last char removed
        sub_input = input[1:-1]
        return (first_char == last_char) and is_palindrome(sub_input)
```

## List Permutations
```python
import copy

def permute(l):
    """
    Return a list of permutations
    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]
    Args:
      l(list): list of items to be permuted
    Returns:
      list of permutation with each permuted item be represented by a list
    """
    perm = []
    if len(l) == 0:
        perm.append([])
    else:
        first_element = l[0]
        #print('first_element: ', first_element)
        after_first = slice(1, None)
        #print('after_first: ', after_first)
        sub_permutes = permute(l[after_first])
        #print('sub-permuts: ', sub_permutes)
        for p in sub_permutes:
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                #print('r: ', r)
                r.insert(j, first_element)
                #print('r: ', r)
                perm.append(r)
                #print('perm: ', perm)
    return perm
```

## String Permutation
```python
def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    """
    perm = []
    if len(string) == 0:
        perm.append('') 
    else:
        first_element = string[0]
        sub_elements = permutations(string[1:])
        for p in sub_elements:
            for j in range(0, len(string)):
                r = p[0:j] + first_element + p[j:]
                perm.append(r)
    return perm
```

## [The call stack and recursion](http://pythontutor.com/)

## Binary search
```python
def binary_search(arr, target):
    return binary_search_func(arr, 0, len(arr) - 1, target)

def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    
    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return binary_search_func(arr, start_index, mid_index - 1, target)
    else:
        return binary_search_func(arr, mid_index + 1, end_index, target)
```

## Tower of Hanoi
```python
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    if num_disks == 0:
        return
    
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')
```

## Return subsets
```python
def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    """
    return return_subsets(arr, 0)
    pass

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]
    
    small_output = return_subsets(arr, index+1)
    
    output = list()
    for element in small_output:
        output.append(element)
        
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output
```

## Last index
```python
def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    """
    if len(arr) == 0:
        return -1
    if arr.pop() == target:
        return len(arr)
    return last_index(arr, target)
```