import sys

with open(sys.argv[1]) as f:
    containers = [int(line) for line in f]
target = 25 if len(containers) == 5 else 150
containers.sort(reverse=True)
n = len(containers)
total = 0
counts = [0] * (n + 1)

def dfs(i, s, u):
    global total
    if s == target:
        total += 1
        counts[u] += 1
        return
    if s > target or i == n:
        return
    dfs(i + 1, s + containers[i], u + 1)
    dfs(i + 1, s, u)

dfs(0, 0, 0)
for c in counts:
    if c:
        print(total)
        print(c)
        break