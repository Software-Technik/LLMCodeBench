import sys

def part1(input_path):
    with open(input_path) as fin:
        grid = fin.read().strip().split("\n")

    n, m = len(grid), len(grid[0])
    for i in range(n):
        if "^" in grid[i]:
            break

    dir = 0
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    seen = {(i, j)}
    while True:
        next_i, next_j = i + dd[dir][0], j + dd[dir][1]
        if not (0 <= next_i < n and 0 <= next_j < m):
            break
        if grid[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j
        seen.add((i, j))

    return len(seen)

def part2(input_path):
    with open(input_path) as fin:
        grid = fin.read().strip().split("\n")

    n, m = len(grid), len(grid[0])
    for i in range(n):
        if "^" in grid[i]:
            break

    dir = 0
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    og_seen = {(i, j)}

    def will_loop():
        seen = set()
        i, j = x, y
        while True:
            if (i, j, dir) in seen or not (0 <= i < n and 0 <= j < m):
                return False
            seen.add((i, j, dir))
            next_i, next_j = i + dd[dir][0], j + dd[dir][1]
            if grid[next_i][next_j] == "#":
                dir = (dir + 1) % 4
            else:
                i, j = next_i, next_j

        return True

    ans = sum(will_loop() for x, y in og_seen)

    return ans

input_path = sys.argv[1]
print(part1(input_path), part2(input_path))