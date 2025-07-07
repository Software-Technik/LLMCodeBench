#!/usr/bin/env python3
import sys

def parse(text):
    lines = text.strip().splitlines()
    w = len(lines[0].strip())
    grid = set()
    start = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == '#':
                grid.add(y * w + x)
            elif c == 'S':
                start = y * w + x
    return grid, start, w

data = open(sys.argv[1]).read()
grid, start, W = parse(data)
deltas = (1, -1, W, -W)

cur = {start}
for _ in range(64):
    nxt = set()
    g = grid
    for p in cur:
        for d in deltas:
            np = p + d
            if np not in g:
                nxt.add(np)
    cur = nxt
p1 = len(cur)

cur = {start}
pts = []
step = 0
half = W // 2
target = 26501365
g = grid
w = W
while len(pts) < 3:
    step += 1
    nxt = set()
    for p in cur:
        for d in deltas:
            n = p + d
            x = n % w
            y = (n // w) % w
            if y * w + x not in g:
                nxt.add(n)
    cur = nxt
    if (step - half) % w == 0:
        pts.append(len(cur))

c, b, a = pts[0], pts[1] - pts[0], pts[2] - pts[1]
x = target // W
p2 = c + b * x + (x * (x - 1) // 2) * (a - b)

sys.stdout.write(f"{p1} {p2}")