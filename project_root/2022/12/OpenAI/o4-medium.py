import sys
from collections import deque
f = open(sys.argv[1])
lines = [l.rstrip('\n') for l in f]
f.close()
h, w = len(lines), len(lines[0])
grid = [[0]*w for _ in range(h)]
for r in range(h):
    for c, ch in enumerate(lines[r]):
        if ch == 'S':
            sr, sc = r, c
            grid[r][c] = 97
        elif ch == 'E':
            er, ec = r, c
            grid[r][c] = 122
        else:
            grid[r][c] = ord(ch)
dirs = ((1,0),(-1,0),(0,1),(0,-1))
dist = [[-1]*w for _ in range(h)]
dq = deque()
dist[sr][sc] = 0
dq.append((sr, sc))
while dq:
    r, c = dq.popleft()
    if r == er and c == ec: break
    d = dist[r][c]
    h0 = grid[r][c]
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < h and 0 <= nc < w and dist[nr][nc] == -1 and grid[nr][nc] - h0 <= 1:
            dist[nr][nc] = d+1
            dq.append((nr, nc))
res1 = dist[er][ec]
dist2 = [[-1]*w for _ in range(h)]
dq = deque()
dist2[er][ec] = 0
dq.append((er, ec))
res2 = None
a_val = 97
while dq:
    r, c = dq.popleft()
    d = dist2[r][c]
    if grid[r][c] == a_val:
        res2 = d
        break
    h0 = grid[r][c]
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < h and 0 <= nc < w and dist2[nr][nc] == -1 and h0 - grid[nr][nc] <= 1:
            dist2[nr][nc] = d+1
            dq.append((nr, nc))
sys.stdout.write(f"{res1}\n{res2}\n")