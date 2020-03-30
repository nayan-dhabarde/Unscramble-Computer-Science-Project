"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def addDuration(number, duration, numberToDuration):

    if number in numberToDuration:
        numberToDuration[number] = numberToDuration[number] + duration
    else:
        numberToDuration[number] = duration

    return numberToDuration


def getNumberToDurationMap():
    numberToDuration = {}

    for call in calls:
        duration = call[3]
        numberToDuration = addDuration(call[0], int(duration), numberToDuration)
        numberToDuration = addDuration(call[1], int(duration), numberToDuration)

    return numberToDuration


def getNumberWhichSpendLongestTimeOnCall():
    longestDuration = 0
    numberWithLongestDuration = None
    numberToDuration = getNumberToDurationMap()

    for number in numberToDuration.keys():
        duration = int(numberToDuration[number])
        if longestDuration < duration:
            longestDuration = duration
            numberWithLongestDuration = number

    print(numberWithLongestDuration + " spent the longest time, " + str(longestDuration) +
          " seconds, on the phone during September 2016.")


# print(getNumberToDurationMap())
getNumberWhichSpendLongestTimeOnCall()


