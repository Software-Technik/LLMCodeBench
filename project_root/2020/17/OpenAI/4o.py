import numpy as np
from collections import defaultdict
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines = []

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
    return sum(world[zz, yy, xx] for dz in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dx in (-1, 0, 1)
               if dz != 0 or dy != 0 or dx != 0
               if 0 <= (zz := z + dz) < DIM
               and 0 <= (yy := y + dy) < DIM
               and 0 <= (xx := x + dx) < DIM)

def round3(world):
    new = world.copy()
    for z in range(DIM):
        for y in range(DIM):
            for x in range(DIM):
                adj = neighbors3(world, z, y, x)
                if world[z, y, x]:
                    new[z, y, x] = adj in (2, 3)
                else:
                    new[z, y, x] = adj == 3
    return new

for _ in range(6):
    world3 = round3(world3)
result1 = world3.sum()

def expand_world_bounds(coord, cur_min, cur_max):
    nu_min = cur_min[:]
    nu_max = cur_max[:]
    for didx in range(4):
        if coord[didx] - 1 < nu_min[didx]:
            nu_min[didx] = coord[didx] - 1
        if coord[didx] + 1 > nu_max[didx]:
            nu_max[didx] = coord[didx] + 1
    return nu_min, nu_max

worldd = defaultdict(bool)
min_dim = [0, 0, 0, 0]
max_dim = [0, 0, len(lines) - 1, len(lines[0]) - 1]

yoffset = 0
for line in lines:
    for idx, c in enumerate(line):
        if c == "#":
            coord = (0, 0, yoffset, idx)
            worldd[coord] = True
            min_dim, max_dim = expand_world_bounds(coord, min_dim, max_dim)
    yoffset += 1

def neighbors(worldd, x, y, z, w):
    return sum(worldd[(ww, zz, yy, xx)]
               for dw in (-1, 0, 1)
               for dz in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dx in (-1, 0, 1)
               if dx != 0 or dy != 0 or dz != 0 or dw != 0
               if (ww := w + dw, zz := z + dz, yy := y + dy, xx := x + dx))

def round(_seats, min_dim_, max_dim_):
    nu_min_dim, nu_max_dim = min_dim_[:], max_dim_[:]
    nu_seats = _seats.copy()
    for w in range(min_dim[0], max_dim[0]+1):
        for z in range(min_dim[1], max_dim[1]+1):
            for y in range(min_dim[2], max_dim[2]+1):
                for x in range(min_dim[3], max_dim[3]+1):
                    adj = neighbors(_seats, x, y, z, w)
                    cur_coord = (w, z, y, x)
                    cur = _seats[cur_coord]
                    if cur == True:
                        nu_seats[cur_coord] = adj in (2, 3)
                    elif adj == 3:
                        nu_seats[cur_coord] = True
                        nu_min_dim, nu_max_dim = expand_world_bounds(cur_coord, nu_min_dim, nu_max_dim)
    return nu_seats, nu_min_dim, nu_max_dim

def active(seats):
    return sum(seats.values())

for _ in range(6):
    worldd, min_dim, max_dim = round(worldd, min_dim, max_dim)
result2 = active(worldd)

print(result1, result2)