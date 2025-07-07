import sys
dirs = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
with open(sys.argv[1]) as f:
    data = f.read().splitlines()
ins1 = data[0].split(','); ins2 = data[1].split(',')
d1 = {}
x = y = steps1 = 0
for ins in ins1:
    dx, dy = dirs[ins[0]]; l = int(ins[1:])
    for _ in range(l):
        x += dx; y += dy; steps1 += 1
        if (x, y) not in d1:
            d1[(x, y)] = steps1
d1_get = d1.get; abs_ = abs
x = y = steps2 = 0
best1 = best2 = float('inf')
for ins in ins2:
    dx, dy = dirs[ins[0]]; l = int(ins[1:])
    for _ in range(l):
        x += dx; y += dy; steps2 += 1
        v = d1_get((x, y))
        if v is not None:
            dist = abs_(x) + abs_(y)
            if dist < best1: best1 = dist
            t = steps2 + v
            if t < best2: best2 = t
sys.stdout.write(f"{best1} {best2}")