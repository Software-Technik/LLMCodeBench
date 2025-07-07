import sys
lines = [l.strip() for l in open(sys.argv[1])]
n, m = len(lines), len(lines[0])
infected0 = {complex(i, j) for i, line in enumerate(lines) for j, ch in enumerate(line) if ch == '#'}
start = complex(n//2, m//2)
start_dir = complex(-1, 0)
grid = infected0.copy()
pos = start; d = start_dir; inf = 0
for _ in range(10000):
    if pos not in grid:
        d *= 1j; grid.add(pos); inf += 1
    else:
        d *= -1j; grid.remove(pos)
    pos += d
print(inf)
grid = {p:2 for p in infected0}
pos = start; d = start_dir; inf = 0
get = grid.get; pop = grid.pop; setitem = grid.__setitem__
for _ in range(10000000):
    s = get(pos, 0)
    if s == 0:
        d *= 1j
    elif s == 1:
        inf += 1
    elif s == 2:
        d *= -1j
    else:
        d *= -1
    ns = (s+1) & 3
    if ns:
        setitem(pos, ns)
    else:
        pop(pos, None)
    pos += d
print(inf)