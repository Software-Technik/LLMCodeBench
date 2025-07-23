import sys
from collections import Counter, defaultdict

def part1(data):
    df = [int(x) for x in data.split(",")]
    for day in range(80):
        new = sum(x == 0 for x in df)
        df = [x - 1 if x > 0 else 6 for x in df] + [8] * new
    return len(df)

def part2(data):
    df = Counter(int(x) for x in data.split(","))
    for i in range(9):
        if i not in df:
            df[i] = 0

    for day in range(256):
        df[-1], df[7] = df[8], df[8] + df[7]
        for i in range(6, -1, -1):
            df[i-1] = df[i]

    return sum(df.values())

input_file = sys.argv[1]
with open(input_file) as f:
    data = next(f).strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")