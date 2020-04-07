"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
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

def add_value_numbers(data, numbers, i):
    """Add an initial value or increment the value on the dictionary, with the key beeing the telephone number.
    INPUT:
    data: Strings list. The texts or the calls.
    numbers: Dictionary. The telephone numbers (key) and the quantity of texts or calls (value).
    i: Integer. The index of the current text or call data.
    """
    number_send = data[1][i][0]
    number_receive = data[1][i][1]
    numbers[number_send] = 1 if not number_send in numbers else numbers[number_send] + 1
    numbers[number_receive] = 1 if not number_receive in numbers else numbers[number_receive] + 1
    
def different_numbers_texts_calls(texts, calls):
    """Calculates the number of different telephone numbers in texts and calls and create a message.
    INPUT:
    texts: Strings list. The incoming number, answering number, and timestamp of the messages.
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    OUTPUT: 
    msg: The message of the different telephone numbers in texts and calls.
    """
    numbers = {}
    higher_data, lower_data = get_tuples_data(texts, calls)
    for i in range(higher_data[0]):
        add_value_numbers(higher_data, numbers, i)
        if i < lower_data[0]:
            add_value_numbers(lower_data, numbers, i)
    msg = "There are {} different telephone numbers in the records.".format(str(len(numbers)))
    return msg

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print(different_numbers_texts_calls(texts, calls))