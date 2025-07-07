import sys
import heapq

def dijkstra(grid):
    h, w = len(grid), len(grid[0])
    dist = [[float('inf')]*w for _ in range(h)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]
    while pq:
        d, y, x = heapq.heappop(pq)
        if d>dist[y][x]: continue
        if y==h-1 and x==w-1:
            return d
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y+dy, x+dx
            if 0<=ny<h and 0<=nx<w:
                nd = d + grid[ny][nx]
                if nd<dist[ny][nx]:
                    dist[ny][nx] = nd
                    heapq.heappush(pq, (nd, ny, nx))
    return -1

def part1(data):
    grid = [list(map(int, line)) for line in data.splitlines()]
    return dijkstra(grid)

def part2(data):
    orig = [list(map(int, line)) for line in data.splitlines()]
    h, w = len(orig), len(orig[0])
    H, W = h*5, w*5
    grid = [[0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            v = orig[y%h][x%w] + y//h + x//w
            grid[y][x] = (v-1)%9 + 1
    return dijkstra(grid)

data = open(sys.argv[1]).read()
print(part1(data), part2(data))