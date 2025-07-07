import sys
def part1(lines):
    units = lines[0].split(", ")
    group = {}
    for u in units:
        group.setdefault(u[-1], []).append(u)
    ans = 0
    for design in lines[2:]:
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for u in group.get(design[i-1], ()):
                L = len(u)
                if i >= L and dp[i-L] and design[i-L:i] == u:
                    dp[i] = True
                    break
        if dp[n]:
            ans += 1
    return ans

def part2(lines):
    units = lines[0].split(", ")
    group = {}
    for u in units:
        group.setdefault(u[-1], []).append(u)
    ans = 0
    for design in lines[2:]:
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            total = 0
            for u in group.get(design[i-1], ()):
                L = len(u)
                if i >= L and design[i-L:i] == u:
                    total += dp[i-L]
            dp[i] = total
        ans += dp[n]
    return ans

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()
print(part1(lines), part2(lines))