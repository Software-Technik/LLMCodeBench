import sys

def find(p, x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def union(p, r, x, y):
    rx, ry = find(p, x), find(p, y)
    if rx == ry: return
    if r[rx] < r[ry]:
        p[rx] = ry
    else:
        p[ry] = rx
        if r[rx] == r[ry]:
            r[rx] += 1

input_f = sys.argv[1]
with open(input_f) as f:
    points = [tuple(map(int, line.split(','))) for line in f]

n = len(points)
p = list(range(n))
r = [0] * n

for i in range(n):
    xi, yi, zi, ti = points[i]
    for j in range(i+1, n):
        xj, yj, zj, tj = points[j]
        if abs(xi-xj) + abs(yi-yj) + abs(zi-zj) + abs(ti-tj) <= 3:
            union(p, r, i, j)

roots = set(find(p, i) for i in range(n))
sys.stdout.write(str(len(roots)))