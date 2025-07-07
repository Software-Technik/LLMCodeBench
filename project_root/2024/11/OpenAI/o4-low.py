import sys
from collections import defaultdict

def run(raw_nums, steps):
    nums = defaultdict(int)
    for x in raw_nums:
        nums[x] += 1
    for _ in range(steps):
        new = defaultdict(int)
        for x, c in nums.items():
            if x == 0:
                new[1] += c
            else:
                s = str(x)
                l = len(s)
                if l & 1:
                    new[x * 2024] += c
                else:
                    h = int(s[:l//2])
                    k = int(s[l//2:])
                    new[h] += c
                    new[k] += c
        nums = new
    return sum(nums.values())

if __name__ == "__main__":
    raw = list(map(int, open(sys.argv[1]).read().split()))
    print(run(raw, 25), run(raw, 75))