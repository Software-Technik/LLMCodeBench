import sys
lines = open(sys.argv[1]).read().strip().splitlines()
H = len(lines)
W = len(lines[0])
static_x = {}
static_y = {}
D0 = set()
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch == 'O':
            D0.add((x, y))
        elif ch != '.':
            static_x.setdefault(x, []).append(y)
            static_y.setdefault(y, []).append(x)
static_x_bounds = {x: [-1] + sorted(static_x.get(x, [])) + [H] for x in range(W)}
static_y_bounds = {y: [-1] + sorted(static_y.get(y, [])) + [W] for y in range(H)}
def pack_vertical(D, d):
    newD = set()
    bycol = {}
    for x, y in D:
        bycol.setdefault(x, []).append(y)
    for x, ys in bycol.items():
        ys.sort()
        bounds = static_x_bounds[x]
        di = 0; n = len(ys)
        for bi in range(len(bounds) - 1):
            low = bounds[bi]; high = bounds[bi + 1]; cnt = 0
            while di < n and low < ys[di] < high:
                cnt += 1; di += 1
            if cnt:
                if d < 0:
                    for k in range(1, cnt + 1):
                        newD.add((x, low + k))
                else:
                    for k in range(1, cnt + 1):
                        newD.add((x, high - k))
    return newD
def pack_horizontal(D, d):
    newD = set()
    byrow = {}
    for x, y in D:
        byrow.setdefault(y, []).append(x)
    for y, xs in byrow.items():
        xs.sort()
        bounds = static_y_bounds[y]
        di = 0; n = len(xs)
        for bi in range(len(bounds) - 1):
            low = bounds[bi]; high = bounds[bi + 1]; cnt = 0
            while di < n and low < xs[di] < high:
                cnt += 1; di += 1
            if cnt:
                if d < 0:
                    for k in range(1, cnt + 1):
                        newD.add((low + k, y))
                else:
                    for k in range(1, cnt + 1):
                        newD.add((high - k, y))
    return newD
D1 = pack_vertical(D0, -1)
part1 = sum(H - y for x, y in D1)
TOTAL = 10**9
D = set(D0)
states = {}
cycles = 0
direction = 0
while True:
    if direction == 0:
        if states is not None:
            sig = frozenset(D)
            if sig in states:
                prev = states[sig]
                period = cycles - prev
                rem = (TOTAL - cycles) % period
                cycles = TOTAL - rem
                states = None
            else:
                states[sig] = cycles
        D = pack_vertical(D, -1)
    elif direction == 1:
        D = pack_horizontal(D, -1)
    elif direction == 2:
        D = pack_vertical(D, 1)
    else:
        D = pack_horizontal(D, 1)
        cycles += 1
        if cycles == TOTAL:
            part2 = sum(H - y for x, y in D)
            break
    direction = (direction + 1) % 4
sys.stdout.write(f"{part1} {part2}")