"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
prefix_bangalore = "(080)"

def verify_add_prefix(calls, prefixes, i):
    """Verify if is a bangalore area and add a fix value to prefixes that called in Bangalore.
    INPUT:
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    prefixes: Dictionary. The prefixes (key) and the value to control if is in Bangalore (value).
    i: Integer. The index of the current call data.
    """
    number_call = calls[i][0]
    number_receive = calls[i][1]
    prefix = ""
    if number_call[:5] == prefix_bangalore:
        prefix = number_receive[:3]
    if prefix != "":
        if prefix[0] == '9' or prefix[0] == '8' or prefix[0] == '7':
            if not prefix in prefixes: prefixes[prefix] = 1

def verify_add_area(calls, areas, i):
    """Verify if is a bangalore area and add a fix value to areas that called in Bangalore.
    INPUT:
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    areas: Dictionary. The areas (key) and the value to control if is in Bangalore (value).
    i: Integer. The index of the current call data.
    """
    number_call = calls[i][0]
    number_receive = calls[i][1]
    area = ""
    if number_call[:5] == prefix_bangalore:
        if number_receive[0] == '(':
            area = number_receive.split(')')[0][1:]
    if area != "":
        if not area in areas: areas[area] = 1

def area_codes_prefixes_bangalore(calls):
    """Find the area codes and prefixes that called in Bangalore and create a message.
    INPUT:
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    OUTPUT:
    msg: The message of the area codes and prefixes that called in Bangalore.
    """
    prefixes = {}
    areas = {}
    for i in range(len(calls)):
        verify_add_prefix(calls, prefixes, i)
        verify_add_area(calls, areas, i)
    list_prefix_area = sorted(list(prefixes.keys()) + list(areas.keys()))
    msg = "The numbers called by people in Bangalore have codes:"
    for i in range(len(list_prefix_area)): msg += '\n' + list_prefix_area[i]
    return msg

def is_bangalore(calls, i):
    """Verify if is a bangalore area and control the possibility of a bangalore call.
    INPUT:
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    i: Integer. The index of the current call data.
    OUTPUT:
    Tuple
        The variable to control wheter it's from bangalore and wheter it's a bangalore call.
    """
    number_call = calls[i][0]
    number_receive = calls[i][1]
    area = ""
    add_variable = (0, 0)
    if number_call[:5] == prefix_bangalore:
        if number_receive[0] == '(':
            area = number_receive.split(')')[0][1:]
        add_variable = (1, 0)
    if area == prefix_bangalore[1:4]:
        add_variable = (1, 1)
    return add_variable

def percentage_bangalore_to_bangalore(calls):
    """Calculates the percentage of calls from bangalore that are made also to Bangalore and create a message.
    INPUT:
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    OUTPUT:
    msg: The message of the percentage of calls.
    """
    total_number, total_to_bangalore = 0, 0
    for i in range(len(calls)):
        add_variable = is_bangalore(calls, i)
        if add_variable[0] == 1: total_number += 1
        if add_variable[1] == 1: total_to_bangalore += 1
    percentage = str(float("{:.2f}".format((total_to_bangalore * 100) / total_number)))
    msg = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage)
    return msg

import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print(area_codes_prefixes_bangalore(calls))
print(percentage_bangalore_to_bangalore(calls))