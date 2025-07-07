import sys
import heapq

def navigate(grid, minval, maxval):
    h, w = len(grid), len(grid[0])
    goal = (h-1, w-1)
    heap = [(0, 0, 0, 0), (0, 0, 0, 1)]
    seen = set()
    while heap:
        cost, y, x, d = heapq.heappop(heap)
        if (y, x) == goal:
            return cost
        if (y, x, d) in seen:
            continue
        seen.add((y, x, d))
        for s in (-1, 1):
            c = cost
            for i in range(1, maxval+1):
                ny = y + (i*s if d==0 else 0)
                nx = x + (i*s if d==1 else 0)
                if not (0 <= ny < h and 0 <= nx < w):
                    break
                c += grid[ny][nx]
                if (ny, nx, 1-d) in seen:
                    continue
                if i >= minval:
                    heapq.heappush(heap, (c, ny, nx, 1-d))

def part1(data):
    grid = [[int(c) for c in line] for line in data]
    return navigate(grid, 1, 3)

def part2(data):
    grid = [[int(c) for c in line] for line in data]
    return navigate(grid, 4, 10)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f if line.strip()]
    print(part1(data), part2(data))