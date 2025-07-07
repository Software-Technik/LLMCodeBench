import sys
import re

def parse_snailfish(n):
    return [int(x) if x.isdigit() else x for x in re.findall(r"\d+|[\[\]]", n)]

def add(a, b):
    return ["["] + a + b + ["]"]

def explode(n):
    depth = 0
    for i, s in enumerate(n):
        if s == "[":
            depth += 1
        elif s == "]":
            depth -= 1

        if depth > 4 and s == "[" and isinstance(n[i + 1], int) and isinstance(n[i + 2], int):
            if isinstance(n[i + 3], int) == False:
                continue
            for j in range(i - 1, -1, -1):
                if isinstance(n[j], int):
                    n[j] += n[i + 1]
                    break
            for j in range(i + 4, len(n)):
                if isinstance(n[j], int):
                    n[j] += n[i + 2]
                    break
            n[i:i + 4] = [0]
            return n, True
    return n, False

def split(n):
    for i, s in enumerate(n):
        if isinstance(s, int) and s >= 10:
            n[i:i + 1] = ["[", s // 2, s - s // 2, "]"]
            return n, True
    return n, False

def reduce(n):
    while True:
        n, to_reduce = explode(n)
        if to_reduce:
            continue
        n, to_reduce = split(n)
        if not to_reduce:
            break
    return n

def magnitude(n):
    while len(n) > 1:
        for i in range(len(n) - 3):
            if n[i] == "[" and isinstance(n[i + 1], int) and isinstance(n[i + 2], int):
                n[i:i + 4] = [3 * n[i + 1] + 2 * n[i + 2]]
                break
    return n[0]

def part1(data):
    m = parse_snailfish(data[0])
    for d in data[1:]:
        n = parse_snailfish(d)
        m = reduce(add(m, n))
    return magnitude(m)

def part2(data):
    max_magnitude = 0
    for i, d1 in enumerate(data):
        for j, d2 in enumerate(data):
            if i != j:
                mag = magnitude(reduce(add(parse_snailfish(d1), parse_snailfish(d2))))
                if mag > max_magnitude:
                    max_magnitude = mag
    return max_magnitude

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read().splitlines()
    print(f"{part1(data)} {part2(data)}")