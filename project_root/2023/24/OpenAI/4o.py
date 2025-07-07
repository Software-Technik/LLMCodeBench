from itertools import combinations
import sympy as sp
import sys

def part1(puzzle_input, test_input=False):
    hailstones = [tuple(map(int, line.replace('@', ',').split(','))) for line in puzzle_input.split('\n') if line]

    lo, hi = (7, 27) if test_input else (2e14, 4e14)
        
    total = 0
    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, dx1, dy1, _ = h1
        x2, y2, _, dx2, dy2, _ = h2
        m1, m2 = dy1 / dx1, dy2 / dx2
        if m1 == m2:
            continue
        x = ((y2 - m2 * x2) - (y1 - m1 * x1)) / (m1 - m2)
        y = m1 * x + y1 - m1 * x1
        if all((lo <= x <= hi, lo <= y <= hi,
                (x > x1 and dx1 > 0) or (x < x1 and dx1 < 0),
                (x > x2 and dx2 > 0) or (x < x2 and dx2 < 0))):
            total += 1

    return total

def part2(puzzle_input):
    first_three_hailstones = [tuple(map(int, line.replace('@', ',').split(','))) for line in puzzle_input.split('\n')[:3]]

    x, y, z, dx, dy, dz, t1, t2, t3 = sp.symbols('x y z dx dy dz t1 t2 t3')
    unknowns = (x, y, z, dx, dy, dz, t1, t2, t3)

    equations = []
    for t, h in zip((t1, t2, t3), first_three_hailstones):
        equations.extend([sp.Eq(x + t*dx, h[0] + t*h[3]),
                          sp.Eq(y + t*dy, h[1] + t*h[4]),
                          sp.Eq(z + t*dz, h[2] + t*h[5])])

    solution = sp.solve(equations, unknowns).pop()
    return sum(solution[:3])

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")