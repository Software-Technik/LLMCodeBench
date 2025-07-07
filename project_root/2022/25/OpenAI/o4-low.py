import sys

mapping = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
inv_mapping = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}

def s2d(s):
    v = 0
    for c in s:
        v = v * 5 + (mapping[c] + 2)
    return v - sum(2 * 5**i for i in range(len(s)))

def d2s(n):
    if n == 0:
        return "0"
    res = []
    while n:
        n, r = divmod(n, 5)
        if r > 2:
            r -= 5
            n += 1
        res.append(inv_mapping[r])
    return "".join(reversed(res))

def part1(data):
    total = 0
    for s in data:
        total += s2d(s)
    return d2s(total)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]
print(part1(data))