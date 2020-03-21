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


def alreadyAdded(item, different):
    for single in different:
        if single == item:
            return True
    return False


def addNumberIfNotAdded(item, different):
    if not alreadyAdded(item, different):
        different.append(item)


def getUniqueNumbersFrom(records, different):
    for record in records:
        addNumberIfNotAdded(record[0], different)
        addNumberIfNotAdded(record[1], different)


def printCountOfUniqueTelephoneNumbers():
    different = []

    getUniqueNumbersFrom(texts, different)
    getUniqueNumbersFrom(calls, different)

    print("There are " + str(len(different)) + " different telephone numbers in the records.")



printCountOfUniqueTelephoneNumbers()