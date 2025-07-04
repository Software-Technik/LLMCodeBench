############### boilerplate ####################################################
import os
from itertools import chain, combinations
from copy import deepcopy
import sys

input_path = sys.argv[1]

# change to dir of script
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    with open(input_path) as f:
    # with open(r"project_root\2020\17\input.txt") as f:
        data = f.read()  # entire file as string
        lines = data.splitlines()
except:
    # print("no input.txt")
    data, lines = "", []

line_groups = data.split("\n\n")  # lines split by double newlines

# rest of utility functions unchanged...
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
############### end of boilerplate #############################################

import numpy as np

# -------- Part 1: 3D Conway Cubes --------
DIM = max(len(lines), len(lines[0])) + 2 * 6  # input dims + 2*cycles
# create 3D world
world3 = np.zeros((DIM, DIM, DIM), dtype=bool)
# center offsets
mid = DIM // 2
z0 = mid  # initial z-layer in middle
y0 = mid - len(lines) // 2
x0 = mid - len(lines[0]) // 2

# initialize
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        world3[z0, y0 + y, x0 + x] = (c == '#')

# neighbor function 3D
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

# one cycle
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

# simulate 6 cycles
for _ in range(6):
    world3 = round3(world3)
result1 = world3.sum()
# print("Part 1:", result1)


############### boilerplate ####################################################
import os
from itertools import chain, combinations
from copy import deepcopy
import sys

input_path = sys.argv[1]

# change to dir of script
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    with open(input_path) as f:
    # with open(r"project_root\2020\17\input.txt") as f:
        data = f.read()  # entire file as string
        lines = data.splitlines()
except:
    # print("no input.txt")
    data, lines = "", []

line_groups = data.split("\n\n")  # lines split by double newlines
# print(lines)
# print(len(lines), "lines in input.txt")


def coords(arr2d):
    # return [(x0,y0), (x1, y0), ...]
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
    # store answer to clipboard
    # print(answer, "| in clipboard")
    # os.system(f'echo "{answer}"| xclip -selection clipboard -in')


strips = lambda l: list(map(str.strip, l))
ints = lambda l: list(map(int, l))
commas = lambda s: s.split(",")
comma_ints = lambda s: ints(strips(s.split(",")))

# print(commas("1,2,3,4,5"))

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map

############### end of boilerplate #############################################

from collections import defaultdict


def line_transform(line):
    # split = [line.split() for line in lines]
    # return int(line)
    return line


lines = [line_transform(line) for line in lines]  # apply line_transform to each line

input_h = len(lines)
input_w = len(lines[0])
# bounding box for alive spots
min_dim = [0, 0, 0, 0]
max_dim = [0, 0, input_h - 1, input_w - 1]

# accessed coord, expand world bounds accordingly
# might over-expand
def expand_world_bounds(coord, cur_min, cur_max):
    nu_min = cur_min
    nu_max = cur_max
    for didx in range(4):
        if coord[didx] - 1 <= nu_min[didx]:
            nu_min[didx] = coord[didx] - 1
        if coord[didx] + 1 >= nu_max[didx]:
            nu_max[didx] = coord[didx] + 1
    return nu_min, nu_max

# set up initial slice
worldd = defaultdict(bool)
yoffset = 0
for line in lines:
    # put in middle
    for idx, c in E(line):
        if c == "#":
            coord = (0, 0, yoffset, idx)
            worldd[coord] = True
            min_dim, max_dim = expand_world_bounds(coord, min_dim, max_dim)
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
                    if worldd[(ww, zz, yy, xx)] == True:
                        adj += 1
    # i check 80 values
    return adj

# check inside bounding boxes
def round(_seats, min_dim_, max_dim_):
    nu_min_dim, nu_max_dim = deepcopy(min_dim_), deepcopy(max_dim_)
    nu_seats = deepcopy(_seats)
    for w in range(min_dim[0], max_dim[0]+1):
        for z in range(min_dim[1], max_dim[1]+1):
            for y in range(min_dim[2], max_dim[2]+1):
                for x in range(min_dim[3], max_dim[3]+1):
                    adj = neighbors(_seats, x, y, z, w)
                    cur_coord = (w, z, y, x)
                    cur = _seats[cur_coord]
                    if cur == True:
                        if adj not in (2, 3):
                            nu_seats[cur_coord] = False
                    if cur == False and adj == 3:
                        nu_seats[cur_coord] = True
                        # fmt: off
                        nu_min_dim, nu_max_dim = expand_world_bounds(cur_coord, nu_min_dim, nu_max_dim)
    # print(list(zip(nu_min_dim, nu_max_dim)))
    return nu_seats, nu_min_dim, nu_max_dim


def active(seats):
    tot = 0
    for i in seats.values():
        if i:
            tot += 1
    return tot


# print(active(worldd))
for i in range(6):
    worldd, min_dim, max_dim = round(worldd, min_dim, max_dim)
    acc = active(worldd)
    # print(acc, 'now active')
    # print(list(zip(min_dim,max_dim)))

# ans(acc) # part 2: 1632
# print(acc)
result2 = acc

print(result1,result2)