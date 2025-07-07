import sys

def part1(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        target = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        dp = {nums[0]}
        for n in nums[1:]:
            new_dp = set()
            for v in dp:
                new_dp.add(v + n)
                new_dp.add(v * n)
            dp = new_dp
        if target in dp:
            ans += target
    return ans

def part2(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        target = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        dp = {nums[0]}
        for n in nums[1:]:
            ndigits = 10 ** len(str(n))
            new_dp = set()
            for v in dp:
                new_dp.add(v + n)
                new_dp.add(v * n)
                new_dp.add(v * ndigits + n)
            dp = new_dp
        if target in dp:
            ans += target
    return ans

if __name__ == "__main__":
    lines = open(sys.argv[1]).read().splitlines()
    print(part1(lines), part2(lines))