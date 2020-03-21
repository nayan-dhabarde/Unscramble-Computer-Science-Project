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

def getAreaCode(number):
    num = str()
    i = 1
    while number[i] != ')':
        num += number[i]
        i += 1
    return num


def getNumberPrefix(number):
    num = str()
    hasSpace = False
    for character in number:
        if character == " ":
            hasSpace = True
            return num
        else:
            num += character

    if hasSpace:
        return num

    return ""


def getCode(number):
    if number[0] == '(':
        return getAreaCode(number)
    else:
        numPrefix = getNumberPrefix(number)
        if numPrefix != "":
            return numPrefix
        else:
            return "140"

def doesNotContain(codes, codeToBeAdded):
    for code in codes:
        if code == codeToBeAdded:
            return False
    return True

def addCode(code, codes):
    if doesNotContain(codes, code):
        codes.append(code)


def printListOfCodes():
    codes = []

    for record in calls:
        caller = record[0]
        receiver = record[1]

        if "(080)" in caller:
            code = getCode(receiver)
            addCode(code, codes)

    print("The numbers called by people in Bangalore have codes:")
    for code in codes:
        print(code)


# printListOfCodes()


def callIsBangaloreFixedLine(number):
    if number[0] == "(":
        if getAreaCode(number) == "080":
            return True
        else:
            return False

    return False


# Get number of calls made from 080
def printPercentageOfCallsMadeFroAndToBangalore():
    callsFrom = 0
    callsTo = 0
    for call in calls:
        if callIsBangaloreFixedLine(call[0]):
            callsFrom += 1
            if callIsBangaloreFixedLine(call[1]):
                callsTo += 1

    percentage = (100 * callsTo) / callsFrom
    print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
          % percentage)

# Print percentage of calls made to and from 080


printListOfCodes()
printPercentageOfCallsMadeFroAndToBangalore()

