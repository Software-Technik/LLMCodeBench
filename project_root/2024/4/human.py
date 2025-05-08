import sys


def part1(lines):

    n = len(lines)
    m = len(lines[0])

    # Generate all directions
    dd = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                dd.append((dx, dy))

    # dd = [(-1, -1), (-1, 0), (-1, 1),
    #       (0, -1),           (0, 1),
    #       (1, -1), (1, 0), (1, 1)]

    def has_xmas(i, j, d):
        dx, dy = d
        for k, x in enumerate("XMAS"):
            ii = i + k * dx
            jj = j + k * dy
            if not (0 <= ii < n and 0 <= jj < m):
                return False
            if lines[ii][jj] != x:
                return False
        return True

    # Count up every cell and every direction
    ans = 0
    for i in range(n):
        for j in range(m):
            for d in dd:
                ans += has_xmas(i, j, d)

    return ans


def part2(lines):

    n = len(lines)
    m = len(lines[0])

    dd = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                dd.append((dx, dy))

    def has_xmas(i, j):
        if not (1 <= i < n - 1 and 1 <= j < m - 1):
            return False
        if lines[i][j] != "A":
            return False

        # Check both diagonals
        diag_1 = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
        diag_2 = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"

        return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += has_xmas(i, j)

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))
