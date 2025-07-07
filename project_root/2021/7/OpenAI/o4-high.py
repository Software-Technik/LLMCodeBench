import sys

with open(sys.argv[1]) as f:
    df = list(map(int, f.readline().strip().split(',')))
n = len(df)
df.sort()
med = df[n//2]
part1 = sum(abs(x - med) for x in df)
s = sum(df)
q, r = divmod(s, n)
best = None
for p in (q, q+1) if r else (q,):
    s2 = 0
    for x in df:
        d = x - p
        if d < 0:
            d = -d
        s2 += d*(d+1)//2
    if best is None or s2 < best:
        best = s2
part2 = best
sys.stdout.write(f"{part1} {part2}")