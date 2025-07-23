import re
import numpy as np

def part1(data):
    steps = [re.match(r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$', line).groups() for line in data]
    DIM = 50
    grid = np.zeros((2 * DIM + 1,) * 3, dtype=int)
    for toggle, x1, x2, y1, y2, z1, z2 in steps:
        x1, x2 = int(x1) + DIM, int(x2) + DIM
        y1, y2 = int(y1) + DIM, int(y2) + DIM
        z1, z2 = int(z1) + DIM, int(z2) + DIM
        if all(0 <= s < 2 * DIM + 1 for s in (x1, x2, y1, y2, z1, z2)):
            grid[x1:x2+1, y1:y2+1, z1:z2+1] = toggle == "on"
    return np.sum(grid)

def part2(data):
    steps = [(toggle == 'on', *map(int, re.match(r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$',
                                                 line).groups())) for line in data]

    xs = sorted({cube[x] for _, *cube in steps for x in (0, 1)} | {cube[0]-1, cube[-1]+1 for _, *cube in steps})
    ys = sorted({cube[y] for _, *cube in steps for y in (2, 3)} | {cube[2]-1, cube[-2]+1 for _, *cube in steps})
    zs = sorted({cube[z] for _, *cube in steps for z in (4, 5)} | {cube[4]-1, cube[-3]+1 for _, *cube in steps})

    xi, yi, zi = {x: i for i, x in enumerate(xs)}, {y: i for i, y in enumerate(ys)}, {z: i for i, z in enumerate(zs)}
    grid = np.zeros((len(xi) - 1, len(yi) - 1, len(zi) - 1), dtype=bool)

    for toggle, x1, x2, y1, y2, z1, z2 in steps:
        grid[xi[x1]:xi[x2 + 1], yi[y1]:yi[y2 + 1], zi[z1]:zi[z2 + 1]] = toggle

    dx, dy, dz = np.diff(xs), np.diff(ys), np.diff(zs)
    total = sum(dx[i] * (grid[i].sum() * dy @ dz) for i in range(len(xi) - 1))
    return int(total)

with open(sys.argv[1]) as f:
    data = f.readlines()

print(part1(data), part2(data))