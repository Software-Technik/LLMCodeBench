import numpy as np
from collections import defaultdict
from copy import deepcopy
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

# Part 1: 3D Conway Cubes
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
                    adj += world[zz, yy, xx]
    return adj

def round3(world):
    new = world.copy()
    for z in range(DIM):
        for y in range(DIM):
            for x in range(DIM):
                adj = neighbors3(world, z, y, x)
                if world[z, y, x]:
                    new[z, y, x] = (adj in (2, 3))
                else:
                    new[z, y, x] = (adj == 3)
    return new

for _ in range(6):
    world3 = round3(world3)
result1 = world3.sum()

# Part 2: 4D Conway Cubes
def line_transform(line):
    return line

lines = [line_transform(line) for line in lines]

input_h = len(lines)
input_w = len(lines[0])

min_dim = [0, 0, 0, 0]
max_dim = [0, 0, input_h - 1, input_w - 1]

def expand_world_bounds(coord, cur_min, cur_max):
    nu_min = list(cur_min)
    nu_max = list(cur_max)
    for didx in range(4):
        if coord[didx] - 1 < nu_min[didx]:
            nu_min[didx] = coord[didx] - 1
        if coord[didx] + 1 > nu_max[didx]:
            nu_max[didx] = coord[didx] + 1
    return nu_min, nu_max

worldd = defaultdict(bool)
yoffset = 0
for line in lines:
    for idx, c in enumerate(line):
        if c == "#":
            coord = (0, 0, yoffset, idx)
            worldd[coord] = True
            min_dim, max_dim = expand_world_bounds(coord, min_dim, max_dim)
    yoffset += 1

def neighbors(worldd, x, y, z, w):
    adj = 0
    for dw in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == dy == dz == dw == 0:
                        continue
                    adj += worldd[(w + dw, z + dz, y + dy, x + dx)]
    return adj

def round(_seats, min_dim_, max_dim_):
    nu_min_dim = list(min_dim_)
    nu_max_dim = list(max_dim_)
    nu_seats = defaultdict(bool)
    for w in range(min_dim_[0], max_dim_[0] + 1):
        for z in range(min_dim_[1], max_dim_[1] + 1):
            for y in range(min_dim_[2], max_dim_[2] + 1):
                for x in range(min_dim_[3], max_dim_[3] + 1):
                    adj = neighbors(_seats, x, y, z, w)
                    cur_coord = (w, z, y, x)
                    cur = _seats[cur_coord]
                    if cur:
                        if adj in (2, 3):
                            nu_seats[cur_coord] = True
                    else:
                        if adj == 3:
                            nu_seats[cur_coord] = True
                            nu_min_dim, nu_max_dim = expand_world_bounds(cur_coord, nu_min_dim, nu_max_dim)
    return nu_seats, nu_min_dim, nu_max_dim

for _ in range(6):
    worldd, min_dim, max_dim = round(worldd, min_dim, max_dim)

result2 = sum(worldd.values())

print(result1, result2)