import sys
from itertools import combinations

def part1(puzzle_input, test_input=False):
    lines = puzzle_input.splitlines()
    hail = []
    for line in lines:
        x,y,_,dx,dy,_ = map(int, line.replace('@',',').split(','))
        m = dy/dx
        hail.append((x, m, y - m*x, dx))
    lo,hi = (7,27) if test_input else (2e14,4e14)
    total = 0
    n = len(hail)
    for i in range(n):
        x1, m1, b1, dx1 = hail[i]
        for j in range(i+1, n):
            x2, m2, b2, dx2 = hail[j]
            if m1 == m2: continue
            x = (b2 - b1) / (m1 - m2)
            y = m1*x + b1
            if lo <= x <= hi and lo <= y <= hi and (x - x1)*dx1 > 0 and (x - x2)*dx2 > 0:
                total += 1
    return total

def part2(puzzle_input):
    import sympy as sp
    data = [tuple(map(int, line.replace('@',',').split(','))) for line in puzzle_input.splitlines()[:3]]
    unknowns = sp.symbols('x y z dx dy dz t1 t2 t3')
    x,y,z,dx,dy,dz,t1,t2,t3 = unknowns
    eqs = []
    for t_sym,(xi,yi,zi,dxi,dyi,dzi) in zip((t1,t2,t3), data):
        eqs.append(sp.Eq(x + t_sym*dx, xi + t_sym*dxi))
        eqs.append(sp.Eq(y + t_sym*dy, yi + t_sym*dyi))
        eqs.append(sp.Eq(z + t_sym*dz, zi + t_sym*dzi))
    sol = sp.solve(eqs, unknowns).pop()
    return sol[0] + sol[1] + sol[2]

if __name__=='__main__':
    text = open(sys.argv[1]).read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")