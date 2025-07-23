import sys

def part1(df):
    p_min, p_max = min(df), max(df)
    fuels = [sum(abs(x - p) for x in df) for p in range(p_min, p_max + 1)]
    return min(fuels)

def part2(df):
    p_min, p_max = min(df), max(df)
    fuels = [sum((n := abs(x - p)) * (n + 1) // 2 for x in df) for p in range(p_min, p_max + 1)]
    return min(fuels)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, next(f).strip().split(',')))

sys.stdout.write(f"{part1(data)} {part2(data)}")