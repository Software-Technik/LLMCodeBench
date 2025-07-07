import sys
data = sorted(map(int, open(sys.argv[1])))
ones = threes = 0
prev = 0
for x in data:
    d = x - prev
    if d == 1: ones += 1
    elif d == 3: threes += 1
    prev = x
threes += 1
print(ones * threes, end=' ')
paths = {0:1}
for x in data:
    paths[x] = paths.get(x-1,0) + paths.get(x-2,0) + paths.get(x-3,0)
print(paths[data[-1]])