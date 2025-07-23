import sys

def part1(data):
    df = list(map(int, data.split(',')))
    median = sorted(df)[len(df)//2]
    return sum(abs(x - median) for x in df)

def part2(data):
    df = list(map(int, data.split(',')))
    total = sum(df)
    n = len(df)
    candidate1 = total // n
    candidate2 = candidate1 + 1
    fuel1 = 0
    fuel2 = 0
    for x in df:
        d1 = abs(x - candidate1)
        fuel1 += d1 * (d1 + 1) // 2
        d2 = abs(x - candidate2)
        fuel2 += d2 * (d2 + 1) // 2
    return min(fuel1, fuel2)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = next(f).strip()
    
sys.stdout.write(f"{part1(data)} {part2(data)}")