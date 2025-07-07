import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
adj=defaultdict(list)
with open(sys.argv[1]) as f:
    for line in f:
        a,b=line.strip().split('-')
        if b!='start' and a!='end': adj[a].append(b)
        if a!='start' and b!='end': adj[b].append(a)
def dfs(node, visited, used):
    if node=='end': return 1
    total=0
    for nei in adj[node]:
        if nei.isupper():
            total+=dfs(nei, visited, used)
        else:
            cnt=visited.get(nei,0)
            if cnt==0:
                visited[nei]=1
                total+=dfs(nei, visited, used)
                del visited[nei]
            elif cnt==1 and not used:
                visited[nei]=2
                total+=dfs(nei, visited, True)
                visited[nei]=1
    return total
v={'start':1}
p1=dfs('start', v, True)
v={'start':1}
p2=dfs('start', v, False)
sys.stdout.write(f"{p1} {p2}")