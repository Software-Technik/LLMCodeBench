import sys

def part1(lines):

    def mix_prune(x, y, mod=16777216):
        return (x ^ y) % mod

    def next_val(x):
        x = mix_prune(x, x * 64)
        x = mix_prune(x, x // 32)
        x = mix_prune(x, x * 2048)
        return x

    def get_idx(seed, idx):
        x = seed
        for _ in range(idx):
            x = next_val(x)
        return x

    return sum(get_idx(x, 2000) for x in lines)

def part2(lines):

    def mix_prune(x, y, mod=16777216):
        return (x ^ y) % mod

    def next_val(x):
        x = mix_prune(x, x * 64)
        x = mix_prune(x, x // 32)
        x = mix_prune(x, x * 2048)
        return x

    def get_profit(seed):
        seq = [seed % 10]
        profit = {}
        x = seed
        for i in range(2000):
            x = next_val(x)
            seq.append(x % 10)

            if i >= 5:
                changes = tuple(seq[j] - seq[j - 1] for j in range(i - 2, i + 2))
                if changes not in profit:
                    profit[changes] = x % 10

        return profit

    profits = [get_profit(seed) for seed in lines]

    total_profit = {}

    for profit in profits:
        for seq, val in profit.items():
            if seq in total_profit:
                total_profit[seq] += val
            else:
                total_profit[seq] = val

    return max(total_profit.values(), default=0)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = list(map(int, fin.read().strip().split("\n")))
    print(part1(lines), part2(lines))