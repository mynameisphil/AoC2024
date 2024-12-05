"""
https://adventofcode.com/2024/day/3
Day 4: Ceres Search
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

