import sys
from functools import lru_cache

def parse(line):
    s, groups = line.strip().split()
    lookup = {"#": 2, "?": 1, ".": 0}
    return tuple(lookup[c] for c in s), tuple(map(int, groups.split(",")))

def solve_line(chars, blocks):
    n, m = len(chars), len(blocks)
    min_rem = [0] * (n + 1)
    max_rem = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        min_rem[i] = min_rem[i + 1] + (chars[i] == 2)
        max_rem[i] = max_rem[i + 1] + (chars[i] > 0)
    sum_b = [0] * (m + 1)
    for j in range(m - 1, -1, -1):
        sum_b[j] = sum_b[j + 1] + blocks[j]
    @lru_cache(None)
    def f(i, j):
        if j == m:
            return 1 if min_rem[i] == 0 else 0
        if i >= n or sum_b[j] > max_rem[i] or sum_b[j] < min_rem[i]:
            return 0
        c = chars[i]
        res = 0
        if c == 0:
            res = f(i + 1, j)
        elif c == 2:
            l = blocks[j]
            end = i + l
            if end <= n and max_rem[i] - max_rem[end] == l and (end == n or chars[end] != 2):
                res = 1 if j + 1 == m and end == n else f(end + 1, j + 1)
        else:
            res = f(i + 1, j)
            l = blocks[j]
            end = i + l
            if end <= n and max_rem[i] - max_rem[end] == l and (end == n or chars[end] != 2):
                res += 1 if (j + 1 == m and end == n) else f(end + 1, j + 1)
        return res
    return f(0, 0)

def part1(text):
    lines = text.strip().splitlines()
    total = 0
    for line in lines:
        chars, blocks = parse(line)
        total += solve_line(chars, blocks)
    return total

def part2(text):
    lines = text.strip().splitlines()
    total = 0
    for line in lines:
        chars, blocks = parse(line)
        nc = (chars + (1,)) * 5
        nc = nc[:-1]
        nb = blocks * 5
        total += solve_line(nc, nb)
    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")