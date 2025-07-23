import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    lines = data.splitlines()

lines = [list(line) for line in lines]

directions = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0]

# Part 1
grid = [row[:] for row in lines]
H = len(grid)
W = len(grid[0])
changed = True
while changed:
    changed = False
    new_grid = [[''] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if grid[y][x] == '.':
                new_grid[y][x] = '.'
                continue
            cnt = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] == '#':
                    cnt += 1
            if grid[y][x] == 'L' and cnt == 0:
                new_grid[y][x] = '#'
                changed = True
            elif grid[y][x] == '#' and cnt >= 4:
                new_grid[y][x] = 'L'
                changed = True
            else:
                new_grid[y][x] = grid[y][x]
    grid = new_grid

result1 = sum(1 for y in range(H) for x in range(W) if grid[y][x] == '#')

# Part 2
grid = [row[:] for row in lines]
H = len(grid)
W = len(grid[0])
changed = True
while changed:
    changed = False
    new_grid = [[''] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if grid[y][x] == '.':
                new_grid[y][x] = '.'
                continue
            cnt = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while 0 <= nx < W and 0 <= ny < H:
                    if grid[ny][nx] == '#':
                        cnt += 1
                        break
                    if grid[ny][nx] == 'L':
                        break
                    nx += dx
                    ny += dy
            if grid[y][x] == 'L' and cnt == 0:
                new_grid[y][x] = '#'
                changed = True
            elif grid[y][x] == '#' and cnt >= 5:
                new_grid[y][x] = 'L'
                changed = True
            else:
                new_grid[y][x] = grid[y][x]
    grid = new_grid

result2 = sum(1 for y in range(H) for x in range(W) if grid[y][x] == '#')

print(result1, result2)