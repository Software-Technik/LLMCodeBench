import sys

def part1(data):
    r = 0
    for line in data:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
            r += 1
    return r

def part2(data):
    r = 0
    for line in data:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if a1 <= b2 and a2 >= b1:
            r += 1
    return r

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")