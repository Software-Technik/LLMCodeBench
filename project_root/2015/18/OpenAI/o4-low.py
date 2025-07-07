import sys

def simulate(data, steps, stuck):
    h, w = len(data), len(data[0])
    H, W = h+2, w+2
    grid = [[False]*W for _ in range(H)]
    for i, row in enumerate(data, 1):
        for j, c in enumerate(row, 1):
            grid[i][j] = (c == '#')
    corners = {(1,1), (1,w), (h,1), (h,w)}
    if stuck:
        for y,x in corners: grid[y][x] = True
    new = [[False]*W for _ in range(H)]
    for _ in range(steps):
        for i in range(1, h+1):
            for j in range(1, w+1):
                if stuck and (i,j) in corners:
                    new[i][j] = True
                else:
                    cnt = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                    if grid[i][j]:
                        new[i][j] = cnt == 2 or cnt == 3
                    else:
                        new[i][j] = cnt == 3
        grid, new = new, grid
    return sum(grid[i][j] for i in range(1, h+1) for j in range(1, w+1))

data = [line.strip() for line in open(sys.argv[1])]
if len(data) == 100:
    print(simulate(data,100,False))
    print(simulate(data,100,True))
else:
    print(simulate(data,4,False))
    print(simulate(data,5,True))