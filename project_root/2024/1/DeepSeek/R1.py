import sys
from collections import defaultdict

def part1(a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    ans = 0
    for i in range(len(a_sorted)):
        ans += abs(a_sorted[i] - b_sorted[i])
    return ans

def part2(a, b):
    counts = defaultdict(int)
    for x in b:
        counts[x] += 1
    ans = 0
    for x in a:
        ans += x * counts[x]
    return ans

if __name__ == "__main__":
    input_path = sys.argv[1]
    a = []
    b = []
    with open(input_path) as fin:
        for line in fin:
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split()
            if len(parts) < 2:
                continue
            a.append(int(parts[0]))
            b.append(int(parts[1]))
    print(part1(a, b), part2(a, b))