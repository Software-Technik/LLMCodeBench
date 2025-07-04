import sys


nums = []

input_path = sys.argv[1]
with open(input_path) as f:
# with open(r"project_root\2020\advent-of-code-2020-master\1\input.txt") as f:
    nums = [int(x.strip()) for x in f.readlines()]

# print(nums)
result1 = 10
for a in nums:
    for b in nums:
        if a + b == 2020:
             (a, b, a * b)
             result1= a*b
            # 279 1741 485739
            # 1741 279 485739
result2 = 20
# part2
for a in nums:
    for b in nums:
        for c in nums:
            if a + b + c == 2020:
                (a, b, c, a * b * c)
                result2 = a * b * c
                # 1269 257 494 161109702
print(result1, result2)
