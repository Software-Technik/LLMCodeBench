import sys
from collections import deque

path = sys.argv[1]
graph = {}
rev = {}

with open(path) as f:
    for line in f:
        line = line.strip().rstrip('.')
        if not line: continue
        parent, rest = line.split(' bags contain ')
        if rest == 'no other bags':
            graph[parent] = []
            continue
        lst = []
        for part in rest.split(', '):
            tokens = part.split()
            n = int(tokens[0])
            child = tokens[1] + ' ' + tokens[2]
            lst.append((child, n))
            rev.setdefault(child, []).append(parent)
        graph[parent] = lst

visited = set()
dq = deque(['shiny gold'])
while dq:
    curr = dq.popleft()
    for p in rev.get(curr, ()):
        if p not in visited:
            visited.add(p)
            dq.append(p)
part1 = len(visited)

memo = {}
def dfs(bag):
    if bag in memo:
        return memo[bag]
    total = 0
    for child, n in graph.get(bag, ()):
        total += n + n * dfs(child)
    memo[bag] = total
    return total

part2 = dfs('shiny gold')
print(part1, part2)