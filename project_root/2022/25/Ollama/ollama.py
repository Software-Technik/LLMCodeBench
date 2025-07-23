import sys

def part1(data):
    return sum(s2d(i) for i in data)

def s2d(s):
    mapping = {"=": -2, "-":-1, "0": 0, "1": 1, "2":4}
    total = 0
    for c in reversed(s):
        total = (total * 5 + mapping[c])
    return total

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n")