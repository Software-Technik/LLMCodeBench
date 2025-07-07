import sys

data = open(sys.argv[1]).read().strip()
groups = data.split('\n\n')
result1 = sum(len(set(g.replace('\n',''))) for g in groups)
result2 = sum(len(set.intersection(*(set(p) for p in g.splitlines()))) for g in groups)
print(result1, result2)