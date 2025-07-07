import sys
sys.setrecursionlimit(10000)
def dfs(node, visited, used, graph):
    if node == "end":
        return 1
    total = 0
    for nei in graph[node]:
        if nei.isupper() or nei not in visited:
            if nei.islower():
                visited.add(nei)
                total += dfs(nei, visited, used, graph)
                visited.remove(nei)
            else:
                total += dfs(nei, visited, used, graph)
        elif not used and nei not in ("start","end"):
            total += dfs(nei, visited, True, graph)
    return total

with open(sys.argv[1]) as f:
    graph = {}
    for line in f:
        a,b = line.strip().split("-")
        graph.setdefault(a,[]).append(b)
        graph.setdefault(b,[]).append(a)
p1 = dfs("start", set(["start"]), True, graph)
p2 = dfs("start", set(["start"]), False, graph)
print(p1, p2)