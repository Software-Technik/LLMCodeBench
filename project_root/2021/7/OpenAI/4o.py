import sys

def part1(data):
    df = list(map(int, data.split(',')))
    median = sorted(df)[len(df) // 2]
    return sum(abs(x - median) for x in df)

def part2(data):
    df = list(map(int, data.split(',')))
    mean_floor = sum(df) // len(df)
    mean_ceil = mean_floor + 1
    fuel_cost = lambda m: sum((abs(x - m) * (abs(x - m) + 1)) // 2 for x in df)
    return min(fuel_cost(mean_floor), fuel_cost(mean_ceil))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = next(f).strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")