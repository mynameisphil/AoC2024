"""
https://adventofcode.com/2024/day/3
Day 3: Mull It Over
"""

import inspect
import re
import os

def file_reader(file_name):
    """Reading and returning a files content"""
    file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    with open(os.path.join(file_path, file_name), encoding="utf-8") as file:
        contents = file.readlines()
    return contents

PART1_REGEX = r"mul[(]\d{1,3}[,]\d{1,3}[)]"
PART1_SUB_REGEX = r"\d{1,3}[,]\d{1,3}"

inputList = file_reader('day3.txt')

PART1_RESULT = 0


for line in inputList:
    for instruction in re.findall(PART1_REGEX,line):
        result = re.findall(PART1_SUB_REGEX,instruction)
        number_a = int(result[0].split(',')[0])
        number_b = int(result[0].split(',')[1])
        PART1_RESULT += number_a * number_b

print("Part1:",PART1_RESULT)

PART2_REGEX = r"(don't\(\)|do\(\)|mul[(]\d{1,3}[,]\d{1,3}[)])"

matchList = []
DONT_FLAG = False

PART2_RESULT = 0

for line in inputList:
    for instruction in re.findall(PART2_REGEX,line):
        if instruction == "don't()":
            DONT_FLAG = True
        if instruction == "do()":
            DONT_FLAG = False
        if DONT_FLAG is False and instruction != "do()":
            matchList.append(instruction)

for line in matchList:
    result = re.findall(PART1_SUB_REGEX,line)
    number_a = int(result[0].split(',')[0])
    number_b = int(result[0].split(',')[1])
    PART2_RESULT += number_a * number_b

print("Part2:",PART2_RESULT)
