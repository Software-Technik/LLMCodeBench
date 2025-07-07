import sys

def part1(input_path):
    with open(input_path) as fin:
        grid = fin.read().strip().split("\n")

    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                start_i, start_j = i, j
                break
        else:
            continue
        break

    dir = 0
    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    seen = set()
    while (start_i, start_j) not in seen:
        seen.add((start_i, start_j))

        next_i = start_i + dd[dir][0]
        next_j = start_j + dd[dir][1]

        if not (0 <= next_i < n and 0 <= next_j < m):
            break

        if grid[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            start_i, start_j = next_i, next_j

    return len(seen)

def part2(input_path):
    with open(input_path) as fin:
        grid = [list(line) for line in fin.read().strip().split("\n")]

    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                start_i, start_j = i, j
                break
        else:
            continue
        break

    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def traverse(i, j):
        dir = 0
        seen = set()
        while (i, j) not in seen:
            seen.add((i, j))
            next_i, next_j = i + dd[dir][0], j + dd[dir][1]

            if not (0 <= next_i < n and 0 <= next_j < m):
                return False

            if grid[next_i][next_j] == "#":
                dir = (dir + 1) % 4
            else:
                i, j = next_i, next_j

        return True

    original_seen = set()
    traverse(start_i, start_j)

    def will_loop(oi, oj):
        if grid[oi][oj] == "#":
            return False

        grid[oi][oj] = "#"
        result = traverse(start_i, start_j)
        grid[oi][oj] = "."
        return result

    ans = 0
    for oi, oj in original_seen:
        if (oi, oj) != (start_i, start_j):
            ans += will_loop(oi, oj)

    return ans

input_path = sys.argv[1]
print(part1(input_path), part2(input_path))