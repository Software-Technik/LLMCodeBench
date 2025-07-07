import sys

def main():
    path = sys.argv[1]
    with open(path) as f:
        lines = [l.rstrip('\n') for l in f]
    n = len(lines)
    m = len(lines[0])
    grid = [list(line) for line in lines]
    start_i = start_j = 0
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == '^':
                start_i, start_j = i, j
                break
        else:
            continue
        break
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen_arr = [False] * (n * m)
    og_seen = []
    i, j, dir = start_i, start_j, 0
    while True:
        idx = i * m + j
        if not seen_arr[idx]:
            seen_arr[idx] = True
            og_seen.append(idx)
        di, dj = dirs[dir]
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
            break
        if grid[ni][nj] == '#':
            dir = (dir + 1) % 4
        else:
            i, j = ni, nj
    part1_res = len(og_seen)
    total_states = n * m * 4
    visited = [0] * total_states
    tick = 1
    ans = 0
    start_idx = start_i * m + start_j
    for idx in og_seen:
        if idx == start_idx:
            continue
        oi, oj = divmod(idx, m)
        grid[oi][oj] = '#'
        i, j, dir = start_i, start_j, 0
        tick += 1
        t = tick
        while True:
            sidx = (i * m + j) * 4 + dir
            if visited[sidx] == t:
                ans += 1
                break
            visited[sidx] = t
            di, dj = dirs[dir]
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                break
            if grid[ni][nj] == '#':
                dir = (dir + 1) % 4
            else:
                i, j = ni, nj
        grid[oi][oj] = '.'
    print(part1_res, ans)

if __name__ == "__main__":
    main()