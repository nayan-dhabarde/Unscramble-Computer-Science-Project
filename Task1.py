"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def getUniqueNumbersFrom(records, different):
    for record in records:
        different.add(record[0])
        different.add(record[1])

def printCountOfUniqueTelephoneNumbers():
    different = set()

    getUniqueNumbersFrom(texts, different)
    getUniqueNumbersFrom(calls, different)

    print("There are " + str(len(different)) + " different telephone numbers in the records.")


printCountOfUniqueTelephoneNumbers()