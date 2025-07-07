import sys

def is_safe(nums):
    d = nums[1] - nums[0]
    if d == 0 or abs(d) > 3:
        return False
    sign = 1 if d > 0 else -1
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff * sign <= 0 or abs(diff) > 3:
            return False
    return True

def is_really_safe(nums):
    if is_safe(nums):
        return True
    n = len(nums)
    for i in range(n):
        if is_safe(nums[:i] + nums[i+1:]):
            return True
    return False

def main():
    lines = open(sys.argv[1]).read().strip().splitlines()
    nums_list = [list(map(int, line.split())) for line in lines]
    p1 = sum(is_safe(nums) for nums in nums_list)
    p2 = sum(is_really_safe(nums) for nums in nums_list)
    print(p1, p2)

if __name__ == "__main__":
    main()