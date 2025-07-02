import sys


def part1(lines):

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

    res = [get_idx(x, 2000) for x in lines]
    # print(res)
    return sum(res)


def part2(lines):

    def mix(a, b):
        return a ^ b

    def prune(a):
        return a % 16777216

    def next(x):
        x = prune(mix(x, x * 64))
        x = prune(mix(x, x // 32))
        x = prune(mix(x, x * 2048))
        return x

    def get_profit(seed):
        seq = [seed % 10]
        profit = {}
        x = seed
        for i in range(2000):
            x = next(x)
            seq.append(x % 10)

            if i >= 5:
                changes = [seq[j] - seq[j - 1] for j in range(i - 2, i + 2)]
                if not tuple(changes) in profit:
                    profit[tuple(changes)] = x % 10

        return profit

    profits = [get_profit(seed) for seed in lines]

    def get_total_profit(seq):
        ans = 0
        for profit in profits:
            if seq in profit:
                ans += profit[seq]
        return ans

    seqs = set()
    for profit in profits:
        seqs = seqs.union(profit.keys())

    best = 0
    for seq in seqs:
        best = max(best, get_total_profit(seq))

    return best


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = list(map(int, fin.read().strip().split("\n")))
    print(part1(lines), part2(lines))
