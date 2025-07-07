import sys

def part1(lines):
    mask = 16777215
    total = 0
    for x in lines:
        for _ in range(2000):
            x = (x ^ (x << 6)) & mask
            x = (x ^ (x >> 5)) & mask
            x = (x ^ (x << 11)) & mask
        total += x
    return total

def part2(lines):
    mask = 16777215
    totals = {}
    for seed in lines:
        x = seed
        w = [seed % 10]
        seen = set()
        for i in range(2000):
            x = (x ^ (x << 6)) & mask
            x = (x ^ (x >> 5)) & mask
            x = (x ^ (x << 11)) & mask
            new = x % 10
            w.append(new)
            if len(w) > 6:
                w.pop(0)
            if i >= 5:
                d1 = w[2] - w[1]
                d2 = w[3] - w[2]
                d3 = w[4] - w[3]
                d4 = w[5] - w[4]
                key = (d1, d2, d3, d4)
                if key not in seen:
                    totals[key] = totals.get(key, 0) + new
                    seen.add(key)
    return max(totals.values()) if totals else 0

with open(sys.argv[1]) as f:
    lines = list(map(int, f.read().split()))
print(part1(lines), part2(lines))