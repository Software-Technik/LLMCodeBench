import sys

def main():
    with open(sys.argv[1]) as f:
        points = [tuple(map(int, line.split(','))) for line in f]
    n = len(points)
    dims = len(points[0]) if n else 0
    adj = [[] for _ in range(n)]
    for i in range(n):
        pi = points[i]
        for j in range(i+1, n):
            pj = points[j]
            dist = 0
            for k in range(dims):
                dist += abs(pi[k] - pj[k])
                if dist > 3:
                    break
            if dist <= 3:
                adj[i].append(j)
                adj[j].append(i)
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
    print(count)

if __name__ == '__main__':
    main()