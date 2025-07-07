import sys
from collections import deque
from math import gcd

data = [line.rstrip('\n') for line in open(sys.argv[1])]
H = len(data); W = len(data[0])
H2 = H - 2; W2 = W - 2
period = H2 * W2 // gcd(H2, W2)
start_c = data[0].index('.'); goal_c = data[-1].index('.')
start = start_c; goal = (H - 1) * W + goal_c
dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
blizz = []
for r in range(1, H - 1):
    for c, ch in enumerate(data[r][1:-1], 1):
        if ch in dirs:
            dr, dc = dirs[ch]
            blizz.append((r, c, dr, dc))
blizz_sets = [set() for _ in range(period)]
for t in range(period):
    s = blizz_sets[t]
    for r, c, dr, dc in blizz:
        rr = (r - 1 + dr * t) % H2 + 1
        cc = (c - 1 + dc * t) % W2 + 1
        s.add(rr * W + cc)
HW = H * W
valid = set(r * W + c for r in range(1, H - 1) for c in range(1, W - 1))
valid.add(start); valid.add(goal)

def bfs(s, g, t0):
    visited = set([s + (t0 % period) * HW])
    dq = deque([(s, t0)])
    while dq:
        pos, t = dq.popleft()
        if pos == g:
            return t
        t1 = t + 1; bs = blizz_sets[t1 % period]; m = t1 % period
        for offset in (0, 1, W, -1, -W):
            npos = pos + offset
            if npos in valid and npos not in bs:
                vid = npos + m * HW
                if vid not in visited:
                    visited.add(vid)
                    dq.append((npos, t1))
    return -1

p1 = bfs(start, goal, 0)
p2 = bfs(goal, start, p1)
p3 = bfs(start, goal, p2)
print(p1, p3, sep='\n')