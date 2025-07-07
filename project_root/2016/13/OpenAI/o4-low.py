import sys
from collections import deque

GOAL = (31, 39)
START = (1, 1)
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def is_open(x, y, fav):
    v = x*x + 3*x + 2*x*y + y + y*y + fav
    return v.bit_count() & 1 == 0

def part1(fav):
    q = deque([(START[0], START[1], 0)])
    seen = {START}
    while q:
        x, y, d = q.popleft()
        if (x, y) == GOAL:
            return d
        for dx, dy in DELTAS:
            nx, ny = x+dx, y+dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in seen and is_open(nx, ny, fav):
                seen.add((nx, ny))
                q.append((nx, ny, d+1))

def part2(fav):
    q = deque([(START[0], START[1], 0)])
    seen = {START}
    while q:
        x, y, d = q.popleft()
        if d == 50:
            continue
        for dx, dy in DELTAS:
            nx, ny = x+dx, y+dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in seen and is_open(nx, ny, fav):
                seen.add((nx, ny))
                q.append((nx, ny, d+1))
    return len(seen)

if __name__ == "__main__":
    fav = int(open(sys.argv[1]).read().strip())
    print(part1(fav), part2(fav))