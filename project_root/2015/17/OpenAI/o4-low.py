import sys

def main():
    data = [int(line) for line in open(sys.argv[1])]
    eggnog = 25 if len(data) == 5 else 150
    dp = {0: {0: 1}}
    for c in data:
        for s, ks in list(dp.items()):
            ns = s + c
            if ns > eggnog: continue
            if ns not in dp: dp[ns] = {}
            for k, cnt in ks.items():
                dp[ns][k+1] = dp[ns].get(k+1, 0) + cnt
    ways = dp.get(eggnog, {})
    p1 = sum(ways.values())
    min_k = min(ways) if ways else 0
    p2 = ways.get(min_k, 0)
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()