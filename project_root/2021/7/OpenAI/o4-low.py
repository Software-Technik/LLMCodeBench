import sys

def part1(df):
    s = sorted(df)
    m = s[len(s)//2]
    return sum(abs(x-m) for x in df)

def part2(df):
    n = len(df)
    mean = sum(df)/n
    best = None
    for m in (int(mean), int(mean)+1):
        total = 0
        for x in df:
            d = abs(x-m)
            total += d*(d+1)//2
        if best is None or total < best:
            best = total
    return best

with open(sys.argv[1]) as f:
    df = list(map(int, f.readline().split(',')))

print(part1(df), part2(df))