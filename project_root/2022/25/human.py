import math
import sys

def part1(data):
    return d2s(sum(s2d(i) for i in data))

def part2(data):
    return "Merry Christmas!"

def s2d(s):
    # return sum(("=-012".index(c) - 2) * 5**i for i, c in enumerate(s[::-1]))
    mapping = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    return sum(mapping[c] * 5**i for i, c in enumerate(s[::-1]))

def d2s(d):
    mapping = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    exp = math.ceil(math.log(d, 5))
    d += sum(2 * 5**i for i in range(exp))
    return "".join(mapping[d // (5**i) % 5 - 2] for i in range(exp - 1, -1, -1))

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")