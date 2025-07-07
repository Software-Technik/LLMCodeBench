import sys
from math import isqrt

data = open(sys.argv[1]).read().splitlines()

def parse(line):
    nums = list(map(int, line.replace('p=<','').replace('>','').replace('v=<','').replace('a=<','').replace('>','').split(',')))
    return tuple(nums[0:3]), tuple(nums[3:6]), tuple(nums[6:9])

particles = [parse(l) for l in data]

def mag(v): return v[0]*v[0]+v[1]*v[1]+v[2]*v[2]

print(min(range(len(particles)), key=lambda i: mag(particles[i][2])))

def pos(coord, t):
    p, v, a = coord
    return p + v*t + a*t*(t+1)//2

def times(p1, p2):
    res = set()
    for axis in range(3):
        p = p1[0][axis] - p2[0][axis]
        v = p1[1][axis] - p2[1][axis]
        a = p1[2][axis] - p2[2][axis]
        b = 2*v + a
        c = 2*p
        ts = set()
        if a == 0:
            if b != 0:
                if -c % b == 0:
                    t = -c//b
                    if t>=0: ts.add(t)
        else:
            D = b*b - 4*a*c
            if D >= 0:
                sd = isqrt(D)
                if sd*sd == D:
                    for s in (sd, -sd):
                        num = -b + s
                        den = 2*a
                        if den != 0 and num % den == 0:
                            t = num//den
                            if t>=0: ts.add(t)
        if not ts:
            return set()
        if axis == 0:
            res = ts
        else:
            res &= ts
        if not res:
            return set()
    return res

coll = {}
n = len(particles)
for i in range(n):
    for j in range(i+1, n):
        ts = times(particles[i], particles[j])
        for t in ts:
            coll.setdefault(t, []).append((i,j))

dead = set()
for t in sorted(coll):
    s = set()
    for i,j in coll[t]:
        if i not in dead and j not in dead:
            s.add(i); s.add(j)
    dead |= s

print(n - len(dead))