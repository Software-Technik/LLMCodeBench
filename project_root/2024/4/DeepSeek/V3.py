import sys

def part1(lines):
    n = len(lines)
    m = len(lines[0]) if n > 0 else 0
    dd = [(-1, -1), (-1, 0), (-1, 1),
          (0, -1),           (0, 1),
          (1, -1), (1, 0), (1, 1)]
    
    ans = 0
    for i in range(n):
        for j in range(m):
            for dx, dy in dd:
                valid = True
                for k, x in enumerate("XMAS"):
                    ii, jj = i + k * dx, j + k * dy
                    if not (0 <= ii < n and 0 <= jj < m) or lines[ii][jj] != x:
                        valid = False
                        break
                ans += valid
    return ans

def part2(lines):
    n = len(lines)
    m = len(lines[0]) if n > 0 else 0
    ans = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if lines[i][j] == 'A':
                diag1 = lines[i-1][j-1] + lines[i+1][j+1]
                diag2 = lines[i-1][j+1] + lines[i+1][j-1]
                if (diag1 in {'MS', 'SM'}) and (diag2 in {'MS', 'SM'}):
                    ans += 1
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))