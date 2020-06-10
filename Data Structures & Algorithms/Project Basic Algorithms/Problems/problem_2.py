def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if type(number) is not int or len(input_list) < 1:
        return -1

    if input_list[0] == number:
        return 0

    rotated_point = find_rotated_point(input_list)

    if input_list[rotated_point] < input_list[rotated_point - 1]:
        rotated_point -= 1

    left_array = input_list[0:rotated_point + 1]
    right_array = input_list[rotated_point + 1:len(input_list)]

    if number <= right_array[len(right_array) - 1]:
        index = binary_serch(right_array, number)
        
        return index if index == -1 else index + rotated_point + 1
    
    index = binary_serch(left_array, number)

    return index

def find_rotated_point(input_list):
    start_index = 0
    end_index = len(input_list) - 1

    while input_list[start_index] > input_list[end_index]:
        start_index += 1
        end_index -= 1
    
    if input_list[end_index] > input_list[start_index - 1]:
        return end_index
    
    return start_index

def binary_serch(input_list, number):
    start_index = 0
    end_index = len(input_list) - 1
    
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_element = input_list[mid_index]

        if number == mid_element:
            return mid_index
        elif number < mid_element:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test case 1

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test case 2

test_function([[2], 2])

# Test case 3

test_function([[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5], 13])
test_function([[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5], 2])

# Test case 4

test_function([[15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 17])
test_function([[15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 12])

# Test case 5 - edge cases

test_function([[], 1]) # returns a "pass" message because these arguments are validated
test_function([[], None]) # returns a "pass" message because these arguments are validated
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], None]) # returns a "pass" message because these arguments are validated

# Test case 6 - edge cases

test_function([[10**10000 + 2, 10**10000 + 3, 10**10000 + 4, 10**10000, 10**10000 + 1], 10**10000 + 3])
test_function([[10**10000 + 2, 10**10000 + 3, 10**10000 + 4, 10**10000, 10**10000 + 1], 10**10000 + 1])
test_function([[10**10000 + 2, 10**10000 + 3, 10**10000 + 4, 10**10000, 10**10000 + 1], 0])