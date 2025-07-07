import sys
def main():
    with open(sys.argv[1]) as f:
        lines = f.read().strip().split("\n")
    units = lines[0].split(", ")
    units_by_last = {}
    for u in units:
        units_by_last.setdefault(u[-1], []).append((u, len(u)))
    ans1 = ans2 = 0
    for s in lines[2:]:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            total = 0
            for u, l in units_by_last.get(s[i-1], ()):
                if l <= i and dp[i - l] and s[i - l:i] == u:
                    total += dp[i - l]
            dp[i] = total
        if dp[n]:
            ans1 += 1
            ans2 += dp[n]
    print(ans1, ans2)

if __name__ == "__main__":
    main()