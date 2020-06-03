def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_number, min_number = None, None

    for number in ints:

        if max_number is None:
            max_number = number
            min_number = number
        else:        
            if number > max_number: max_number = number
            if number < min_number: min_number = number

    if max_number is None:
        return 'Invalid argument'
    
    pigeonhole_sort(ints, min_number, max_number)

    return (ints[0], ints[-1])

def pigeonhole_sort(ints, min_number, max_number): 
    size = max_number - min_number + 1
    holes = [0] * size
  
    for x in ints: 
        holes[x - min_number] += 1
  
    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            ints[i] = count + min_number 
            i += 1

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

## Test Case of One Thousand Integers

l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)

print ("Pass" if ((0, 999) == get_min_max(l)) else "Fail")

## Test Case of One Million Integers

l = [i for i in range(0, 1000000)]  # a list containing 0 - 999999
random.shuffle(l)

print ("Pass" if ((0, 999999) == get_min_max(l)) else "Fail")

## Test Case of Zero Integers - returns a message of invalid argument and fails the test

l = [i for i in range(0)]  # a list containing nothing
random.shuffle(l)

print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail") 