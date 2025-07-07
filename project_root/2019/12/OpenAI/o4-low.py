import sys
from math import gcd
from functools import reduce

def lcm(a, b): return a * b // gcd(a, b)
def lcm3(a, b, c): return lcm(lcm(a, b), c)

def part1(px, py, pz):
    vx = [0]*4; vy = [0]*4; vz = [0]*4
    for _ in range(1000):
        for i in range(4):
            for j in range(i+1, 4):
                if px[i] < px[j]: vx[i]+=1; vx[j]-=1
                elif px[i] > px[j]: vx[i]-=1; vx[j]+=1
                if py[i] < py[j]: vy[i]+=1; vy[j]-=1
                elif py[i] > py[j]: vy[i]-=1; vy[j]+=1
                if pz[i] < pz[j]: vz[i]+=1; vz[j]-=1
                elif pz[i] > pz[j]: vz[i]-=1; vz[j]+=1
        for i in range(4):
            px[i]+=vx[i]; py[i]+=vy[i]; pz[i]+=vz[i]
    e=0
    for i in range(4):
        pot=abs(px[i])+abs(py[i])+abs(pz[i])
        kin=abs(vx[i])+abs(vy[i])+abs(vz[i])
        e+=pot*kin
    return e

def period(axis):
    p = axis[:]
    v = [0]*4
    seen = tuple(p+v)
    steps=0
    while True:
        steps+=1
        for i in range(4):
            for j in range(i+1,4):
                if p[i]<p[j]: v[i]+=1; v[j]-=1
                elif p[i]>p[j]: v[i]-=1; v[j]+=1
        for i in range(4): p[i]+=v[i]
        state = tuple(p+v)
        if state==seen: return steps

fn = sys.argv[1]
with open(fn) as f:
    px=[]; py=[]; pz=[]
    for line in f:
        x,y,z = line.strip('<>\n').split(', ')
        px.append(int(x.split('=')[1]))
        py.append(int(y.split('=')[1]))
        pz.append(int(z.split('=')[1]))

res1 = part1(px[:], py[:], pz[:])
px2,py2,pz2 = px[:], py[:], pz[:]
tx = period(px2); ty = period(py2); tz = period(pz2)
res2 = lcm3(tx, ty, tz)
print(res1, res2)