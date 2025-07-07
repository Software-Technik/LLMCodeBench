import sys
import heapq

def dijkstra(grid):
    n, m = len(grid), len(grid[0])
    dist = [[10**18]*m for _ in range(n)]
    dist[0][0] = 0
    hq = [(0, 0, 0)]
    while hq:
        d, x, y = heapq.heappop(hq)
        if d > dist[x][y]: continue
        if x == n-1 and y == m-1:
            return d
        if x>0:
            nd = d + grid[x-1][y]
            if nd < dist[x-1][y]:
                dist[x-1][y] = nd
                heapq.heappush(hq, (nd, x-1, y))
        if x+1<n:
            nd = d + grid[x+1][y]
            if nd < dist[x+1][y]:
                dist[x+1][y] = nd
                heapq.heappush(hq, (nd, x+1, y))
        if y>0:
            nd = d + grid[x][y-1]
            if nd < dist[x][y-1]:
                dist[x][y-1] = nd
                heapq.heappush(hq, (nd, x, y-1))
        if y+1<m:
            nd = d + grid[x][y+1]
            if nd < dist[x][y+1]:
                dist[x][y+1] = nd
                heapq.heappush(hq, (nd, x, y+1))

def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    orig = [[int(c) for c in line] for line in lines]
    p1 = dijkstra(orig)
    r, c = len(orig), len(orig[0])
    grid = [[((orig[i%r][j%c] + i//r + j//c - 1) % 9) + 1 for j in range(c*5)] for i in range(r*5)]
    p2 = dijkstra(grid)
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()