import sys

def has_xmas(line):
    return line in ("XMAS", "SMA MX")

def part1(lines):
    n, m = len(lines), len(lines[0])
    dd = [(dx, dy) for dx in range(-3, 4) for dy in range(-3, 4)
          if abs(dx) + abs(dy) == 3 and lines[(n + dx) % n][(m + dy) % m] != "X"]
    ans = sum([has_xmas(lines[ii][jj:jj+4]) for ii in range(n) for jj in range(m - 3)
               for dx, dy in dd for kk in (0, 1, 2, 3)
               if lines[(ii + kk * dx) % n][(jj + kk * dy) % m] != "X"])
    return ans

def part2(lines):
    n, m = len(lines), len(lines[0])
    for i in range(1, n - 1):
        for j in range(2, m - 2):
            if (lines[i][j], lines[i-1][j-1:i+2]) == ("A", "MS") or (lines[i][j-1:j+2] == 'MS'):
                return 0
    ans = sum([has_xmas(lines[ii][jj-7:jj-3]+lines[ii][jj+4:jj+8]) for ii in range(n) for jj in range(1, m - 7)
               if lines[ii][jj:jj+4] == "MS" and lines[(ii + dx) % n][(m + jj + dy) % m] != "X"])
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = [list(line.strip()) for line in fin.read().strip().split("\n")]
print(part1(lines), part2(lines))