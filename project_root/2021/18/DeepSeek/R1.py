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
        if depth > 4 and s == "[" and isinstance(n[i+1], int) and isinstance(n[i+2], int) and n[i+3] == "]":
            for j in range(i-1, -1, -1):
                if isinstance(n[j], int):
                    n[j] += n[i+1]
                    break
            for j in range(i+4, len(n)):
                if isinstance(n[j], int):
                    n[j] += n[i+2]
                    break
            return n[:i] + [0] + n[i+4:], True
    return n, False

def split(n):
    for i, s in enumerate(n):
        if isinstance(s, int) and s >= 10:
            return n[:i] + ["[", s//2, s - s//2, "]"] + n[i+1:], True
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
    for token in n:
        if token == '[' or token == ',':
            continue
        elif token == ']':
            right = stack.pop()
            left = stack.pop()
            stack.append(3 * left + 2 * right)
        else:
            stack.append(token)
    return stack[0]

def part1(parsed_data):
    current = parsed_data[0]
    for i in range(1, len(parsed_data)):
        current = reduce(add(current, parsed_data[i]))
    return magnitude(current)

def part2(parsed_data):
    max_magnitude = 0
    n = len(parsed_data)
    for i in range(n):
        for j in range(n):
            if i != j:
                s = add(parsed_data[i], parsed_data[j])
                s = reduce(s)
                mag = magnitude(s)
                if mag > max_magnitude:
                    max_magnitude = mag
    return max_magnitude

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

parsed_data = [parse_snailfish(line) for line in data]
sys.stdout.write(f"{part1(parsed_data)} {part2(parsed_data)}")