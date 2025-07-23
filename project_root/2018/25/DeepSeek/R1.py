import sys

def main():
    input_f = sys.argv[1]
    with open(input_f) as f:
        points = [tuple(int(n) for n in line.strip().split(',')) for line in f]

    grid = {}
    for p in points:
        key = (p[0]//4, p[1]//4, p[2]//4, p[3]//4)
        if key not in grid:
            grid[key] = []
        grid[key].append(p)
    
    parent = {p: p for p in points}
    rank = {p: 0 for p in points}
    
    def find(x):
        path = []
        while parent[x] != x:
            path.append(x)
            x = parent[x]
        for node in path:
            parent[node] = x
        return x

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1

    for p in points:
        k0, k1, k2, k3 = p[0]//4, p[1]//4, p[2]//4, p[3]//4
        for d0 in (-1, 0, 1):
            for d1 in (-1, 0, 1):
                for d2 in (-1, 0, 1):
                    for d3 in (-1, 0, 1):
                        nkey = (k0+d0, k1+d1, k2+d2, k3+d3)
                        if nkey not in grid:
                            continue
                        for q in grid[nkey]:
                            if p < q:
                                s = abs(p[0]-q[0])
                                if s > 3:
                                    continue
                                s += abs(p[1]-q[1])
                                if s > 3:
                                    continue
                                s += abs(p[2]-q[2])
                                if s > 3:
                                    continue
                                s += abs(p[3]-q[3])
                                if s <= 3:
                                    union(p, q)
    
    count = sum(1 for p in points if parent[p] == p)
    sys.stdout.write(str(count))

if __name__ == "__main__":
    main()