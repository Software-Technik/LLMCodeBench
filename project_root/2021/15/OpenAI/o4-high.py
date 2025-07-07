import sys, heapq

def dijkstra(grid):
    h, w = len(grid), len(grid[0])
    dist = [[10**18]*w for _ in range(h)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]
    while pq:
        d, x, y = heapq.heappop(pq)
        if d > dist[x][y]:
            continue
        if x == h-1 and y == w-1:
            return d
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w:
                nd = d + grid[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))
    return dist[h-1][w-1]

def part1(lines):
    grid = [list(map(int, line)) for line in lines]
    return dijkstra(grid)

def part2(lines):
    orig = [list(map(int, line)) for line in lines]
    oh, ow = len(orig), len(orig[0])
    h, w = oh*5, ow*5
    grid = [[0]*w for _ in range(h)]
    for i in range(h):
        ri = orig[i%oh]
        add_i = i//oh
        for j in range(w):
            v = ri[j%ow] + add_i + j//ow
            grid[i][j] = (v-1)%9 + 1
    return dijkstra(grid)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    a = part1(lines)
    b = part2(lines)
    sys.stdout.write(f"{a} {b}")