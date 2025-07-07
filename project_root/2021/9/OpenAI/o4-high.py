import sys
def main():
    with open(sys.argv[1]) as f:
        grid = [list(map(int, line.strip())) for line in f if line.strip()]
    h, w = len(grid), len(grid[0])
    lows = []
    risk = 0
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if (i == 0 or v < grid[i-1][j]) and (i == h-1 or v < grid[i+1][j]) and (j == 0 or v < grid[i][j-1]) and (j == w-1 or v < grid[i][j+1]):
                risk += v + 1
                lows.append((i, j))
    visited = [[False]*w for _ in range(h)]
    basins = []
    for i0, j0 in lows:
        if visited[i0][j0]: continue
        size = 0
        stack = [(i0, j0)]
        visited[i0][j0] = True
        while stack:
            i, j = stack.pop()
            size += 1
            if i > 0 and not visited[i-1][j] and grid[i-1][j] < 9:
                visited[i-1][j] = True; stack.append((i-1, j))
            if i < h-1 and not visited[i+1][j] and grid[i+1][j] < 9:
                visited[i+1][j] = True; stack.append((i+1, j))
            if j > 0 and not visited[i][j-1] and grid[i][j-1] < 9:
                visited[i][j-1] = True; stack.append((i, j-1))
            if j < w-1 and not visited[i][j+1] and grid[i][j+1] < 9:
                visited[i][j+1] = True; stack.append((i, j+1))
        basins.append(size)
    basins.sort(reverse=True)
    sys.stdout.write(f"{risk} {basins[0]*basins[1]*basins[2]}")
if __name__ == "__main__":
    main()