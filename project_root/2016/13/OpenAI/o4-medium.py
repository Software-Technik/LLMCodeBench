import sys
from collections import deque
fav = int(open(sys.argv[1]).read())
deltas = ((1,0),(-1,0),(0,1),(0,-1))
Xg, Yg = 31, 39
q = deque([(1,1,0)])
seen = set()
goal = part2 = None
while q:
    x, y, s = q.popleft()
    if (x, y) in seen: continue
    if s > 50 and part2 is None:
        part2 = len(seen)
        if goal is not None: break
    if x == Xg and y == Yg and goal is None:
        goal = s
        if part2 is not None: break
    seen.add((x, y))
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and (nx, ny) not in seen:
            if ((nx*nx + 3*nx + 2*nx*ny + ny + ny*ny + fav).bit_count() & 1) == 0:
                q.append((nx, ny, s+1))
sys.stdout.write(f"{goal} {part2}")