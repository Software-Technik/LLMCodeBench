import sys
from collections import Counter

a = []
b = []
with open(sys.argv[1]) as f:
    for line in f:
        x, y = map(int, line.split())
        a.append(x)
        b.append(y)
a.sort()
b.sort()
p1 = sum(abs(x - y) for x, y in zip(a, b))
ac = Counter(a)
bc = Counter(b)
p2 = sum(x * ac[x] * bc[x] for x in ac)
print(p1, p2)