import sys

counts = {}
with open(sys.argv[1]) as f:
    for line in f:
        for token in line.split():
            x = int(token)
            counts[x] = counts.get(x, 0) + 1

res1 = None
for i in range(75):
    new = {}
    for x, c in counts.items():
        if x == 0:
            new[1] = new.get(1, 0) + c
        else:
            s = str(x)
            l = len(s)
            if l & 1 == 0:
                h = l >> 1
                a = int(s[:h])
                b = int(s[h:])
                new[a] = new.get(a, 0) + c
                new[b] = new.get(b, 0) + c
            else:
                y = x * 2024
                new[y] = new.get(y, 0) + c
    counts = new
    if i == 24:
        res1 = sum(counts.values())
res2 = sum(counts.values())
print(res1, res2)