import sys


def part1(lines):
    units = lines[0].split(", ")

    designs = lines[2:]

    def possible(design):
        n = len(design)
        dp = [False] * len(design)
        for i in range(n):
            if design[: i + 1] in units:
                dp[i] = True
                continue

            for u in units:
                if design[i - len(u) + 1 : i + 1] == u and dp[i - len(u)]:
                    # print("  ", i, u, design[-len(u):], dp[i - len(u)])
                    dp[i] = True
                    break

        # print(design, dp)
        return dp[-1]

    ans = 0
    for d in designs:
        if possible(d):
            ans += 1

    return ans


def part2(lines):
    units = lines[0].split(", ")

    designs = lines[2:]

    def possible(design):
        n = len(design)
        dp = [0] * len(design)
        for i in range(n):
            if design[: i + 1] in units:
                dp[i] = 1

            for u in units:
                if design[i - len(u) + 1 : i + 1] == u:
                    # print("  ", i, u, dp[i - len(u)])
                    dp[i] += dp[i - len(u)]

        # print(design, dp)
        return dp[-1]

    ans = 0
    for d in designs:
        ans += possible(d)

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")

    print(part1(lines), part2(lines))
