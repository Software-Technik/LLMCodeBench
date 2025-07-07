import sys
from math import gcd
def part1(data):
    pos=[list(p) for p in data]
    vel=[[0,0,0] for _ in pos]
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    for _ in range(1000):
        for i,j in pairs:
            for a in range(3):
                if pos[i][a]<pos[j][a]:
                    vel[i][a]+=1; vel[j][a]-=1
                elif pos[i][a]>pos[j][a]:
                    vel[i][a]-=1; vel[j][a]+=1
        for i in range(4):
            for a in range(3):
                pos[i][a]+=vel[i][a]
    e=0
    for i in range(4):
        pot=sum(abs(c) for c in pos[i])
        kin=sum(abs(c) for c in vel[i])
        e+=pot*kin
    return e

def part2(data):
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    def cycle(axis):
        p=[p0[axis] for p0 in data]
        v=[0]*4
        init_p=tuple(p); init_v=tuple(v)
        step=0
        while True:
            for i,j in pairs:
                if p[i]<p[j]:
                    v[i]+=1; v[j]-=1
                elif p[i]>p[j]:
                    v[i]-=1; v[j]+=1
            for i in range(4):
                p[i]+=v[i]
            step+=1
            if tuple(p)==init_p and tuple(v)==init_v:
                return step
    x=cycle(0); y=cycle(1); z=cycle(2)
    def lcm(a,b): return a*b//gcd(a,b)
    return lcm(lcm(x,y),z)

with open(sys.argv[1]) as f:
    positions=[]
    for line in f:
        x,y,z=map(int,(line[line.find('=')+1:line.find(',')],line[line.find('y=')+2:line.rfind(',')],line[line.find('z=')+2:line.rfind('>')]))
        positions.append((x,y,z))
sys.stdout.write(f"{part1(positions)} {part2(positions)}")