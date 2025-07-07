import sys

def solve(lines):
    ans1 = ans2 = 0
    for line in lines:
        parts = line.split()
        target = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        curr = {nums[0]}
        for num in nums[1:]:
            next_set = set()
            for v in curr:
                next_set.add(v + num)
                next_set.add(v * num)
            curr = next_set
        if target in curr:
            ans1 += target
        curr = {nums[0]}
        mults = [10**len(str(num)) for num in nums[1:]]
        for num, m in zip(nums[1:], mults):
            next_set = set()
            for v in curr:
                next_set.add(v + num)
                next_set.add(v * num)
                next_set.add(v * m + num)
            curr = next_set
        if target in curr:
            ans2 += target
    print(ans1, ans2)

if __name__ == "__main__":
    lines = open(sys.argv[1]).read().strip().splitlines()
    solve(lines)