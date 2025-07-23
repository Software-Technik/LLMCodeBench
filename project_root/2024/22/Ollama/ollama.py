import sys

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def next(x):
    x = prune(mix(x, x * 64))
    x = prune(mix(x, x // 32))
    x = prune(mix(x, x * 2048))
    return x

def get_idx(seed, idx):
    x = seed
    for _ in range(idx):
        x = next(x)
    return x

def part1(lines):
    res = [get_idx(x, 2000) for x in lines]
    return sum(res)

def get_profit(seed, profits):
    seq = [seed % 10]
    profit = {}
    x = seed
    for i in range(2000):
        x = next(x)
        seq.append(x % 10)
        if i >= 5:
            changes = [seq[j] - seq[j - 1] for j in range(i - 2, i + 2)]
            if tuple(changes) not in profit:
                profit[tuple(changes)] = x % 10
    profits.append(profit)

def get_total_profit(seq, profits):
    return sum(profit.get(seq, 0) for profit in profits)

def part2(lines):
    profits = []
    [get_profit(seed, profits) for seed in lines]
    seqs = set().union(*(profit.keys() for profit in profits))
    return max(get_total_profit(seq, profits) for seq in seqs)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = list(map(int, fin.read().strip().split("\n")))
    print(part1(lines), part2(lines))