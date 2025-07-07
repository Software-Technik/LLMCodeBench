import sys
import math
from collections import deque

def parse(data):
    h, w = len(data), len(data[0])
    blizzards = []
    dirs = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
    for y, line in enumerate(data[1:-1], 1):
        for x, c in enumerate(line[1:-1], 1):
            if c in dirs:
                dy, dx = dirs[c]
                blizzards.append((y-1, x-1, dy, dx))
    return blizzards, h, w

def build_blocked(blizzards, h, w):
    H, W = h-2, w-2
    period = math.lcm(H, W)
    blocked = []
    for t in range(period):
        s = set()
        for y0, x0, dy, dx in blizzards:
            y = (y0 + dy*t) % H + 1
            x = (x0 + dx*t) % W + 1
            s.add((y, x))
        blocked.append(s)
    return blocked, period

def bfs(start, goal, start_time, blocked, period, h, w):
    moves = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
    seen = set()
    dq = deque()
    dq.append((start[0], start[1], start_time))
    while dq:
        y, x, t = dq.popleft()
        if (y, x) == goal:
            return t
        t1 = t + 1
        b = blocked[t1 % period]
        for dy, dx in moves:
            ny, nx = y+dy, x+dx
            if (ny, nx) == goal or (ny, nx) == start or (1 <= ny < h-1 and 1 <= nx < w-1):
                if (ny, nx) not in b:
                    key = (ny, nx, t1 % period)
                    if key not in seen:
                        seen.add(key)
                        dq.append((ny, nx, t1))
    return None

def main():
    fn = sys.argv[1]
    data = [line.strip() for line in open(fn)]
    blizzards, h, w = parse(data)
    blocked, period = build_blocked(blizzards, h, w)
    start = (0, 1)
    target = (h-1, w-2)
    t1 = bfs(start, target, 0, blocked, period, h, w)
    t2 = bfs(target, start, t1, blocked, period, h, w)
    t3 = bfs(start, target, t2, blocked, period, h, w)
    sys.stdout.write(f"{t1}\n{t3}\n")

if __name__ == "__main__":
    main()