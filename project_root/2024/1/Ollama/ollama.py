from collections import defaultdict
import sys

def solve_part1_data(data):
    a = []
    b = []

    for line in data.strip().split("\n"):
        nums = [int(i) for i in line.split("   ")]
        a.append(nums[0])
        b.append(nums[1])

    a.sort()
    b.sort()

    ans = sum(abs(x - y) for x, y in zip(a, b))
    return ans

def solve_part2_data(data):
    a = []
    b = []

    for line in data.strip().split("\n"):
        nums = [int(i) for i in line.split("   ")]
        a.append(nums[0])
        b.append(nums[1])

    counts = defaultdict(int)
    for x in b:
        counts[x] += 1

    ans = sum(x * counts[x] for x in a)

    return ans

def main():
    input_path = sys.argv[1]
    with open(input_path) as fin:
        data = fin.read()
        print(solve_part1_data(data), solve_part2_data(data))

if __name__ == "__main__":
    main()