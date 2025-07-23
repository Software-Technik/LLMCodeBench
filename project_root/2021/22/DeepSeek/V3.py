import sys
import re
import numpy as np
from dataclasses import dataclass


def part1(data):
    regex = r"^(on|off) x=([0-9-]+)\.\.([0-9-]+),y=([0-9-]+)\.\.([0-9-]+),z=([0-9-]+)\.\.([0-9-]+)$"
    steps = [re.match(regex, line).groups() for line in data]

    DIM = 50
    grid = np.zeros((2 * DIM + 1, 2 * DIM + 1, 2 * DIM + 1), dtype=bool)

    for toggle, x1, x2, y1, y2, z1, z2 in steps:
        x1, x2 = int(x1) + DIM, int(x2) + DIM
        y1, y2 = int(y1) + DIM, int(y2) + DIM
        z1, z2 = int(z1) + DIM, int(z2) + DIM
        if x1 >= 0 and x2 < 2 * DIM + 1 and y1 >= 0 and y2 < 2 * DIM + 1 and z1 >= 0 and z2 < 2 * DIM + 1:
            grid[x1:x2+1, y1:y2+1, z1:z2+1] = (toggle == "on")

    return np.sum(grid)

@dataclass
class Cube:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int


def part2(data):
    regex = r"^(on|off) x=([0-9-]+)\.\.([0-9-]+),y=([0-9-]+)\.\.([0-9-]+),z=([0-9-]+)\.\.([0-9-]+)$"
    inputs = [re.match(regex, line).groups() for line in data]
    steps = [(toggle == "on", Cube(*map(int, coords))) for toggle, *coords in inputs]

    xs = set()
    ys = set()
    zs = set()
    for _, cube in steps:
        xs.update({cube.x1 - 1, cube.x1, cube.x1 + 1, cube.x2 - 1, cube.x2, cube.x2 + 1})
        ys.update({cube.y1 - 1, cube.y1, cube.y1 + 1, cube.y2 - 1, cube.y2, cube.y2 + 1})
        zs.update({cube.z1 - 1, cube.z1, cube.z1 + 1, cube.z2 - 1, cube.z2, cube.z2 + 1})
    xs = sorted(xs)
    ys = sorted(ys)
    zs = sorted(zs)

    xi = {x: i for i, x in enumerate(xs)}
    yi = {y: i for i, y in enumerate(ys)}
    zi = {z: i for i, z in enumerate(zs)}

    grid = np.zeros((len(xi) - 1, len(yi) - 1, len(zi) - 1), dtype=bool)
    for toggle, cube in steps:
        x1 = xi[cube.x1]
        x2 = xi[cube.x2 + 1]
        y1 = yi[cube.y1]
        y2 = yi[cube.y2 + 1]
        z1 = zi[cube.z1]
        z2 = zi[cube.z2 + 1]
        grid[x1:x2, y1:y2, z1:z2] = toggle

    dx = np.diff(xs)
    dy = np.diff(ys)
    dz = np.diff(zs)

    total = 0
    dy_dz = np.outer(dy, dz)
    for i in range(grid.shape[0]):
        total += dx[i] * np.sum(grid[i] * dy_dz)
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")