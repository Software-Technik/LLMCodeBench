import sys
from collections import Counter, defaultdict

pow_cache = {0: 1}

def blink(nums):
    new = defaultdict(int)
    for x, c in nums.items():
        if x == 0:
            new[1] += c
        else:
            s = str(x)
            d = len(s)
            if d & 1 == 0:
                h = d >> 1
                div = pow_cache.get(h)
                if div is None:
                    div = 10 ** h
                    pow_cache[h] = div
                new[x // div] += c
                new[x % div] += c
            else:
                new[x * 2024] += c
    return new

def main():
    data = list(map(int, open(sys.argv[1]).read().split()))
    nums = Counter(data)
    ans1 = None
    for i in range(75):
        nums = blink(nums)
        if i == 24:
            ans1 = sum(nums.values())
    ans2 = sum(nums.values())
    print(ans1, ans2)

if __name__ == "__main__":
    main()