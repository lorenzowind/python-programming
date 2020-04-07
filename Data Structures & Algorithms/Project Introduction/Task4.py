"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def get_tuples_data(texts, calls):
    """Get tuples representing the data with the highest and the lowest size of texts or calls.
    INPUT:
    texts: Strings list. The incoming number, answering number, and timestamp of the messages.
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    OUTPUT: 
    tuples 
        The size and the data related to the highest and the lowest.
    """
    if len(texts) > len(calls):
        return (len(texts), texts), (len(calls), calls)
    else:
        return (len(calls), calls), (len(texts), texts)

def verify_telemarketer(data, numbers, i):
    """Verify and control if the number is not automatically a telemarketer.
    INPUT:
    data: Strings list. The texts or the calls.
    numbers: Dictionary. The telephone numbers (key) and the quantity of texts or calls (value).
    i: Integer. The index of the current text or call data.
    """
    number_send = data[1][i][0]
    number_receive = data[1][i][1]
    if len(data[1][i]) == 3:
        if not number_send in numbers: numbers[number_send] = False
        elif numbers[number_send]: numbers[number_send] = False
    else:
        if not number_send in numbers: numbers[number_send] = True
    if not number_receive in numbers: numbers[number_receive] = False
    elif numbers[number_receive]: numbers[number_receive] = False       

def telemarketers_number(texts, calls):
    """Search for numbers that are possible telemarketers and create a message.
    INPUT:
    texts: Strings list. The incoming number, answering number, and timestamp of the messages.
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    OUTPUT:
    msg: The message of the possible telemarketers.
    """
    numbers = {}
    higher_data, lower_data = get_tuples_data(texts, calls)
    for i in range(higher_data[0]):
        verify_telemarketer(higher_data, numbers, i)
        if i < lower_data[0]:
            verify_telemarketer(lower_data, numbers, i)
    msg = "These numbers could be telemarketers:"
    list_telemarketers = [key for key, value in numbers.items() if value]
    for number in sorted(list_telemarketers): msg += '\n' + number
    return msg

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print(telemarketers_number(texts, calls))