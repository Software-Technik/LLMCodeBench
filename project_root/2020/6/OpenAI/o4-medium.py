import sys
with open(sys.argv[1]) as f:
    data = f.read().strip()
groups = [g.split() for g in data.split('\n\n')]
result1 = sum(len(set().union(*g)) for g in groups)
result2 = sum(len(set(g[0]).intersection(*g[1:])) for g in groups)
print(result1, result2)