import sys

def part1(lines):
    units = set(lines[0].split(", "))
    max_len = max(len(u) for u in units) if units else 0
    designs = lines[2:]

    def possible(design):
        n = len(design)
        dp = [False] * n
        for i in range(n):
            for l in range(1, max_len + 1):
                if i - l + 1 < 0:
                    continue
                substring = design[i - l + 1 : i + 1]
                if substring in units and (i - l == -1 or dp[i - l]):
                    dp[i] = True
                    break
        return dp[-1] if n > 0 else False

    return sum(1 for d in designs if possible(d))

def part2(lines):
    units = set(lines[0].split(", "))
    max_len = max(len(u) for u in units) if units else 0
    designs = lines[2:]

    def possible(design):
        n = len(design)
        dp = [0] * n
        for i in range(n):
            for l in range(1, max_len + 1):
                if i - l + 1 < 0:
                    continue
                substring = design[i - l + 1 : i + 1]
                if substring in units:
                    dp[i] += dp[i - l] if i - l >= 0 else 1
        return dp[-1] if n > 0 else 0

    return sum(possible(d) for d in designs)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))