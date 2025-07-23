import sys

def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

def part1():
    return sum(is_triangle(row) for row in horizontal)

def part2():
    count = 0
    n = len(horizontal)
    for i in range(0, n, 3):
        for j in range(3):
            a = horizontal[i][j]
            b = horizontal[i+1][j]
            c = horizontal[i+2][j]
            if is_triangle([a, b, c]):
                count += 1
    return count

inout_strings = sys.argv[1]
horizontal = []
with open(inout_strings, 'r') as infile:
    for line in infile:
        parts = line.split()
        row = [int(x) for x in parts]
        horizontal.append(row)

sys.stdout.write(f"{part1()} {part2()}")