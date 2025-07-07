import sys, heapq

def navigate(grid, H, W, minval, maxval):
    seen = [[0]*W for _ in range(H)]
    goal_y, goal_x = H-1, W-1
    heap = [(0, 0, 0, 0), (0, 0, 0, 1)]
    heapq.heapify(heap)
    while heap:
        cost, y, x, d = heapq.heappop(heap)
        if y == goal_y and x == goal_x:
            return cost
        if seen[y][x] >> d & 1:
            continue
        seen[y][x] |= 1 << d
        for s in (-1, 1):
            nc = cost
            for i in range(1, maxval+1):
                if d:
                    yy, xx = y, x + s*i
                else:
                    yy, xx = y + s*i, x
                if yy < 0 or yy >= H or xx < 0 or xx >= W:
                    break
                nc += grid[yy][xx]
                od = d ^ 1
                if seen[yy][xx] >> od & 1:
                    continue
                if i >= minval:
                    heapq.heappush(heap, (nc, yy, xx, od))

if __name__ == "__main__":
    data = [line.strip() for line in open(sys.argv[1]) if line.strip()]
    grid = [[int(c) for c in line] for line in data]
    H, W = len(grid), len(grid[0])
    a = navigate(grid, H, W, 1, 3)
    b = navigate(grid, H, W, 4, 10)
    sys.stdout.write(f"{a} {b}")