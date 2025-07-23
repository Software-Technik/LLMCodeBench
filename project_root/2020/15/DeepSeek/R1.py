import os
from itertools import chain, combinations
from copy import deepcopy
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

line_groups = data.split("\n\n")

def coords(arr2d):
    coords = []
    for y in range(len(arr2d)):
        for x in range(len(arr2d[0])):
            coords.append((x, y))
    return coords

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def ans(answer):
    pass

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map

def line_transform(line):
    return line.split(",")

lines = [line_transform(line) for line in lines] if lines else []

if not lines:
    print("")
    exit(0)

starting_numbers = [int(x) for x in lines[0]]
n = len(starting_numbers)
result1 = None
result2 = None

if n > 2019:
    result1 = starting_numbers[2019]
if n > 29999999:
    result2 = starting_numbers[29999999]

if n < 30000000:
    last_occurrence = {}
    prev_occurrence = {}
    last_spoken = None

    for turn, num in enumerate(starting_numbers):
        if num in last_occurrence:
            prev_occurrence[num] = last_occurrence[num]
        last_occurrence[num] = turn
        last_spoken = num

    turn_count = n
    while turn_count < 30000000:
        if last_spoken in prev_occurrence:
            next_num = last_occurrence[last_spoken] - prev_occurrence[last_spoken]
        else:
            next_num = 0

        if turn_count == 2019:
            result1 = next_num
        if turn_count == 29999999:
            result2 = next_num

        if next_num in last_occurrence:
            prev_occurrence[next_num] = last_occurrence[next_num]
        last_occurrence[next_num] = turn_count
        last_spoken = next_num
        turn_count += 1

if result1 is None:
    result1 = starting_numbers[2019] if n > 2019 else None
if result2 is None:
    result2 = starting_numbers[29999999] if n > 29999999 else None

print(result1, result2)