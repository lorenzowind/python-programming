def smallest_positive(in_list):
    x = None
    if len(in_list) > 0:
        for num in in_list:
            if num > 0:
                if x == None or num < x:
                    x = num
    return x

print(smallest_positive([4, -6, 7, 2, -4, 10]))
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
print(smallest_positive([-6, -9, -7]))
print(smallest_positive([]))