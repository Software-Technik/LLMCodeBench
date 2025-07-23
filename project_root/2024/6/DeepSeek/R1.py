To solve this problem, we need to optimize the given Python code for both parts of the problem while preserving correctness. The goal is to improve runtime performance and reduce memory usage without altering the output for the same input.

### Approach
1. **Part 1 Optimization**:
   - **Finding the Starting Position**: The code searches for the starting position (marked by '^') in the grid. This is done efficiently by breaking out of the loops as soon as the position is found.
   - **Simulating the Path**: The guard moves in a straight line until it hits a wall ('#'), then turns right (direction changes in modulo 4). The path is simulated until the guard moves out of bounds. The visited positions are stored in a set, and the size of this set is returned.

2. **Part 2 Optimization**:
   - **Reusing State Set**: Instead of creating a new set for each simulation (when placing an obstacle), a single set is reused. This set is cleared before each simulation to save memory and reduce overhead.
   - **Inline Simulation**: The simulation for each obstacle placement is inlined within the loop, avoiding the overhead of function calls. The grid is temporarily modified to place an obstacle, and the simulation checks if the guard enters a loop (repeats a state) or exits the grid.
   - **Efficient State Tracking**: The simulation tracks the guard's position and direction. If a state (position and direction) repeats, it indicates a loop, and the obstacle placement is counted.

### Solution Code

import sys

def part1(input_path):
    with open(input_path) as fin:
        grid = fin.read().strip().split("\n")

    n = len(grid)
    m = len(grid[0])

    found = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                found = True
                break
        if found:
            break

    dir = 0
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    seen = set()
    while True:
        seen.add((i, j))

        next_i = i + dd[dir][0]
        next_j = j + dd[dir][1]

        if not (0 <= next_i < n and 0 <= next_j < n):
            break

        if grid[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j

    return len(seen)

def part2(input_path):
    with open(input_path) as fin:
        grid = [list(line) for line in fin.read().strip().split("\n")]

    n = len(grid)
    m = len(grid[0])

    found = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                found = True
                break
        if found:
            break

    ii = i
    jj = j

    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    dir = 0
    og_seen = set()
    while True:
        og_seen.add((i, j))

        next_i = i + dd[dir][0]
        next_j = j + dd[dir][1]

        if not (0 <= next_i < n and 0 <= next_j < n):
            break

        if grid[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j

    ans = 0
    seen_set = set()
    for oi, oj in og_seen:
        if oi == ii and oj == jj:
            continue
        grid[oi][oj] = '#'
        i, j, dir = ii, jj, 0
        seen_set.clear()
        loop = False
        while True:
            state = (i, j, dir)
            if state in seen_set:
                loop = True
                break
            seen_set.add(state)

            next_i = i + dd[dir][0]
            next_j = j + dd[dir][1]

            if not (0 <= next_i < n and 0 <= next_j < n):
                break

            if grid[next_i][next_j] == '#':
                dir = (dir + 1) % 4
            else:
                i, j = next_i, next_j

        grid[oi][oj] = '.'
        ans += 1 if loop else 0

    return ans

input_path = sys.argv[1]
print(part1(input_path), part2(input_path))


### Explanation
- **Part 1**: The code reads the grid, locates the starting position ('^'), and simulates the guard's movement. The guard moves straight until hitting a wall, then turns right. The simulation stops when the guard moves out of bounds, and the number of unique positions visited is returned.
- **Part 2**: The grid is processed similarly to Part 1 to find the starting position and the original path. For each position in the original path (except the start), an obstacle ('#') is placed temporarily. The simulation checks if the guard enters a loop (repeats a state) or exits the grid. The obstacle placements causing loops are counted, and the total count is returned. Memory usage is optimized by reusing a set for state tracking across simulations.