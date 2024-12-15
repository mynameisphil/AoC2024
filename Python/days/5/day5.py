"""
https://adventofcode.com/2024/day/5
Day 5: Print Queue
"""

import inspect
import os
from collections import defaultdict

def file_reader(file_name):
    """Reading and returning a files content as list"""
    file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    with open(os.path.join(file_path, file_name), encoding="utf-8") as file:
        contents = file.readlines()
    return contents

def init_puzzle_config():
    """Parsing the puzzle input"""
    rules_flag = True
    rules_list = []
    pages_list = []
    for item in file_reader('day5.txt'):
        if rules_flag is True:
            if item.strip() == '':
                rules_flag = False
                continue
            rules_list.append(item.strip('\n'))
        else:
            pages_list.append(item.strip('\n'))
    return rules_list, pages_list

rawConfigDict = {"rules" : [], "pages" : []}
rawConfigDict["rules"], rawConfigDict["pages"] = init_puzzle_config()

DEBUG_FLAG = False

valid_order_list = []



for rawPage in rawConfigDict["pages"]:
    current_page = rawPage.split(',')
    sorted_print_order = []
    if DEBUG_FLAG is True:
        print("Print Order")
        print(">",current_page) # something is off
    for rule in rawConfigDict["rules"]:
        first,second = rule.split('|')
        if first not in current_page:
            continue
        if second not in current_page:
            continue
        if first not in sorted_print_order:
            sorted_print_order.append(first)
        if second not in sorted_print_order:
            sorted_print_order.append(second)
    for rule in rawConfigDict["rules"]:
        first,second = rule.split('|')
        if first not in current_page:
            continue
        if second not in current_page:
            continue
        if sorted_print_order.index(first) > sorted_print_order.index(second):
            sorted_print_order.pop(sorted_print_order.index(first))
            sorted_print_order.insert(sorted_print_order.index(second),first)
    if DEBUG_FLAG is True:
        print("Update Order")
        print(">",sorted_print_order)
        print(">",(current_page == sorted_print_order))
        print("\n")
    if (current_page == sorted_print_order):
        valid_order_list.append(current_page)
        
PART1_TOTAL = 0
for order in valid_order_list:
#   print(len(order)%2,order)
    PART1_TOTAL += int(order[int(len(order)/2)])
print(PART1_TOTAL,len(valid_order_list)) 
