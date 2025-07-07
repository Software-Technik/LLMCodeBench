import sys
import re
from collections import namedtuple

Cube = namedtuple('Cube', 'x1 x2 y1 y2 z1 z2')

def intersect(a, b):
    x1 = max(a.x1, b.x1)
    x2 = min(a.x2, b.x2)
    y1 = max(a.y1, b.y1)
    y2 = min(a.y2, b.y2)
    z1 = max(a.z1, b.z1)
    z2 = min(a.z2, b.z2)
    if x1 <= x2 and y1 <= y2 and z1 <= z2:
        return Cube(x1, x2, y1, y2, z1, z2)
    return None

def volume(c):
    return (c.x2 - c.x1 + 1) * (c.y2 - c.y1 + 1) * (c.z2 - c.z1 + 1)

def solve(data, limit=None):
    steps = []
    for line in data:
        t, *nums = re.match(r'(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', line).groups()
        cube = Cube(*map(int, nums))
        if limit:
            lim = Cube(-limit, limit, -limit, limit, -limit, limit)
            c = intersect(cube, lim)
            if not c: continue
            cube = c
        steps.append((t=='on', cube))
    cuboids = []
    for on, cube in steps:
        additions = []
        for existing, sign in cuboids:
            inter = intersect(existing, cube)
            if inter:
                additions.append((inter, -sign))
        if on:
            additions.append((cube, 1))
        cuboids.extend(additions)
    return sum(sign * volume(c) for c, sign in cuboids)

data = sys.stdin.read().splitlines()
p1 = solve(data, limit=50)
p2 = solve(data, limit=None)
print(p1, p2)