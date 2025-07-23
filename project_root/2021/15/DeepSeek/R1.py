import sys
import heapq

def dijkstra(base, part2=False):
    R = len(base)
    C = len(base[0])
    if part2:
        rows = R * 5
        cols = C * 5
    else:
        rows = R
        cols = C
    dist = [[10**18] * cols for _ in range(rows)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]
    target = (rows-1, cols-1)
    while heap:
        cost, i, j = heapq.heappop(heap)
        if (i, j) == target:
            return cost
        if cost != dist[i][j]:
            continue
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < rows and 0 <= nj < cols:
                if part2:
                    base_val = base[ni % R][nj % C]
                    tile_i = ni // R
                    tile_j = nj // C
                    cell_cost = (base_val + tile_i + tile_j - 1) % 9 + 1
                else:
                    cell_cost = base[ni][nj]
                new_cost = cost + cell_cost
                if new_cost < dist[ni][nj]:
                    dist[ni][nj] = new_cost
                    heapq.heappush(heap, (new_cost, ni, nj))
    return dist[rows-1][cols-1]

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    base = []
    for line in data:
        base.append([int(x) for x in line.strip()])

p1 = dijkstra(base, False)
p2 = dijkstra(base, True)
sys.stdout.write(f"{p1} {p2}")