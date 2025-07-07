import sys
grid = open(sys.argv[1]).read().strip().split("\n")
n = len(grid)
comp = [[-1]*n for _ in range(n)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
size = []
per1 = []
min_r = []
max_r = []
min_c = []
max_c = []
cid = 0
for i in range(n):
    for j in range(n):
        if comp[i][j] != -1: continue
        ch = grid[i][j]
        size.append(0)
        per1.append(0)
        min_r.append(i)
        max_r.append(i)
        min_c.append(j)
        max_c.append(j)
        stack = [(i,j)]
        while stack:
            x,y = stack.pop()
            if comp[x][y] != -1: continue
            comp[x][y] = cid
            size[cid] += 1
            if x < min_r[cid]: min_r[cid] = x
            if x > max_r[cid]: max_r[cid] = x
            if y < min_c[cid]: min_c[cid] = y
            if y > max_c[cid]: max_c[cid] = y
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == ch:
                    if comp[nx][ny] == -1:
                        stack.append((nx,ny))
                else:
                    per1[cid] += 1
        cid += 1
ans1 = 0
for k in range(cid):
    ans1 += per1[k] * size[k]
corner_scores = [0]*16
for m in (1,2,4,8,7,11,13,14):
    corner_scores[m] = 1
for m in (6,9):
    corner_scores[m] = 2
ans2 = 0
for k in range(cid):
    score = 0
    for x in range(min_r[k]-1, max_r[k]):
        x1 = x+1
        for y in range(min_c[k]-1, max_c[k]):
            y1 = y+1
            mask = 0
            if 0 <= x < n and 0 <= y < n and comp[x][y] == k:
                mask |= 1
            if 0 <= x < n and 0 <= y1 < n and comp[x][y1] == k:
                mask |= 2
            if 0 <= x1 < n and 0 <= y < n and comp[x1][y] == k:
                mask |= 4
            if 0 <= x1 < n and 0 <= y1 < n and comp[x1][y1] == k:
                mask |= 8
            score += corner_scores[mask]
    ans2 += score * size[k]
print(ans1, ans2)