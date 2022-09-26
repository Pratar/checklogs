import sys
import datetime
from datetime import timedelta
import re

def roundMunute(line):
    margin = re.search('\[(.*)\]', re.sub(r'.{2}]', '00]', line))
    nextMinute = datetime.datetime.strptime(margin.group(0), '[%Y-%m-%d %H:%M:%S]') + timedelta(minutes=1)
    return nextMinute

def getEvent(line):
    minute = re.search('\[(.*)\]', line)
    eventTime = datetime.datetime.strptime(minute.group(0), '[%Y-%m-%d %H:%M:%S]')
    return eventTime

countNOK = 0

f = open("test.txt",'r')
line = f.readline()
nextMinute = roundMunute(line)
while line:
    if 'NOK' in line:
        eventMinute = getEvent(line) 

        if  nextMinute > eventMinute:
            countNOK += 1

        if  nextMinute < eventMinute:
            print(nextMinute - timedelta(minutes=1), "Count event:", countNOK)
            countNOK = 1
            nextMinute = roundMunute(line)

    line = f.readline()

print(nextMinute - timedelta(minutes=1), "Count event:", countNOK)
f.close()
