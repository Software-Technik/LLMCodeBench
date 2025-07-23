from collections import defaultdict
import sys


def part1(data):
    a = []
    b = []
    for line in data.strip().split("\n"):
        num1, num2 = map(int, line.split())
        a.append(num1)
        b.append(num2)
    a.sort()
    b.sort()
    return sum(abs(x - y) for x, y in zip(a, b))


def part2(data):
    a = []
    b_counts = defaultdict(int)
    for line in data.strip().split("\n"):
        num1, num2 = map(int, line.split())
        a.append(num1)
        b_counts[num2] += 1
    return sum(x * b_counts[x] for x in a)


input_path = sys.argv[1]
with open(input_path) as fin:
    data = fin.read()
    print(part1(data), part2(data))