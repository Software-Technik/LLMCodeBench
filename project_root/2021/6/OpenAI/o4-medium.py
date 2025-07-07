import sys

with open(sys.argv[1]) as f:
    data = f.read().strip().split(',')

counts = [0]*9
for x in data:
    counts[int(x)] += 1

res1 = None
for day in range(1, 257):
    new = counts[0]
    for i in range(8):
        counts[i] = counts[i+1]
    counts[6] += new
    counts[8] = new
    if day == 80:
        res1 = sum(counts)

res2 = sum(counts)
print(res1, res2)