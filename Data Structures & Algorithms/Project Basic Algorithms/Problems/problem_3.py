def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return "Invalid arguments"

    # quicksort(input_list) - option to use if the array has repeated elements

    input_list = count_frequencies(input_list)

    return get_highest_sum(input_list)

def get_highest_sum(input_list):
    digits_first, digits_second = get_digits(len(input_list))
    
    first_number, second_number = "", ""

    for i in range(digits_first):
        first_number += str(input_list[(len(input_list) - 1) - i * 2])
        if digits_first != digits_second:
            if i != digits_first - 1:
                second_number += str(input_list[(len(input_list) - 2) - i * 2])
        else:
            second_number += str(input_list[(len(input_list) - 2) - i * 2])
    
    return int(first_number), int(second_number)

def get_digits(list_size):
    if list_size % 2 != 0:
        return list_size // 2 + 1, list_size // 2
    
    return list_size // 2, list_size // 2

def count_frequencies(input_list):
    frequencies = set()
    
    for element in input_list:
        frequencies.add(element)

    return list(frequencies)

def quicksort(input_list):
    quicksort_recursive_solution(input_list, 0, len(input_list) - 1)

def quicksort_recursive_solution(input_list, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_helper(input_list, begin_index, end_index)

    quicksort_recursive_solution(input_list, begin_index, pivot_index - 1)
    quicksort_recursive_solution(input_list, pivot_index + 1, end_index)

def sort_helper(input_list, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = input_list[pivot_index]

    while (pivot_index != left_index):

        value = input_list[left_index]

        if value <= pivot_value:
            left_index += 1
            continue

        input_list[left_index] = input_list[pivot_index - 1]
        input_list[pivot_index - 1] = pivot_value
        input_list[pivot_index] = value

        pivot_index -= 1
    
    return pivot_index

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test case 1

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test case 2

test_function([[6, 12, 7, 1, 13, 18, 15, 5, 9, 16, 19, 4, 11, 3, 8, 14, 10, 2, 17, 20], 
    [2018161412108642, 191715131197531]])

# Test case 3 - edge cases

try:
    test_function([[], []])
    test_function([[1], [1]])
    test_function([[None], [None, None]])
    test_function([[""], ["", ""]])

except TypeError: print("Invalid arguments")

# Test case 4 - edge cases

test_function([[10**1000 + 5, 10**1000 + 1, 10**1000 + 3, 10**1000 + 4, 10**1000], 
    [int(str(10**1000 + 5) + str(10**1000 + 3) + str(10**1000)), int(str(10**1000 + 4) + str(10**1000 + 1))]])
