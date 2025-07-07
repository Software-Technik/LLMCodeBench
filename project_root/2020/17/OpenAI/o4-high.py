import sys
from itertools import product

lines = open(sys.argv[1]).read().splitlines()

active3 = set()
active4 = set()
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch == '#':
            active3.add((x, y, 0))
            active4.add((x, y, 0, 0))

offsets3 = [o for o in product((-1,0,1), repeat=3) if o != (0,0,0)]
offsets4 = [o for o in product((-1,0,1), repeat=4) if o != (0,0,0,0)]

def simulate(active, offsets):
    counts = {}
    for coord in active:
        for o in offsets:
            n = tuple(c+o_i for c, o_i in zip(coord, o))
            counts[n] = counts.get(n, 0) + 1
    return {c for c, cnt in counts.items() if cnt == 3 or (cnt == 2 and c in active)}

for _ in range(6):
    active3 = simulate(active3, offsets3)
res1 = len(active3)

for _ in range(6):
    active4 = simulate(active4, offsets4)
res2 = len(active4)

print(res1, res2)