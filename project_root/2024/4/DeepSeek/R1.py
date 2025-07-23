import sys

def part1(lines):
    n = len(lines)
    m = len(lines[0])
    dd = [(-1,-1), (-1,0), (-1,1),
          (0,-1),           (0,1),
          (1,-1), (1,0), (1,1)]
    ans = 0
    for dx, dy in dd:
        i0 = max(0, -3 * dx)
        i1 = min(n-1, n-1 - 3*dx)
        j0 = max(0, -3 * dy)
        j1 = min(m-1, m-1 - 3*dy)
        if i0 > i1 or j0 > j1:
            continue
        for i in range(i0, i1+1):
            for j in range(j0, j1+1):
                if lines[i][j] == 'X' and lines[i+dx][j+dy] == 'M' and lines[i+2*dx][j+2*dy] == 'A' and lines[i+3*dx][j+3*dy] == 'S':
                    ans += 1
    return ans

def part2(lines):
    n = len(lines)
    m = len(lines[0])
    ans = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if lines[i][j] != 'A':
                continue
            tl = lines[i-1][j-1]
            br = lines[i+1][j+1]
            if not ((tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')):
                continue
            tr = lines[i-1][j+1]
            bl = lines[i+1][j-1]
            if (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M'):
                ans += 1
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))