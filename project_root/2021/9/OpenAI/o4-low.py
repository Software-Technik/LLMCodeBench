import sys
sys.setrecursionlimit(1000000)
def main():
    path = sys.argv[1]
    with open(path) as f:
        grid = [list(map(int, line.strip())) for line in f if line.strip()]
    n, m = len(grid), len(grid[0])
    part1 = 0
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            if (i==0 or v<grid[i-1][j]) and (i==n-1 or v<grid[i+1][j]) and (j==0 or v<grid[i][j-1]) and (j==m-1 or v<grid[i][j+1]):
                part1 += v+1
    visited = [[False]*m for _ in range(n)]
    sizes = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j]<9:
                size = 0
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    size += 1
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]<9:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                sizes.append(size)
    sizes.sort()
    part2 = sizes[-1]*sizes[-2]*sizes[-3]
    sys.stdout.write(f"{part1} {part2}")

if __name__=="__main__":
    main()