import sys

with open(sys.argv[1]) as f:
    adapters = sorted(map(int, f.read().split()))

ones = threes = 0
prev = 0
for x in adapters:
    d = x - prev
    if d == 1:
        ones += 1
    elif d == 3:
        threes += 1
    prev = x
threes += 1

dp = {0: 1}
for x in adapters:
    dp[x] = dp.get(x-1, 0) + dp.get(x-2, 0) + dp.get(x-3, 0)

print(ones * threes, dp[adapters[-1]])