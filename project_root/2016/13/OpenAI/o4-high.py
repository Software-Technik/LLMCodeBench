import sys
from collections import deque

salt = int(open(sys.argv[1]).read().strip())
deltas = ((1,0),(-1,0),(0,1),(0,-1))
goalx, goaly = 31, 39
q = deque([(1,1,0)])
seen = {(1,1)}
part1 = None
part2 = 1
bitcount = int.bit_count
while q:
    x, y, steps = q.popleft()
    if steps > 50 and part1 is not None:
        break
    for dx, dy in deltas:
        nx = x + dx; ny = y + dy
        if nx < 0 or ny < 0 or (nx, ny) in seen:
            continue
        v = nx*nx + 3*nx + 2*nx*ny + ny + ny*ny + salt
        if bitcount(v) & 1:
            continue
        seen.add((nx, ny))
        ns = steps + 1
        if ns <= 50:
            part2 += 1
        if part1 is None and nx == goalx and ny == goaly:
            part1 = ns
        q.append((nx, ny, ns))
sys.stdout.write(f"{part1} {part2}")