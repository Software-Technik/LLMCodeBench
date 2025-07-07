import sys
import sympy as sp

lines = open(sys.argv[1]).read().splitlines()
h_full = [tuple(map(int, line.replace('@',',').split(','))) for line in lines]
hs = [(x,y,dx,dy,dy/dx,y-(dy/dx)*x) for x,y,_,dx,dy,_ in h_full]
lo, hi = 2e14, 4e14
tot = 0
n = len(hs)
for i in range(n):
    x1,y1,dx1,dy1,m1,b1 = hs[i]
    for j in range(i):
        x2,y2,dx2,dy2,m2,b2 = hs[j]
        if dy1*dx2 == dy2*dx1: continue
        xi = (b2 - b1)/(m1 - m2)
        yi = m1*xi + b1
        if lo <= xi <= hi and lo <= yi <= hi and ((xi > x1 and dx1 > 0) or (xi < x1 and dx1 < 0)) and ((xi > x2 and dx2 > 0) or (xi < x2 and dx2 < 0)):
            tot += 1

x,y,z,dx,dy,dz,t1,t2,t3 = sp.symbols('x y z dx dy dz t1 t2 t3')
eqs = []
for (xi,yi,zi,dxi,dyi,dzi), tt in zip(h_full[:3], (t1,t2,t3)):
    eqs += [sp.Eq(x+tt*dx, xi+tt*dxi), sp.Eq(y+tt*dy, yi+tt*dyi), sp.Eq(z+tt*dz, zi+tt*dzi)]
sol = sp.solve(eqs, (x,y,z,dx,dy,dz,t1,t2,t3), dict=True)[0]
res2 = sol[x] + sol[y] + sol[z]

sys.stdout.write(f"{tot} {res2}")