import sys

def part1(lines):
    def is_safe(nums):
        inc = nums[1] > nums[0]
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if inc:
                if not 1 <= diff <= 3:
                    return False
            else:
                if not -3 <= diff <= -1:
                    return False
        return True

    return sum(is_safe([int(i) for i in line.split()]) for line in lines)

def part2(lines):
    def is_safe(nums):
        inc = nums[1] > nums[0]
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if inc:
                if not 1 <= diff <= 3:
                    return False
            else:
                if not -3 <= diff <= -1:
                    return False
        return True
    
    def is_really_safe(nums):
        if is_safe(nums):
            return True
        return any(is_safe(nums[:i] + nums[i + 1:]) for i in range(len(nums)))

    return sum(is_really_safe([int(i) for i in line.split()]) for line in lines)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))