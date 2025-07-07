import sys
with open(sys.argv[1]) as f:
    nums = list(map(int, f))
s = set(nums)
result1 = next(a*(2020-a) for a in nums if 2020-a in s)
result2 = next(a*b*(2020-a-b) for a in nums for b in nums if 2020-a-b in s)
print(result1, result2)