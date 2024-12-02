"""
https://adventofcode.com/2024/day/2
Day 2: Red-Nosed Reports
"""
import inspect
import os
PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# Using readlines() https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

def file_reader(file_path):
    """Reading and returning a files content"""
    with open(file_path, encoding="utf-8") as file:
        contents = file.readlines()
    return contents

inputList = file_reader(os.path.join(PATH, 'day2_test.txt'))

SAFE_REPORT_COUNTER = 0

badReportDict = {}

for rawReport in inputList:
    reportList = rawReport.strip('\n').split(' ')
    INCREMENT_COUNTER = 0
    DECREMENT_COUNTER = 0
    for i, currentValue in enumerate(reportList):
        if i+1 < len(reportList):
            deltaValue = int(reportList[i+1]) - int(currentValue)
            if -1 >= deltaValue >= -3 :
                DECREMENT_COUNTER += 1
            elif 1 <= deltaValue <= 3:
                INCREMENT_COUNTER += 1
            else:
                badReportDict[rawReport.strip('\n')] = i # not all bad values are added somehow ?
                break
        else:
            if (DECREMENT_COUNTER > 0 and INCREMENT_COUNTER == 0) or (INCREMENT_COUNTER > 0 and DECREMENT_COUNTER == 0):
                SAFE_REPORT_COUNTER += 1

print("Part1: ",SAFE_REPORT_COUNTER)
