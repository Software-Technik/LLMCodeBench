import sys
from math import gcd
def lcm(a,b):return a*b//gcd(a,b)
def part1(px,py,pz):
    vx=[0]*4;vy=[0]*4;vz=[0]*4
    for _ in range(1000):
        for i in range(4):
            for j in range(i+1,4):
                if px[i]<px[j]:vx[i]+=1;vx[j]-=1
                elif px[i]>px[j]:vx[i]-=1;vx[j]+=1
                if py[i]<py[j]:vy[i]+=1;vy[j]-=1
                elif py[i]>py[j]:vy[i]-=1;vy[j]+=1
                if pz[i]<pz[j]:vz[i]+=1;vz[j]-=1
                elif pz[i]>pz[j]:vz[i]-=1;vz[j]+=1
        for i in range(4):
            px[i]+=vx[i];py[i]+=vy[i];pz[i]+=vz[i]
    e=0
    for i in range(4):
        e+=(abs(px[i])+abs(py[i])+abs(pz[i]))*(abs(vx[i])+abs(vy[i])+abs(vz[i]))
    return e
def period_axis(p):
    v=[0]*4;init=p.copy();step=0
    while 1:
        step+=1
        for i in range(4):
            for j in range(i+1,4):
                if p[i]<p[j]:v[i]+=1;v[j]-=1
                elif p[i]>p[j]:v[i]-=1;v[j]+=1
        for i in range(4):p[i]+=v[i]
        if p==init and v==[0]*4:return step
def part2(px,py,pz):
    return lcm(lcm(period_axis(px.copy()),period_axis(py.copy())),period_axis(pz.copy()))
lines=open(sys.argv[1]).read().strip().splitlines()
px=[];py=[];pz=[]
for line in lines:
    a,b,c=line[1:-1].split(', ')
    px.append(int(a.split('=')[1]));py.append(int(b.split('=')[1]));pz.append(int(c.split('=')[1]))
p1=part1(px.copy(),py.copy(),pz.copy())
p2=part2(px,py,pz)
sys.stdout.write(f"{p1} {p2}")