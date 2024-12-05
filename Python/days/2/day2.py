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

inputList = file_reader(os.path.join(PATH, 'day2.txt'))

PART1_SAFE_REPORT_COUNTER = 0
PART2_SAFE_REPORT_COUNTER = 0

def check_report(level_list):
    """Checks the report if it is safe - returns a negative value if unresolveable"""
    inc_count = 0
    dec_count = 0
    for y, current_value in enumerate(level_list):
        if y+1 < len(level_list):
            delta_value = int(level_list[y+1]) - int(current_value)
            if -1 >= delta_value >= -3 :
                dec_count += 1
            elif 1 <= delta_value <= 3:
                inc_count += 1
            elif delta_value == 0:
                return (False, y)
            else:
                return (False, y+1)
            if dec_count >= 1 and inc_count >= 1:
                return (False, y)
        else:
            if (dec_count > 0 and inc_count == 0) or (inc_count > 0 and dec_count == 0):
                return (True,-1)
    return (False, -1)

for rawReport in inputList:
    reportList = rawReport.strip('\n').split(' ')
    resultTuple = check_report(reportList)
    #Do Part 1
    if resultTuple[0] is True:
        PART1_SAFE_REPORT_COUNTER += 1
    elif resultTuple[1] >= 0:
        popIndex = resultTuple[1]
        reportListAfter = reportList[:]
        reportListBefore = reportList[:]
        reportList.pop(popIndex)
        reportListBefore.pop(popIndex-1)
        if check_report(reportList)[0] is True:
            PART2_SAFE_REPORT_COUNTER += 1
        elif check_report(reportListBefore)[0] is True:
            PART2_SAFE_REPORT_COUNTER += 1
        elif popIndex < len(reportListAfter):
            reportListAfter.pop(popIndex+1)
            if check_report(reportListAfter)[0] is True:
                PART2_SAFE_REPORT_COUNTER += 1

print("Part1: ",PART1_SAFE_REPORT_COUNTER)
print("Part2: ",PART1_SAFE_REPORT_COUNTER+PART2_SAFE_REPORT_COUNTER)
