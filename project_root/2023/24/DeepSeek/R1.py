import sympy as sp
import sys

def part1(puzzle_input, test_input=False):
    hailstones = []
    for line in puzzle_input.split('\n'):
        if not line:
            continue
        nums = line.replace('@', ',').split(',')
        hailstones.append(tuple(map(int, nums)))
    
    if test_input:
        lo_int, hi_int = 7, 27
    else:
        lo_int, hi_int = 200000000000000, 400000000000000
        
    total = 0
    n = len(hailstones)
    for i in range(n):
        for j in range(i+1, n):
            h1 = hailstones[i]
            h2 = hailstones[j]
            x1, y1, _, dx1, dy1, _ = h1
            x2, y2, _, dx2, dy2, _ = h2
            
            denominator = dx2 * dy1 - dx1 * dy2
            if denominator == 0:
                continue
                
            numerator_t = (x1 - x2) * dy2 + (y2 - y1) * dx2
            numerator_s = (x1 - x2) * dy1 + (y2 - y1) * dx1
            
            if (numerator_t * denominator < 0) or (numerator_s * denominator < 0):
                continue
                
            X = x1 * denominator + numerator_t * dx1
            Y = y1 * denominator + numerator_t * dy1
            
            if denominator > 0:
                if not (lo_int * denominator <= X <= hi_int * denominator):
                    continue
                if not (lo_int * denominator <= Y <= hi_int * denominator):
                    continue
            else:
                if not (hi_int * denominator <= X <= lo_int * denominator):
                    continue
                if not (hi_int * denominator <= Y <= lo_int * denominator):
                    continue
                    
            total += 1
            
    return total

def part2(puzzle_input):
    first_three_hailstones = []
    for line in puzzle_input.split('\n')[:3]:
        if not line:
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