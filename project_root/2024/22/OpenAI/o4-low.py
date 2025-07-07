import sys

mask = (1 << 24) - 1

def next_x(x):
    x = (x ^ (x * 64)) & mask
    x = (x ^ (x >> 5)) & mask
    x = (x ^ (x * 2048)) & mask
    return x

def part1(lines):
    total = 0
    for seed in lines:
        x = seed
        for _ in range(2000):
            x = next_x(x)
        total += x
    return total

def part2(lines):
    total_profit = {}
    for seed in lines:
        seq = [seed % 10]
        x = seed
        for i in range(2000):
            x = next_x(x)
            seq.append(x % 10)
            if i >= 5:
                changes = (seq[i-2] - seq[i-3], seq[i-1] - seq[i-2], seq[i] - seq[i-1], seq[i+1] - seq[i])
                total_profit[changes] = total_profit.get(changes, 0) + (x % 10)
    return max(total_profit.values() or [0])

with open(sys.argv[1]) as fin:
    lines = list(map(int, fin.read().split()))
    print(part1(lines), part2(lines))