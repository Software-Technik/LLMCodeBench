import sys

def run_steps(grid, steps=None):
    total_flashes = 0
    step = 0
    rows, cols = len(grid), len(grid[0])
    while True:
        step += 1
        stack = []
        flashed = [[False]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    stack.append((i, j))
        while stack:
            i, j = stack.pop()
            if flashed[i][j]:
                continue
            flashed[i][j] = True
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < rows and 0 <= nj < cols and not flashed[ni][nj]:
                        grid[ni][nj] += 1
                        if grid[ni][nj] > 9:
                            stack.append((ni, nj))
        step_flashes = 0
        for i in range(rows):
            for j in range(cols):
                if flashed[i][j]:
                    grid[i][j] = 0
                    step_flashes += 1
        if steps is not None:
            total_flashes += step_flashes
            if step == steps:
                return total_flashes
        if steps is None and step_flashes == rows*cols:
            return step

def main():
    data = [list(map(int, line.strip())) for line in open(sys.argv[1]) if line.strip()]
    import copy
    grid1 = copy.deepcopy(data)
    grid2 = copy.deepcopy(data)
    p1 = run_steps(grid1, steps=100)
    p2 = run_steps(grid2, steps=None)
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()