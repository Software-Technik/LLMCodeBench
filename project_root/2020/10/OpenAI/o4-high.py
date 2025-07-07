import sys
with open(sys.argv[1]) as f:
    adapters = sorted(int(line) for line in f if line.strip())
adapters = [0] + adapters + [adapters[-1] + 3]
ones = threes = 0
for a, b in zip(adapters, adapters[1:]):
    d = b - a
    if d == 1: ones += 1
    elif d == 3: threes += 1
ways = {0: 1}
for a in adapters[1:]:
    ways[a] = ways.get(a-1, 0) + ways.get(a-2, 0) + ways.get(a-3, 0)
print(ones * threes, ways[adapters[-1]])