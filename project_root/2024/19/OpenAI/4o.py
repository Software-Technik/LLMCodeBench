import sys


def part1(lines):
    units = set(lines[0].split(", "))
    designs = lines[2:]

    def possible(design):
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for u in units:
                if i >= len(u) and dp[i - len(u)] and design[i - len(u):i] == u:
                    dp[i] = True
                    break
        return dp[n]

    return sum(possible(d) for d in designs)


def part2(lines):
    units = set(lines[0].split(", "))
    designs = lines[2:]

    def possible(design):
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for u in units:
                if i >= len(u) and design[i - len(u):i] == u:
                    dp[i] += dp[i - len(u)]
        return dp[n]

    return sum(possible(d) for d in designs)


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")

    print(part1(lines), part2(lines))