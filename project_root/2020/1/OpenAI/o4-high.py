import sys

def main():
    nums = list(map(int, open(sys.argv[1]).read().split()))
    s = set(nums)
    result1 = next(x*(2020-x) for x in nums if 2020-x in s)
    result2 = next(a*b*(2020-a-b) for i,a in enumerate(nums) for b in nums[i+1:] if 2020-a-b in s)
    print(result1, result2)

if __name__ == "__main__":
    main()