def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) is not int or number < 0:
        return "Invalid argument"

    if number > 1:
        
        result = number // 2
        auxiliar = 0

        while result != auxiliar:
            auxiliar = result
            result = (number // auxiliar + auxiliar) // 2

            if auxiliar < result:
                result = auxiliar
        
        return result

    return number

# Test case 1

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Test case 2

print ("Pass" if  (11 == sqrt(143)) else "Fail")
print ("Pass" if  (12 == sqrt(144)) else "Fail")

# Test case 3

print ("Pass" if  (12344 == sqrt(152399024)) else "Fail")
print ("Pass" if  (12345 == sqrt(152399025)) else "Fail")

# Test case 4 - edge cases

print ("Pass" if  (31621 == sqrt(999950883)) else "Fail")
print ("Pass" if  (31622 == sqrt(999950884)) else "Fail")

# Test case 5 - edge cases

print(sqrt(-1)) # returns a message of invalid argument
print(sqrt(None)) # returns a message of invalid argument
print(sqrt("")) # returns a message of invalid argument