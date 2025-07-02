import sys
import re
import numpy as np
from dataclasses import dataclass


def part1(data):
    regex = r"^(on|off) x=([0-9-]+)\.\.([0-9-]+),y=([0-9-]+)\.\.([0-9-]+),z=([0-9-]+)\.\.([0-9-]+)$"
    steps = [re.match(regex, line).groups() for line in data]

    DIM = 50
    grid = np.zeros((2 * DIM + 1, 2 * DIM + 1, 2 * DIM + 1), dtype=int)

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

    # possible positions along the x, y and z axises
    xs = sorted({cube.x1 - 1 for _, cube in steps} | {cube.x1 for _, cube in steps} | {cube.x1 + 1 for _, cube in steps} | {cube.x2 - 1 for _, cube in steps} | {cube.x2 for _, cube in steps} | {cube.x2 + 1 for _, cube in steps})
    ys = sorted({cube.y1 - 1 for _, cube in steps} | {cube.y1 for _, cube in steps} | {cube.y1 + 1 for _, cube in steps} | {cube.y2 - 1 for _, cube in steps} | {cube.y2 for _, cube in steps} | {cube.y2 + 1 for _, cube in steps})
    zs = sorted({cube.z1 - 1 for _, cube in steps} | {cube.z1 for _, cube in steps} | {cube.z1 + 1 for _, cube in steps} | {cube.z2 - 1 for _, cube in steps} | {cube.z2 for _, cube in steps} | {cube.z2 + 1 for _, cube in steps})

    # map positions to indexes
    xi = {x: i for i, x in enumerate(xs)}
    yi = {y: i for i, y in enumerate(ys)}
    zi = {z: i for i, z in enumerate(zs)}

    # Turn on/off reactor cubes
    grid = np.zeros((len(xi) - 1, len(yi) - 1, len(zi) - 1), dtype=bool)
    for toggle, cube in steps:
        x1 = xi[cube.x1]
        x2 = xi[cube.x2 + 1]
        y1 = yi[cube.y1]
        y2 = yi[cube.y2 + 1]
        z1 = zi[cube.z1]
        z2 = zi[cube.z2 + 1]
        grid[x1:x2, y1:y2, z1:z2] = toggle

    # Compute deltas of each reactor cube,
    # weight of the cube located at (i, j, k) is then dx[i] * dy[j] * dz[k]
    dx = [xs[i + 1] - xs[i] for i in range(len(xs) - 1)]
    dy = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]
    dz = [zs[i + 1] - zs[i] for i in range(len(zs) - 1)]

    # Compute the total number of activated reactor cubes
    # To save memory, we compute the total by slicing the grid on first dimension
    total = 0
    d = np.array([dy]).T * np.array([dz])
    for i in range(grid.shape[0]):
        total += dx[i] * int(np.sum(grid[i, :, :] * d, dtype=np.int64))
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")