"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def first_record_texts(texts):
    """Create a message of the first record text.
    INPUT:
    texts: Strings list. The incoming number, answering number, and timestamp of the messages.
    OUTPUT: 
    msg: The first record text message.
    """
    msg = "First record of texts, {} texts {} at time {}".format(texts[0][0], 
        texts[0][1], texts[0][2].split(" ")[1])
    return msg

def last_record_calls(calls):
    """Create a message of the last record call.
    INPUT:
    calls: Strings list. The incoming number, answering number, timestamp, and duration of the calls.
    OUTPUT: 
    msg: The last record call message.
    """
    msg = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0], 
        calls[-1][1], calls[-1][2].split(" ")[1], calls[-1][3])
    return msg

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print(first_record_texts(texts))
print(last_record_calls(calls))