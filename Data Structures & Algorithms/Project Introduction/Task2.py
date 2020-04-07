"""
TASK 2: 
Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def add_duration_numbers(calls, numbers, i):
    """Add an initial duration or increment the duration on the dictionary, with the key beeing the telephone number.
    INPUT:
    data: Strings list. The texts or the calls.
    numbers: Dictionary. The telephone numbers (key) and the duration spent on the phone (value).
    i: Integer. The index of the current call data.
    """
    number_call = calls[i][0]
    number_receive = calls[i][1]
    duration = int(calls[i][3])
    numbers[number_call] = duration if not number_call in numbers else numbers[number_call] + duration
    numbers[number_receive] = duration if not number_receive in numbers else numbers[number_receive] + duration

def telephone_longest_time(calls):
    """Calculates the longest time spent on the phone and create a message.
    INPUT:
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    OUTPUT: 
    msg: The message of the longest time spent on the phone.
    """
    numbers = {}
    for i in range(len(calls)):
        add_duration_numbers(calls, numbers, i)
    time = max(numbers.values())
    number = [key for key, value in numbers.items() if value == time]
    msg = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(number[0], str(time))
    return msg

import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print(telephone_longest_time(calls))