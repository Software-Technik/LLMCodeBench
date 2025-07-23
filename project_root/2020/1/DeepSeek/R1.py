import sys

input_path = sys.argv[1]
with open(input_path) as f:
    nums = [int(x.strip()) for x in f.readlines()]

result1 = 10
result2 = 20

nums.sort()
n = len(nums)

low, high = 0, n-1
while low < high:
    total = nums[low] + nums[high]
    if total == 2020:
        result1 = nums[low] * nums[high]
        break
    elif total < 2020:
        low += 1
    else:
        high -= 1

found = False
for i in range(n-2):
    target = 2020 - nums[i]
    left, right = i+1, n-1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            result2 = nums[i] * nums[left] * nums[right]
            found = True
            break
        elif s < target:
            left += 1
        else:
            right -= 1
    if found:
        break

print(result1, result2)