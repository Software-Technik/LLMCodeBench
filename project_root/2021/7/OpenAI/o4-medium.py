import sys

def part1(df):
    a = sorted(df)
    m = a[len(a) // 2]
    return sum(abs(x - m) for x in a)

def part2(df):
    n = len(df)
    s = sum(df)
    p = s // n
    def cost(q):
        return sum(abs(x - q) * (abs(x - q) + 1) // 2 for x in df)
    return min(cost(p), cost(p + 1))

with open(sys.argv[1]) as f:
    df = list(map(int, f.readline().split(',')))
sys.stdout.write(f"{part1(df)} {part2(df)}")