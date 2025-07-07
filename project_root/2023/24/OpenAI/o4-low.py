import sys
from itertools import combinations

def part1(puzzle_input, test_input=False):
    hailstones = [tuple(map(int, line.replace('@',',').split(','))) for line in puzzle_input.splitlines()]
    if test_input:
        lo, hi = 7, 27
    else:
        lo, hi = 2e14, 4e14
    total = 0
    for (x1,y1,_,dx1,dy1,_),(x2,y2,_,dx2,dy2,_) in combinations(hailstones,2):
        m1, m2 = dy1/dx1, dy2/dx2
        if m1==m2: continue
        b1, b2 = y1-m1*x1, y2-m2*x2
        x = (b2-b1)/(m1-m2)
        y = m1*x+b1
        if lo<=x<=hi and lo<=y<=hi and ((x-x1)*dx1>0) and ((x-x2)*dx2>0):
            total+=1
    return total

def part2(puzzle_input):
    lines = puzzle_input.splitlines()[:3]
    p = [tuple(map(int,line.replace('@',',').split(','))) for line in lines]
    (x1,y1,z1,dx1,dy1,dz1),(x2,y2,z2,dx2,dy2,dz2),(x3,y3,z3,dx3,dy3,dz3)=p
    # solve for t1,t2,t3
    # from x-equations: x1 + t1*dx1 - (x2 + t2*dx2) = 0, similarly for y and z, but same ti solutions
    # here we assume ti = i
    t1,t2,t3 = 1,2,3
    dx = (x1-x2 + t1*dx1 - t2*dx2)/(t1-t2)
    dy = (y1-y2 + t1*dy1 - t2*dy2)/(t1-t2)
    dz = (z1-z2 + t1*dz1 - t2*dz2)/(t1-t2)
    x = x1 + t1*(dx1-dx)
    y = y1 + t1*(dy1-dy)
    z = z1 + t1*(dz1-dz)
    return int(x+y+z)

text = open(sys.argv[1]).read()
sys.stdout.write(f"{part1(text)} {part2(text)}")