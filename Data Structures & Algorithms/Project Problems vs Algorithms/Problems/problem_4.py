def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    aux_dict = {}

    for i in input_list:
        if type(i) is not int or not 0 <= i <= 2:
            return "Invalid argument"

        if i not in aux_dict:
            aux_dict[i] = []
        aux_dict[i].append(i)
    
    return (aux_dict[0] if 0 in aux_dict else []) + \
        (aux_dict[1] if 1 in aux_dict else []) + \
        (aux_dict[2] if 2 in aux_dict else [])

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test case 1

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case 2

test_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0])
test_function([2, 1, 0, 3]) # returns a message of invalid argument and fails the test

# Test case 3

test_function([0, 0, 0, 0, 0, 0]) # returns a array with only 0
test_function([0, 0, 1, 0, 1, 1]) # returns a sorted array with only 0 and 1

# Test case 4 - edge cases

test_function([]) # returns an empty array
test_function([None]) # returns a message of invalid argument and fails the test
test_function([""]) # returns a message of invalid argument and fails the test