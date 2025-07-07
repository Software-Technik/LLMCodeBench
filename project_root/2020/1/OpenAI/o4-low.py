import sys

def main():
    path = sys.argv[1]
    nums = []
    with open(path) as f:
        for line in f:
            nums.append(int(line))
    nums.sort()
    i, j = 0, len(nums) - 1
    res1 = 0
    while i < j:
        s = nums[i] + nums[j]
        if s == 2020:
            res1 = nums[i] * nums[j]
            break
        elif s < 2020:
            i += 1
        else:
            j -= 1
    res2 = 0
    n = len(nums)
    for k in range(n):
        target = 2020 - nums[k]
        i, j = k + 1, n - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                res2 = nums[k] * nums[i] * nums[j]
                print(res1, res2)
                return
            elif s < target:
                i += 1
            else:
                j -= 1
    print(res1, res2)

if __name__ == "__main__":
    main()