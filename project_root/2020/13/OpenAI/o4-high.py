import sys
lines = open(sys.argv[1]).read().splitlines()
start = int(lines[0])
parts = lines[1].split(',')
min_wait = float('inf')
bus0 = 0
t = 0
step = 1
for i, x in enumerate(parts):
    if x != 'x':
        v = int(x)
        w = v - start % v
        if w < min_wait:
            min_wait = w
            bus0 = v
        while (t + i) % v:
            t += step
        step *= v
print(min_wait * bus0, t)