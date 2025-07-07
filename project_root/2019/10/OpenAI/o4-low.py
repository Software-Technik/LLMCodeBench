import sys
from math import gcd, atan2, pi

def part1(asteroids):
    best = 0
    for x0,y0 in asteroids:
        dirs = set()
        for x1,y1 in asteroids:
            if x0==x1 and y0==y1: continue
            dx,dy = x1-x0,y1-y0
            g = gcd(dx,dy)
            dirs.add((dx//g,dy//g))
        if len(dirs)>best: best = len(dirs)
    return best

def part2(asteroids):
    best = 0; station = None
    for x0,y0 in asteroids:
        dirs = set()
        for x1,y1 in asteroids:
            if x0==x1 and y0==y1: continue
            dx,dy = x1-x0,y1-y0
            g = gcd(dx,dy)
            dirs.add((dx//g,dy//g))
        if len(dirs)>best:
            best = len(dirs); station=(x0,y0)
    sx,sy = station
    d = {}
    for x,y in asteroids:
        if x==sx and y==sy: continue
        dx,dy = x-sx, y-sy
        ang = atan2(dx, -dy)
        if ang<0: ang+=2*pi
        d.setdefault(ang, []).append((dx*dx+dy*dy, x, y))
    for lst in d.values():
        lst.sort()
    angles = sorted(d.keys())
    count = 0
    while True:
        for ang in angles:
            lst = d[ang]
            if lst:
                count+=1
                dist,x,y = lst.pop(0)
                if count==200:
                    return x*100+y

data = list(open(sys.argv[1]).read().splitlines())
asteroids = [(x,y) for y,row in enumerate(data) for x,c in enumerate(row) if c=='#']
res1 = part1(asteroids)
res2 = part2(asteroids)
sys.stdout.write(f"{res1} {res2}")