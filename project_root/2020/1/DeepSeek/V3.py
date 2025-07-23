import sys

def solve():
    with open(sys.argv[1]) as f:
        nums = [int(x.strip()) for x in f.readlines()]
    
    nums_set = set(nums)
    result1 = 0
    for a in nums:
        b = 2020 - a
        if b in nums_set:
            result1 = a * b
            break
    
    result2 = 0
    for i, a in enumerate(nums):
        for j, b in enumerate(nums[i+1:], i+1):
            c = 2020 - a - b
            if c in nums_set:
                result2 = a * b * c
                print(result1, result2)
                return
    
    print(result1, result2)

solve()