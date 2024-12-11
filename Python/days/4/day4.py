"""
https://adventofcode.com/2024/day/4
Day 4: Ceres Search
"""

import inspect
import os

def file_reader(file_name):
    """Reading and returning a files content"""
    file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    with open(os.path.join(file_path, file_name), encoding="utf-8") as file:
        contents = file.readlines()
    return contents

def check_vertical(input_list,pattern):
    """
    Checks input list against a vertical pattern for example
    xmas_vertical = ['X0.#','M1-_','A2!+','S3&%']
    pattern = "XMAS"
    """
    count = 0
    for y in range(len(input_list[0])):
        if input_list[0][y] == pattern[0]:
            if input_list[1][y] == pattern[1]:
                if input_list [2][y] == pattern[2]:
                    if input_list[3][y] == pattern[3]:
                        count += 1
    return count

def check_horizontal(input_list,pattern):
    """
    Checks input list against a pattern for example
    xmas_horizontal = ['XMAS','b1-_','c2!+','d3&%']
    pattern = "XMAS"
    """
    count = 0
    for line in input_list:
        if line.count(pattern):
            count += 1
    return count

def check_diagonal(input_list,pattern):
    """
    Checks input list against a pattern for example
    xmas_diagonal = ['X0.#','bM-_','c2A+','d3&S']
    pattern = "XMAS"
    """
    count = 0
    if input_list[0][0] == pattern[0]:
        if input_list[1][1] == pattern[1]:
            if input_list [2][2] == pattern[2]:
                if input_list[3][3] == pattern[3]:
                    count = 1
    return count

def check_anti_diagonal(input_list,pattern):
    """
    Checks input list against a pattern for example
    xmas_anti_diagonal = ['a0.S','b1A_','cM!+','X3&%']
    pattern = "XMAS"
    """
    count = 0
    if input_list[0][3] == pattern[3]:
        if input_list[1][2] == pattern[2]:
            if input_list [2][1] == pattern[1]:
                if input_list[3][0] == pattern[0]:
                    count = 1
    return count

file_as_list = file_reader('day4.txt')

MAX_COLUMNS = len(file_as_list[0].strip('\n'))
MAX_HEIGHT = len(file_as_list)
TOTAL_COUNT = 0

# Really crude but quick "initial 4 lines population and processing"
# Didn't want to change the logic at line 96 for that
buffer = []
for inputLine in file_as_list[:4]:
    buffer.append(inputLine.strip('\n'))
    TOTAL_COUNT+= inputLine.count("XMAS") + inputLine.count("SAMX")

TOTAL_COUNT += check_vertical(buffer,"XMAS") + check_vertical(buffer,"SAMX")

for i in range(0,MAX_COLUMNS):
    frame = []
    for buffer_line in buffer:
        if i+4 > MAX_COLUMNS:
            break
        frame.append(buffer_line[i:4+i])
    if len(frame) == 4:
        TOTAL_COUNT += check_anti_diagonal(frame,"XMAS") + check_diagonal(frame,"XMAS")
        TOTAL_COUNT += check_anti_diagonal(frame,"SAMX") + check_diagonal(frame,"SAMX")

for i in range(len(buffer),MAX_HEIGHT):
    buffer.pop(0)
    buffer.append(file_as_list[i].strip('\n'))
    TOTAL_COUNT+= file_as_list[i].count("XMAS") + file_as_list[i].count("SAMX")
    TOTAL_COUNT += check_vertical(buffer,"XMAS") + check_vertical(buffer,"SAMX")
    for i in range(0,MAX_COLUMNS):
        frame = []
        for buffer_line in buffer:
            if i+4 > MAX_COLUMNS:
                break
            frame.append(buffer_line[i:4+i])
        if len(frame) == 4:
            TOTAL_COUNT += check_anti_diagonal(frame,"XMAS") + check_diagonal(frame,"XMAS")
            TOTAL_COUNT += check_anti_diagonal(frame,"SAMX") + check_diagonal(frame,"SAMX")

print("Part1:",TOTAL_COUNT)
