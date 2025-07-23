import sys

def part1(data):
    df = list(map(int, data.split(',')))
    median = sorted(df)[len(df) // 2]
    return sum(abs(x - median) for x in df)

def part2(data):
    df = list(map(int, data.split(',')))
    mean = sum(df) // len(df)
    return min(sum(abs(x - p) * (abs(x - p) + 1) // 2 for x in df) for p in (mean, mean + 1))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = next(f).strip()
    
sys.stdout.write(f"{part1(data)} {part2(data)}")