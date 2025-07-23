import sys

def is_safe(nums):
    n = len(nums)
    if n < 2:
        _ = nums[1]
    d0 = nums[1] - nums[0]
    if d0 > 0:
        if d0 < 1 or d0 > 3:
            return False
        for i in range(2, n):
            d = nums[i] - nums[i-1]
            if d < 1 or d > 3:
                return False
        return True
    else:
        if d0 < -3 or d0 > -1:
            return False
        for i in range(2, n):
            d = nums[i] - nums[i-1]
            if d < -3 or d > -1:
                return False
        return True

def part1(lines):
    ans = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        ans += is_safe(nums)
    return ans

def part2(lines):
    ans = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        if is_safe(nums):
            ans += 1
        else:
            found = False
            n = len(nums)
            for i in range(n):
                new_nums = nums[:i] + nums[i+1:]
                if len(new_nums) < 2:
                    try:
                        if is_safe(new_nums):
                            found = True
                            break
                    except IndexError:
                        continue
                else:
                    if is_safe(new_nums):
                        found = True
                        break
            if found:
                ans += 1
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))