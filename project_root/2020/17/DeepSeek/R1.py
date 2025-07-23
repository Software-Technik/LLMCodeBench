import os
from itertools import chain, combinations
from copy import deepcopy
import sys
import numpy as np

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

strips = lambda l: list(map(str.strip, l))
ints = lambda l: list(map(int, l))
commas = lambda s: s.split(",")
comma_ints = lambda s: ints(strips(s.split(",")))

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map

DIM = max(len(lines), len(lines[0])) + 2 * 6
world3 = np.zeros((DIM, DIM, DIM), dtype=bool)
mid = DIM // 2
z0 = mid
y0 = mid - len(lines) // 2
x0 = mid - len(lines[0]) // 2

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        world3[z0, y0 + y, x0 + x] = (c == '#')

def neighbors3(world, z, y, x):
    adj = 0
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dz == dy == dx == 0:
                    continue
                zz, yy, xx = z + dz, y + dy, x + dx
                if 0 <= zz < DIM and 0 <= yy < DIM and 0 <= xx < DIM:
                    if world[zz, yy, xx]:
                        adj += 1
    return adj

def round3(world):
    new = deepcopy(world)
    for z in range(DIM):
        for y in range(DIM):
            for x in range(DIM):
                adj = neighbors3(world, z, y, x)
                if world[z, y, x]:
                    if adj not in (2, 3):
                        new[z, y, x] = False
                else:
                    if adj == 3:
                        new[z, y, x] = True
    return new

for _ in range(6):
    world3 = round3(world3)
result1 = world3.sum()

active_set = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '#':
            active_set.add((0, 0, y, x))

directions = []
for dw in (-1, 0, 1):
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dw == dz == dy == dx == 0:
                    continue
                directions.append((dw, dz, dy, dx))

from collections import defaultdict
for _ in range(6):
    counter = defaultdict(int)
    for cell in active_set:
        for d in directions:
            neighbor = (cell[0] + d[0], cell[1] + d[1], cell[2] + d[2], cell[3] + d[3])
            counter[neighbor] += 1
    candidate_set = active_set | set(counter.keys())
    new_active = set()
    for cell in candidate_set:
        cnt = counter.get(cell, 0)
        if cell in active_set:
            if cnt in (2, 3):
                new_active.add(cell)
        else:
            if cnt == 3:
                new_active.add(cell)
    active_set = new_active

result2 = len(active_set)
print(result1, result2)