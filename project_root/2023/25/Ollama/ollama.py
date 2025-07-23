M = defaultdict(set)
for line in sys.stdin:
    src, dst = line.split(': ')
    for de in dst.split():
        M[src].add(de)
        M[de].add(src)

visited = {next(iter(M)): (0, [])}
heap = [(0, next(iter(M)), [])]
nodelen = len(M)
while heap:
    dist, node, path = heappop(heap)
    if len(path) < 3 or all((path[i], path[i + 1]) == (path[j], path[j + 1]) for i in range(len(path) - 1) for j in range(i)):
        for de in M[node]:
            exclusions = {(node, de), (de, node)}
            if len(path) > 2 and all((path[i], path[i + 1]) == (path[j], path[j + 1]) for i in range(len(path) - 1) for j in range(i)):
                continue
            new_visited = {next(iter(M)): (nodelen, [])}
            if de not in new_visited:
                new_visited[de] = (dist + 1, path + [node, de])
                heappush(heap, (dist + 1, de, path + [node, de]))
        visited.update(new_visited)
        nodelen += len(new_visited) - 1
sys.stdout.write(f"{nodelen * (len(M) - nodelen)}")