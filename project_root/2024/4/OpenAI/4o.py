import sys

def part1(lines):
    n, m = len(lines), len(lines[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def has_xmas(i, j, dx, dy):
        return all(
            0 <= i + k * dx < n and 0 <= j + k * dy < m and lines[i + k * dx][j + k * dy] == x
            for k, x in enumerate("XMAS")
        )

    return sum(has_xmas(i, j, dx, dy) for i in range(n) for j in range(m) for dx, dy in directions)

def part2(lines):
    n, m = len(lines), len(lines[0])

    def has_xmas(i, j):
        if lines[i][j] == "A" and 1 <= i < n - 1 and 1 <= j < m - 1:
            diag_1 = lines[i-1][j-1] + lines[i+1][j+1]
            diag_2 = lines[i-1][j+1] + lines[i+1][j-1]
            return diag_1 in {"MS", "SM"} and diag_2 in {"MS", "SM"}
        return False

    return sum(has_xmas(i, j) for i in range(n) for j in range(m))

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))