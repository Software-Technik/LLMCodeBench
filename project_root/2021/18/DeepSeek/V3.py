import sys
import re

def parse_snailfish(n):
    v = re.split(r"(\[|\]|,)", n)
    v = [x for x in v if x not in ("", ",")]
    v = [int(x) if x.isdigit() else x for x in v]
    return v

def add(a, b):
    return ["["] + a + b + ["]"]

def explode(n):
    depth = 0
    for i, s in enumerate(n):
        if s == "[":
            depth += 1
        elif s == "]":
            depth -= 1

        if depth > 4 and s == "[" and isinstance(n[i + 1], int) and isinstance(n[i + 2], int) and n[i + 3] == "]":
            left = n[i + 1]
            right = n[i + 2]
            for j in range(i - 1, -1, -1):
                if isinstance(n[j], int):
                    n[j] += left
                    break
            for j in range(i + 4, len(n)):
                if isinstance(n[j], int):
                    n[j] += right
                    break
            return n[:i] + [0] + n[i + 4:], True
    return n, False

def split(n):
    for i, s in enumerate(n):
        if isinstance(s, int) and s >= 10:
            half = s // 2
            return n[:i] + ["[", half, s - half, "]"] + n[i + 1:], True
    return n, False

def reduce(n):
    while True:
        n, changed = explode(n)
        if changed:
            continue
        n, changed = split(n)
        if not changed:
            break
    return n

def magnitude(n):
    stack = []
    for s in n:
        if s == "[" or s == ",":
            continue
        if s == "]":
            right = stack.pop()
            left = stack.pop()
            stack.append(3 * left + 2 * right)
        else:
            stack.append(s)
    return stack[0]

def part1(data):
    m = parse_snailfish(data[0])
    for d in data[1:]:
        n = parse_snailfish(d)
        m = reduce(add(m, n))
    return magnitude(m)

def part2(data):
    max_magnitude = 0
    parsed = [parse_snailfish(d) for d in data]
    for i in range(len(parsed)):
        for j in range(len(parsed)):
            if i != j:
                mag = magnitude(reduce(add(parsed[i], parsed[j])))
                if mag > max_magnitude:
                    max_magnitude = mag
    return max_magnitude

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")