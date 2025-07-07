import sys

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")

ans1 = 0
ans2 = 0

for line in lines:
    parts = line.split()
    n = len(parts)
    nums = [int(x) for x in parts]
    prev = None
    inc = None
    lo = hi = 0
    safe = True
    for x in nums:
        if prev is None:
            prev = x
        else:
            d = x - prev
            if inc is None:
                if d > 0:
                    inc = True
                    lo, hi = 1, 3
                else:
                    inc = False
                    lo, hi = -3, -1
            if d < lo or d > hi:
                safe = False
                break
            prev = x
    if safe:
        ans1 += 1
        ans2 += 1
        continue
    for i in range(n):
        prev2 = None
        inc2 = None
        lo2 = hi2 = 0
        ok = True
        for j in range(n):
            if j == i:
                continue
            x = nums[j]
            if prev2 is None:
                prev2 = x
            else:
                d2 = x - prev2
                if inc2 is None:
                    if d2 > 0:
                        inc2 = True
                        lo2, hi2 = 1, 3
                    else:
                        inc2 = False
                        lo2, hi2 = -3, -1
                if d2 < lo2 or d2 > hi2:
                    ok = False
                    break
                prev2 = x
        if ok:
            ans2 += 1
            break

print(ans1, ans2)