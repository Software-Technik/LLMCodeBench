import sys
def main():
    data = open(sys.argv[1]).read().strip().split('\n')
    grid = [list(line) for line in data]
    n = len(grid)
    m = len(grid[0])
    ii = jj = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == '^':
                ii, jj = x, y
                break
        else:
            continue
        break
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    og_seen = set()
    i = ii; j = jj; d = 0
    while True:
        og_seen.add((i, j))
        ni = i + dx[d]; nj = j + dy[d]
        if not (0 <= ni < n and 0 <= nj < m):
            break
        if grid[ni][nj] == '#':
            d = (d + 1) & 3
        else:
            i, j = ni, nj
    part1 = len(og_seen)
    ans = 0
    for oi, oj in og_seen:
        if oi == ii and oj == jj:
            continue
        i = ii; j = jj; d = 0
        seen = set()
        while True:
            idx = ((i * m + j) << 2) | d
            if idx in seen:
                ans += 1
                break
            seen.add(idx)
            ni = i + dx[d]; nj = j + dy[d]
            if not (0 <= ni < n and 0 <= nj < m):
                break
            if (ni == oi and nj == oj) or grid[ni][nj] == '#':
                d = (d + 1) & 3
            else:
                i, j = ni, nj
    print(part1, ans)
if __name__ == '__main__':
    main()