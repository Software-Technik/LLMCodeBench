import sys

def part1(data):
    df = list(map(int, data.split(',')))
    p_min, p_max = min(df), max(df)
    fuels = [sum(map(lambda x: abs(x - p), df)) for p in range(p_min, p_max + 1)]
    return min(fuels)   # 347011

def part2(data):
    df = list(map(int, data.split(',')))
    p_min, p_max = min(df), max(df)
    fuels = [sum(map(lambda x: abs(x - p) * (abs(x - p) + 1) // 2, df)) for p in range(p_min, p_max + 1)]
    return min(fuels)   # 98363777

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = next(f).strip()
    
sys.stdout.write(f"{part1(data)} {part2(data)}")