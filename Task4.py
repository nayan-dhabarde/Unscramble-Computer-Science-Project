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

def hasNotReceivedText(number):
    for record in texts:
        if record[1] == number:
            return False

    return True


def hasNotSendText(number):
    for record in texts:
        if record[0] == number:
            return False

    return True


def hasNotReceivedACall(number):
    for record in calls:
        if record[1] == number:
            return False

    return True


def addTeleMarketer(telemarketers, number):
    if not exists(telemarketers, number):
        telemarketers.append(number)


def exists(telemarketers, number):
    for telemarketer in telemarketers:
        if telemarketer == number:
            return True
    return False


def printNumbersWhichCouldBeTelemarketers():
    telemarketers = []

    for call in calls:
        caller = call[0]
        if hasNotReceivedText(caller) and hasNotSendText(caller) and hasNotReceivedACall(caller):
            addTeleMarketer(telemarketers, caller)

    print("These numbers could be telemarketers: ")

    for number in telemarketers:
        print(number)


printNumbersWhichCouldBeTelemarketers()






