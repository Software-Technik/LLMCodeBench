from itertools import combinations
import sympy as sp
import sys


def part1(puzzle_input, test_input=False):
    hailstones = []
    for line in puzzle_input.split('\n'):
        if not line.strip():
            continue
        nums = line.replace('@', ',').split(',')
        hailstones.append(tuple(map(int, nums)))

    if test_input:
        lo, hi = 7, 27
    else:
        lo, hi = 200000000000000, 400000000000000
        
    total = 0
    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, dx1, dy1, _ = h1
        x2, y2, _, dx2, dy2, _ = h2
        
        denom = dx1 * dy2 - dx2 * dy1
        if denom == 0:
            continue
        
        t1 = (dx2 * (y1 - y2) - dy2 * (x1 - x2)) / denom
        t2 = (dx1 * (y1 - y2) - dy1 * (x1 - x2)) / denom
        
        if t1 < 0 or t2 < 0:
            continue
        
        x = x1 + t1 * dx1
        y = y1 + t1 * dy1
        
        if lo <= x <= hi and lo <= y <= hi:
            total += 1

    return total


def part2(puzzle_input):
    first_three_hailstones = []
    for line in puzzle_input.split('\n')[:3]:
        if not line.strip():
            continue
        nums = line.replace('@', ',').split(',')
        first_three_hailstones.append(tuple(map(int, nums)))

    unknowns = sp.symbols('x y z dx dy dz t1 t2 t3')
    x, y, z, dx, dy, dz, *time = unknowns

    equations = []
    for t, h in zip(time, first_three_hailstones):
        equations.append(sp.Eq(x + t*dx, h[0] + t*h[3]))
        equations.append(sp.Eq(y + t*dy, h[1] + t*h[4]))
        equations.append(sp.Eq(z + t*dz, h[2] + t*h[5]))

    solution = sp.solve(equations, unknowns).pop()
    return sum(solution[:3])


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")