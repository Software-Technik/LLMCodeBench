import sys

input_path = sys.argv[1]
with open(input_path) as f:
    nums = [int(x) for x in f]

result1 = None
seen = set()
for a in nums:
    b = 2020 - a
    if b in seen:
        result1 = a * b
        break
    seen.add(a)

result2 = None
for i, a in enumerate(nums):
    seen = set()
    target = 2020 - a
    for b in nums[i+1:]:
        c = target - b
        if c in seen:
            result2 = a * b * c
            break
        seen.add(b)
    if result2:
        break

print(result1, result2)