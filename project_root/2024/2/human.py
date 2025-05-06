import sys


def part1(lines):
    ans = 0

    def is_safe(nums):
        inc = nums[1] > nums[0]
        if inc:
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i - 1]
                if not 1 <= diff <= 3:
                    return False
            return True
        else:
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i - 1]
                if not -3 <= diff <= -1:
                    return False
            return True

    for line in lines:
        nums = [int(i) for i in line.split()]
        ans += is_safe(nums)

    return ans


def part2(lines):
    ans = 0

    def is_safe(nums):
        inc = nums[1] > nums[0]
        if inc:
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i - 1]
                if not 1 <= diff <= 3:
                    return False
            return True
        else:
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i - 1]
                if not -3 <= diff <= -1:
                    return False
            return True

    def is_really_safe(nums):
        if is_safe(nums):
            return True
        for i in range(len(nums)):
            if is_safe(nums[:i] + nums[i + 1 :]):
                return True
        return False

    for line in lines:
        nums = [int(i) for i in line.split()]
        ans += is_really_safe(nums)

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))
