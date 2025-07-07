import sys
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
x = y = 0
d = 0
dirs = [(1,0),(0,-1),(-1,0),(0,1)]
for l in lines:
    c = l[0]; v = int(l[1:])
    if c == 'N': y -= v
    elif c == 'S': y += v
    elif c == 'E': x += v
    elif c == 'W': x -= v
    elif c == 'L': d = (d + v//90) & 3
    elif c == 'R': d = (d - v//90) & 3
    else:
        dx, dy = dirs[d]
        x += dx * v; y += dy * v
r1 = abs(x) + abs(y)
x = y = 0
wx, wy = 10, -1
for l in lines:
    c = l[0]; v = int(l[1:])
    if c == 'N': wy -= v
    elif c == 'S': wy += v
    elif c == 'E': wx += v
    elif c == 'W': wx -= v
    elif c in ('L','R'):
        k = v//90
        if c == 'L': k = (4 - k) & 3
        for _ in range(k):
            wx, wy = -wy, wx
    else:
        x += wx * v; y += wy * v
r2 = abs(x) + abs(y)
print(r1, r2)