import sys
d = {'n': (0, -1), 'nw': (-1, 0), 'sw': (-1, 1), 's': (0, 1), 'se': (1, 0), 'ne': (1, -1)}
with open(sys.argv[1]) as f:
    ins = f.read().strip().split(',')
x = y = 0
m = 0
for s in ins:
    dx, dy = d[s]; x += dx; y += dy
    a = abs(x); b = abs(y); c = abs(x + y)
    dist = a if a > b else b
    if c > dist: dist = c
    if dist > m: m = dist
a = abs(x); b = abs(y); c = abs(x + y)
dist = a if a > b else b
if c > dist: dist = c
print(dist)
print(m)