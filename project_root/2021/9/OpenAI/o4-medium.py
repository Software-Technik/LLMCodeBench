import sys

data = [line.strip() for line in open(sys.argv[1]) if line.strip()]
n, m = len(data), len(data[0])
grid = [list(map(int, line)) for line in data]

risk = 0
low_points = []
for i in range(n):
    for j in range(m):
        h = grid[i][j]
        if (i == 0 or h < grid[i-1][j]) and (i == n-1 or h < grid[i+1][j]) and (j == 0 or h < grid[i][j-1]) and (j == m-1 or h < grid[i][j+1]):
            risk += h + 1
            low_points.append((i, j))

visited = [[False]*m for _ in range(n)]
basins = []
for i0, j0 in low_points:
    if visited[i0][j0]: continue
    size = 0
    stack = [(i0, j0)]
    visited[i0][j0] = True
    while stack:
        i, j = stack.pop()
        size += 1
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and grid[ni][nj] < 9:
                visited[ni][nj] = True
                stack.append((ni, nj))
    basins.append(size)

basins.sort(reverse=True)
result2 = basins[0] * basins[1] * basins[2]
sys.stdout.write(f"{risk} {result2}")