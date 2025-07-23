import sys

def part1(data):
    state = ''.join(data)
    size = 5
    total = size * size
    adjacent = []
    for i in range(total):
        x, y = i % size, i // size
        neighbors = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < size and 0 <= ny < size:
                neighbors.append(ny * size + nx)
        adjacent.append(neighbors)
    
    seen = set()
    while state not in seen:
        seen.add(state)
        new_state = []
        for i in range(total):
            count = 0
            for j in adjacent[i]:
                if state[j] == '#':
                    count += 1
            if state[i] == '#':
                new_char = '.' if count != 1 else '#'
            else:
                new_char = '#' if count in (1,2) else '.'
            new_state.append(new_char)
        state = ''.join(new_state)
    
    result = 0
    for i, c in enumerate(state):
        if c == '#':
            result += 1 << i
    return result

def createlevel2(data):
    level = {}
    for y in range(5):
        line = data[y]
        for x in range(5):
            if (x, y) == (2, 2):
                continue
            level[(x, y)] = line[x]
    return level

def part2(data):
    points = [(x, y) for x in range(5) for y in range(5) if (x, y) != (2, 2)]
    neighbor_map = {}
    for (x, y) in points:
        lst = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) != (2, 2):
                lst.append((0, nx, ny))
        if x == 0:
            lst.append((1, 1, 2))
        if x == 4:
            lst.append((1, 3, 2))
        if y == 0:
            lst.append((1, 2, 1))
        if y == 4:
            lst.append((1, 2, 3))
        if (x, y) == (2, 1):
            for i in range(5):
                lst.append((-1, i, 0))
        if (x, y) == (1, 2):
            for i in range(5):
                lst.append((-1, 0, i))
        if (x, y) == (3, 2):
            for i in range(5):
                lst.append((-1, 4, i))
        if (x, y) == (2, 3):
            for i in range(5):
                lst.append((-1, i, 4))
        neighbor_map[(x, y)] = lst

    levels = {0: createlevel2(data)}
    empty = {p: '.' for p in points}
    
    for minute in range(200):
        newlevels = {}
        min_depth = -minute - 1
        max_depth = minute + 1
        for depth in range(min_depth, max_depth + 1):
            current_grid = levels.get(depth, empty)
            new_grid = {}
            for pos in points:
                count = 0
                for nd, nx, ny in neighbor_map[pos]:
                    target_depth = depth + nd
                    grid_at_target = levels.get(target_depth, empty)
                    state = grid_at_target.get((nx, ny), '.')
                    if state == '#':
                        count += 1
                current_char = current_grid.get(pos, '.')
                if current_char == '#':
                    new_char = '.' if count != 1 else '#'
                else:
                    new_char = '#' if count in (1, 2) else '.'
                new_grid[pos] = new_char
            newlevels[depth] = new_grid
        levels = newlevels

    total = 0
    for grid in levels.values():
        for char in grid.values():
            if char == '#':
                total += 1
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")