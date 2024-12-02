"""
https://adventofcode.com/2024/day/1
Day 1: Historian Hysteria
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

inputList = file_reader(os.path.join(PATH, 'day1_test.txt'))

TOTAL_DISTANCE = 0
SIMILARITY_SCORE = 0
leftList = []
rightList = []
for x in inputList:
    numbers = x.strip('\n').split(' ')
    leftList.append(int(numbers[0]))
    rightList.append(int(numbers[-1]))
leftList.sort()
rightList.sort()

if len(leftList) == len(rightList):
    for i, a in enumerate(leftList):
        b = rightList[i]
        if a > b:
            TOTAL_DISTANCE += a - b
        else:
            TOTAL_DISTANCE += b - a
        SIMILARITY_SCORE += int(a) * int(rightList.count(a))
    print("Part1: ", TOTAL_DISTANCE)
    print("Part2: ", SIMILARITY_SCORE)
else:
    print("Foo")
    