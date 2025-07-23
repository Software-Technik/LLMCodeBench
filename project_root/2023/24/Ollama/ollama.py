from itertools import combinations
import sympy as sp
import sys


def part1(puzzle_input, test_input=False):
    hailstones = [tuple(map(int, line.replace('@', ',').split(','))) for line in puzzle_input.split('\n')]

    lo, hi = (7, 27) if test_input else (2e14, 4e14)
    total = 0

    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, dx1, dy1, _ = h1
        x2, y2, _, dx2, dy2, _ = h2

        if (y2 - y1) * (dx1 - dx2) == (dy1 - dy2) * (x2 - x1):
            continue

        denom = (y2 - y1) * (dx1 - dx2) - (dy1 - dy2) * (x2 - x1)
        num_x = (y2 - y1) * (x2 - x1) - (z2 - z1) * (dx2 - dx1)
        num_y = (dx2 - dx1) * (z2 - z1) - (x2 - x1) * (dy2 - dy1)

        x = num_x / denom
        y = num_y / denom

        if all((lo <= x <= hi, lo <= y <= hi,
                (x > x1 and dx1 > 0) or (x < x1 and dx1 < 0),
                (x > x2 and dx2 > 0) or (x < x2 and dx2 < 0))):
            total += 1

    return total


def part2(puzzle_input):
    first_three_hailstones = [tuple(map(int, line.replace('@', ',').split(','))) for line in puzzle_input.split('\n')[:3]]

    unknowns = sp.symbols('x y z dx dy dz t1 t2 t3')
    x, y, z, dx, dy, dz, *time = unknowns

    equations = [sp.Eq(x + t*dx, h[0] + t*h[3]) for t, h in zip(time, first_three_hailstones)] + \
                [sp.Eq(y + t*dy, h[1] + t*h[4]) for t, h in zip(time, first_three_hailstones)] + \
                [sp.Eq(z + t*dz, h[2] + t*h[5]) for t, h in zip(time, first_three_hailstones)]

    solution = sp.solve(equations, unknowns).pop()
    return sum(solution[:3])


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")