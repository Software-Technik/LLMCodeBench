import sys, math

def part1(data):
    result = 0
    for i in data:
        a = list(map(int, i.split("x")))
        s = sum(a)
        t = sum(i * i for i in a)
        m = min(math.prod(p) for p in zip(a, reversed(a)))
        result += s ** 2 - t + m
    return result

def part2(data):
    result = 0
    for i in data:
        a = sorted(map(int, i.split("x")))
        result += 2 * (a[0] + a[1]) + math.prod(a)
    return result

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")