import sys
with open(sys.argv[1]) as f:
    intervals = [tuple(map(int, line.split('-'))) for line in f]
intervals.sort()
lowest = first = total = 0
for lo, hi in intervals:
    if lo > lowest:
        total += lo - lowest
        if not first:
            first = lowest
    if hi + 1 > lowest:
        lowest = hi + 1
sys.stdout.write(f"{first} {total}")