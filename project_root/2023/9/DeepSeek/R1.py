import sys

cache = {}

def get_pascal_triangle_row(row):
    if row in cache:
        return cache[row]
    res = [1] * (row+1)
    if row == 0:
        cache[row] = res
        return res
    for k in range(1, row+1):
        res[k] = res[k-1] * (row - k + 1) // k
    cache[row] = res
    return res

def part1(text: str) -> int:
    lines = text.splitlines()
    lines = [list(map(int, line.split())) for line in lines]
    if not lines:
        return 0
    n = len(lines[0])
    values = get_pascal_triangle_row(n)
    total = 0
    for line in lines:
        add = len(line) % 2 != 0
        for a, b in zip(line, values):
            r = a * b
            if add:
                total += r
            else:
                total -= r
            add = not add
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    lines = [list(map(int, line.split()[::-1])) for line in lines]
    if not lines:
        return 0
    n = len(lines[0])
    values = get_pascal_triangle_row(n)
    total = 0
    for line in lines:
        add = len(line) % 2 != 0
        for a, b in zip(line, values):
            r = a * b
            if add:
                total += r
            else:
                total -= r
            add = not add
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read().strip()
if not text:
    sys.stdout.write("0 0")
else:
    sys.stdout.write(f"{part1(text)} {part2(text)}")