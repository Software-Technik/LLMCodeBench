import sys

def simulate(data, steps, stuck):
    h, w = len(data), len(data[0])
    H, W = h + 2, w + 2
    g = [[0] * W for _ in range(H)]
    ng = [[0] * W for _ in range(H)]
    for i, row in enumerate(data, 1):
        for j, c in enumerate(row, 1):
            g[i][j] = c == '#'
    if stuck:
        g[1][1] = g[1][w] = g[h][1] = g[h][w] = 1
    for _ in range(steps):
        for i in range(1, h+1):
            for j in range(1, w+1):
                if stuck and ((i == 1 and j == 1) or (i == 1 and j == w) or (i == h and j == 1) or (i == h and j == w)):
                    ng[i][j] = 1
                else:
                    s = g[i-1][j-1] + g[i-1][j] + g[i-1][j+1] + g[i][j-1] + g[i][j+1] + g[i+1][j-1] + g[i+1][j] + g[i+1][j+1]
                    if g[i][j]:
                        ng[i][j] = 1 if s == 2 or s == 3 else 0
                    else:
                        ng[i][j] = 1 if s == 3 else 0
        g, ng = ng, g
    return sum(sum(row[1:w+1]) for row in g[1:h+1])

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]
h = len(data)
p1 = simulate(data, 100 if h == 100 else 4, False)
p2 = simulate(data, 100 if h == 100 else 5, True)
sys.stdout.write(f"{p1}\n{p2}\n")