import sys

def s2d(s):
    mapping = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    return sum(mapping[c] * (5 ** i) for i, c in enumerate(s[::-1]))

def d2s(d):
    if d == 0:
        return "0"
    mapping = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    digits = []
    while d:
        d, r = divmod(d, 5)
        if r > 2:
            r -= 5
            d += 1
        digits.append(mapping[r])
    return "".join(digits[::-1])

def part1(data):
    total = sum(s2d(line) for line in data)
    return d2s(total)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n")