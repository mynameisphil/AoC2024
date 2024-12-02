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

inputList = file_reader(os.path.join(PATH, 'day1.txt'))

totalDistance = 0
similarityScore = 0
leftList = []
rightList = []
for x in inputList:
    numbers = x.strip('\n').split(' ')
    leftList.append(int(numbers[0]))
    rightList.append(int(numbers[-1]))
leftList.sort()
rightList.sort()


if len(leftList) == len(rightList):
    for i in range(0,len(leftList)):
        a = leftList[i]
        b = rightList[i]
        if a > b:
            totalDistance += a - b
        else:
            totalDistance += b - a
        similarityScore += int(a) * int(rightList.count(a))
    print("Part1: ", totalDistance)
    print("Part2: ", similarityScore)
else:
    print("Foo")
    

