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

def check_part2(input_list):
    """Pattern is 3x3 MAS in any direction - for it to be valid it needs to have 2 occurences"""
    count = 0
    if input_list[1][1] == 'A':
        diagonal = input_list[0][0] + input_list[1][1] + input_list[2][2]
        anti_diagonal = input_list[2][0] + input_list[1][1] + input_list[0][2]
        if diagonal in ('SAM','MAS') and anti_diagonal in ('SAM','MAS'):
            count = 1
    return count

file_as_list = file_reader('day4_test.txt')

MAX_COLUMNS = len(file_as_list[0].strip('\n'))
MAX_HEIGHT = len(file_as_list)


def part1():
    """Solving for Part1"""
    # Really crude but quick "initial 4 lines population and processing"
    # Didn't want to change the logic at line 96 for that
    buffer = []
    total_count = 0
    for input_line in file_as_list[:4]:
        buffer.append(input_line.strip('\n'))
        total_count+= input_line.count("XMAS") + input_line.count("SAMX")

    total_count += check_vertical(buffer,"XMAS") + check_vertical(buffer,"SAMX")

    for i in range(0,MAX_COLUMNS):
        frame = []
        for buffer_line in buffer:
            if i+4 > MAX_COLUMNS:
                break
            frame.append(buffer_line[i:4+i])
        if len(frame) == 4:
            total_count += check_anti_diagonal(frame,"XMAS") + check_diagonal(frame,"XMAS")
            total_count += check_anti_diagonal(frame,"SAMX") + check_diagonal(frame,"SAMX")

    for i in range(len(buffer),MAX_HEIGHT):
        buffer.pop(0)
        buffer.append(file_as_list[i].strip('\n'))
        total_count+= file_as_list[i].count("XMAS") + file_as_list[i].count("SAMX")
        total_count += check_vertical(buffer,"XMAS") + check_vertical(buffer,"SAMX")
        for i in range(0,MAX_COLUMNS):
            frame = []
            for buffer_line in buffer:
                if i+4 > MAX_COLUMNS:
                    break
                frame.append(buffer_line[i:4+i])
            if len(frame) == 4:
                total_count += check_anti_diagonal(frame,"XMAS") + check_diagonal(frame,"XMAS")
                total_count += check_anti_diagonal(frame,"SAMX") + check_diagonal(frame,"SAMX")

    print("Part1:",total_count)
def part2():
    """Solving for Part2"""
    # Really crude but quick "initial 3 lines population and processing"
    # Didn't want to change the logic at line 96 for that
    buffer = []
    total_count = 0
    for input_line in file_as_list[:3]:
        buffer.append(input_line.strip('\n'))

    for i in range(0,MAX_COLUMNS):
        frame = []
        for buffer_line in buffer:
            if i+3 > MAX_COLUMNS:
                break
            frame.append(buffer_line[i:3+i])
        if len(frame) == 3:
            total_count += check_part2(frame)

    for i in range(len(buffer),MAX_HEIGHT):
        buffer.pop(0)
        buffer.append(file_as_list[i].strip('\n'))
        for i in range(0,MAX_COLUMNS):
            frame = []
            for buffer_line in buffer:
                if i+3 > MAX_COLUMNS:
                    break
                frame.append(buffer_line[i:3+i])
            if len(frame) == 3:
                total_count += check_part2(frame)

    print("Part2:",total_count)
part1()
part2()
