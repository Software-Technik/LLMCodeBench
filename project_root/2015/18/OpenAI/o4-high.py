import sys

def simulate(data, steps, stuck):
    h = len(data)
    w = len(data[0])
    H = h + 2
    W = w + 2
    grid = [[0] * W for _ in range(H)]
    for i, row in enumerate(data, 1):
        gi = grid[i]
        for j, ch in enumerate(row, 1):
            gi[j] = ch == '#'
    if stuck:
        grid[1][1] = grid[1][w] = grid[h][1] = grid[h][w] = True
    new = [[0] * W for _ in range(H)]
    for _ in range(steps):
        for i in range(1, h+1):
            prev = grid[i-1]
            curr = grid[i]
            nxt  = grid[i+1]
            nrow = new[i]
            for j in range(1, w+1):
                if stuck and ((i == 1 or i == h) and (j == 1 or j == w)):
                    nrow[j] = True
                else:
                    s = prev[j-1] + prev[j] + prev[j+1] + curr[j-1] + curr[j+1] + nxt[j-1] + nxt[j] + nxt[j+1]
                    if curr[j]:
                        nrow[j] = (s == 2 or s == 3)
                    else:
                        nrow[j] = (s == 3)
        grid, new = new, grid
    tot = 0
    for i in range(1, h+1):
        tot += sum(grid[i][1:w+1])
    return tot

data = [line.strip() for line in open(sys.argv[1])]
h = len(data)
p1 = simulate(data, 100 if h == 100 else 4, False)
p2 = simulate(data, 100 if h == 100 else 5, True)
sys.stdout.write(f"{p1}\n{p2}\n")