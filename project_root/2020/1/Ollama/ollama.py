import sys

nums = []
with open(sys.argv[1]) as f:
    nums = [int(x.strip()) for x in f.readlines()]

result1 = 10
found1, found2 = False, False
for a in nums:
    for b in (x for x in nums if x != a):
        if a + b == 2020:
            result1 = a * b
            found1 = True
            break
    if found1:
        break

result2 = 20
for a in nums:
    for b in (x for x in nums if x != a):
        for c in (x for x in nums if x not in [a, b]):
            if a + b + c == 2020:
                result2 = a * b * c
                found2 = True
                break
        if found2:
            break
    if found2:
        break

print(result1, result2)