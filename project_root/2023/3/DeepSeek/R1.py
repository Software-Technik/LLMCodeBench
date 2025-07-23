import sys

grid = []
is_symbol = []
number_info = []

def part1():
    global grid, is_symbol, number_info
    if not grid:
        return 0
    n = len(grid)
    m = len(grid[0])
    total = 0
    for i in range(n):
        j = 0
        while j < m:
            if grid[i][j].isdigit():
                i0, start, end = number_info[i][j]
                found = False
                for r in range(max(0, i0-1), min(n, i0+2)):
                    for c in range(max(0, start-1), min(m, end+2)):
                        if is_symbol[r][c]:
                            found = True
                            break
                    if found:
                        break
                if found:
                    num = int(grid[i0][start:end+1])
                    total += num
                j = end + 1
            else:
                j += 1
    return total

def part2():
    global grid, is_symbol, number_info
    if not grid:
        return 0
    n = len(grid)
    m = len(grid[0])
    total = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                adjacent_nums = set()
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        ni = i + dx
                        nj = j + dy
                        if 0 <= ni < n and 0 <= nj < m:
                            info = number_info[ni][nj]
                            if info is not None:
                                adjacent_nums.add(info)
                if len(adjacent_nums) == 2:
                    nums = []
                    for (i0, start, end) in adjacent_nums:
                        nums.append(int(grid[i0][start:end+1]))
                    total += nums[0] * nums[1]
    return total

with open(sys.argv[1]) as f:
    text = f.read().strip()
grid = text.splitlines()
n = len(grid)
if n == 0:
    is_symbol = []
    number_info = []
    sys.stdout.write(f"{0} {0}")
    sys.exit(0)
m = len(grid[0])

is_symbol = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        c = grid[i][j]
        if c != '.' and not c.isdigit():
            is_symbol[i][j] = True

number_info = [[None] * m for _ in range(n)]
for i in range(n):
    j = 0
    while j < m:
        if grid[i][j].isdigit():
            start = j
            while j < m and grid[i][j].isdigit():
                j += 1
            end = j - 1
            for col in range(start, end + 1):
                number_info[i][col] = (i, start, end)
        else:
            j += 1

sys.stdout.write(f"{part1()} {part2()}")