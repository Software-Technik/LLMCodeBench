import sys

def part1(input_path):
    with open(input_path) as fin:
        grid = fin.read().strip().split("\n")

    n = len(grid)
    m = len(grid[0])

    found = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                found = True
                break
        if found:
            break

    dir = 0
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    seen = set()
    while True:
        seen.add((i, j))

        next_i = i + dd[dir][0]
        next_j = j + dd[dir][1]

        if not (0 <= next_i < n and 0 <= next_j < m):
            break

        if grid[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j

    return len(seen)

def part2(input_path):
    with open(input_path) as fin:
        grid = [list(line) for line in fin.read().strip().split("\n")]

    n = len(grid)
    m = len(grid[0])

    found = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                found = True
                break
        if found:
            break

    ii, jj = i, j
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    og_seen = set()
    dir = 0
    i, j = ii, jj
    while True:
        og_seen.add((i, j))
        next_i = i + dd[dir][0]
        next_j = j + dd[dir][1]

        if not (0 <= next_i < n and 0 <= next_j < m):
            break

        if grid[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j

    def will_loop(oi, oj):
        if grid[oi][oj] == "#":
            return False

        grid[oi][oj] = "#"
        i, j = ii, jj
        dir = 0
        seen = set()
        while True:
            key = (i, j, dir)
            if key in seen:
                grid[oi][oj] = "."
                return True
            seen.add(key)

            next_i = i + dd[dir][0]
            next_j = j + dd[dir][1]

            if not (0 <= next_i < n and 0 <= next_j < m):
                grid[oi][oj] = "."
                return False

            if grid[next_i][next_j] == "#":
                dir = (dir + 1) % 4
            else:
                i, j = next_i, next_j

    ans = 0
    for oi, oj in og_seen:
        if oi == ii and oj == jj:
            continue
        if will_loop(oi, oj):
            ans += 1
    return ans

input_path = sys.argv[1]
print(part1(input_path), part2(input_path))