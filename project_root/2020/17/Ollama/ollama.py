import os
from itertools import chain, combinations
from copy import deepcopy
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except Exception:
    data, lines = "", []

DIM = max(len(lines), len(lines[0])) + 2 * 6
world3 = [[[False] * DIM for _ in range(DIM)] for _ in range(DIM)]
mid = DIM // 2
z0, y0, x0 = mid, mid - len(lines) // 2, mid - len(lines[0]) // 2

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        world3[z0][y0 + y][x0 + x] = (c == '#')

def neighbors3(world, z, y, x):
    adj = 0
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dz == dy == dx == 0:
                    continue
                zz, yy, xx = z + dz, y + dy, x + dx
                if 0 <= zz < DIM and 0 <= yy < DIM and 0 <= xx < DIM and world[zz][yy][xx]:
                    adj += 1
    return adj

def round3(world):
    new = deepcopy(world)
    for z in range(DIM):
        for y in range(DIM):
            for x in range(DIM):
                adj = neighbors3(world, z, y, x)
                if world[z][y][x]:
                    if adj not in (2, 3):
                        new[z][y][x] = False
                else:
                    if adj == 3:
                        new[z][y][x] = True
    return new

for _ in range(6):
    world3 = round3(world3)

result1 = sum(sum(sum(row) for row in plane) for plane in world3)
print(result1, end=' ')

from collections import defaultdict

worldd = defaultdict(bool)

yoffset = 0
for line in lines:
    for idx, c in enumerate(line):
        if c == "#":
            coord = (0, 0, yoffset, idx)
            worldd[coord] = True
    yoffset += 1

def neighbors(worldd, x, y, z, w):
    offs = (-1, 0, 1)
    adj = 0
    for dw in offs:
        for dz in offs:
            for dy in offs:
                for dx in offs:
                    if dx == dy == dz == dw == 0:
                        continue
                    xx = x + dx
                    yy = y + dy
                    zz = z + dz
                    ww = w + dw
                    if worldd[(ww, zz, yy, xx)]:
                        adj += 1
    return adj

def round4(worldd):
    new_worldd = defaultdict(bool)
    active_coords = set(k for k, v in worldd.items() if v)

    for w, z, y, x in active_coords:
        for dw in (-1, 0, 1):
            for dz in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        adj = neighbors(worldd, x + dx, y + dy, z + dz, w + dw)
                        if worldd[(w, z, y, x)]:
                            new_worldd[(w, z, y, x)] = True if adj in (2, 3) else False
                        elif adj == 3:
                            new_worldd[(w, z, y, x)] = True

    return new_worldd

for _ in range(6):
    worldd = round4(worldd)

result2 = sum(value for value in worldd.values() if value)
print(result2)