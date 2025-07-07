import sys
from collections import deque

def main():
    with open(sys.argv[1]) as f:
        lines = f.read().strip().splitlines()
    N = len(lines)
    coords = []
    world = {}
    for idx, line in enumerate(lines):
        a, b = line.split('~')
        x1, y1, z1 = map(int, a.split(','))
        x2, y2, z2 = map(int, b.split(','))
        cps = []
        if x1 != x2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                cps.append((x, y1, z1))
        elif y1 != y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                cps.append((x1, y, z1))
        else:
            for z in range(min(z1, z2), max(z1, z2) + 1):
                cps.append((x1, y1, z))
        coords.append(cps)
        for c in cps:
            world[c] = idx
    adj = [[] for _ in range(N)]
    for i, cps in enumerate(coords):
        for x, y, z in cps:
            j = world.get((x, y, z + 1))
            if j is not None:
                adj[i].append(j)
    part1 = sum(1 for lst in adj if not lst)
    total = 0
    for i in range(N):
        seen = [False] * N
        dq = deque()
        for j in adj[i]:
            seen[j] = True
            dq.append(j)
        cnt = 0
        while dq:
            u = dq.popleft()
            cnt += 1
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    dq.append(v)
        total += cnt
    sys.stdout.write(f"{part1} {total}")

if __name__ == "__main__":
    main()