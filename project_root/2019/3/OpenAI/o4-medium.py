import sys

with open(sys.argv[1]) as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()

d = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

x = y = s = 0
m1 = {}
for ins in line1.split(','):
    dx, dy = d[ins[0]]
    l = int(ins[1:])
    for _ in range(l):
        x += dx; y += dy; s += 1
        if (x, y) not in m1:
            m1[(x, y)] = s

x = y = s = 0
seen = set()
md = ms = 10**18
for ins in line2.split(','):
    dx, dy = d[ins[0]]
    l = int(ins[1:])
    for _ in range(l):
        x += dx; y += dy; s += 1
        p = (x, y)
        if p in m1 and p not in seen:
            seen.add(p)
            dist = abs(x) + abs(y)
            if dist < md: md = dist
            total = s + m1[p]
            if total < ms: ms = total

sys.stdout.write(f"{md} {ms}")