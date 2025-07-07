from collections import Counter
import sys

def part1(data):
    a, b = zip(*((int(n) for n in line.split("   ")) for line in data.strip().split("\n")))
    a, b = sorted(a), sorted(b)
    return sum(abs(x - y) for x, y in zip(a, b))

def part2(data):
    a, b = zip(*((int(n) for n in line.split("   ")) for line in data.strip().split("\n")))
    counts = Counter(b)
    return sum(x * counts[x] for x in a)

input_path = sys.argv[1]
with open(input_path) as fin:
    data = fin.read()
    print(part1(data), part2(data))