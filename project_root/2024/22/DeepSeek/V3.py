import sys

def part1(lines):
    def mix(a, b):
        return a ^ b

    def prune(a):
        return a & 0xFFFFFF  # Equivalent to mod 16777216

    def next_val(x):
        x = prune(mix(x, x << 6))  # x * 64 is x << 6
        x = prune(mix(x, x >> 5))  # x // 32 is x >> 5
        x = prune(mix(x, x << 11))  # x * 2048 is x << 11
        return x

    def get_idx(seed, idx):
        x = seed
        for _ in range(idx):
            x = next_val(x)
        return x

    return sum(get_idx(x, 2000) for x in lines)

def part2(lines):
    def mix(a, b):
        return a ^ b

    def prune(a):
        return a & 0xFFFFFF

    def next_val(x):
        x = prune(mix(x, x << 6))
        x = prune(mix(x, x >> 5))
        x = prune(mix(x, x << 11))
        return x

    def get_profit(seed):
        seq = [seed % 10]
        profit = {}
        x = seed
        for i in range(1, 2001):
            x = next_val(x)
            current_mod = x % 10
            seq.append(current_mod)
            if i >= 5:
                changes = tuple(seq[j] - seq[j - 1] for j in range(i - 2, i + 2))
                if changes not in profit:
                    profit[changes] = current_mod
        return profit

    profits = [get_profit(seed) for seed in lines]
    all_seqs = set().union(*profits)
    max_profit = 0
    for seq in all_seqs:
        total = sum(p.get(seq, 0) for p in profits)
        if total > max_profit:
            max_profit = total
    return max_profit

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = list(map(int, fin.read().strip().split("\n")))
    print(part1(lines), part2(lines))