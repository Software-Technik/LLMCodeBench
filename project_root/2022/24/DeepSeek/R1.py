To solve this problem, we need to navigate through a grid filled with moving blizzards to reach a target position in the shortest time possible. The blizzards move in specific directions and wrap around the grid when they reach the boundaries. The solution involves simulating the movement of blizzards over time and using a breadth-first search (BFS) to explore possible paths while avoiding blizzards and walls.

### Approach
1. **Problem Analysis**: The grid consists of walls, open spaces, and blizzards that move in four directions (up, down, left, right). Blizzards wrap around the grid when they hit boundaries. The goal is to move from the start position to the target position in the shortest time, avoiding blizzards and walls. For part two, the task extends to going from start to target, back to start, and then to the target again.

2. **Key Insight**: The blizzards' positions repeat periodically. The period is the least common multiple (LCM) of the grid's inner dimensions (height-2 and width-2). This periodicity allows us to precompute blizzard positions for each time modulo the period, optimizing the BFS by avoiding redundant state checks.

3. **Algorithm Selection**: 
   - **BFS with State Tracking**: We use BFS to explore all possible moves (up, down, left, right, or wait) at each time step. The state includes the current position and time modulo the blizzard period.
   - **Blizzard Position Caching**: For each time modulo the period, we cache the set of positions occupied by blizzards. This avoids recalculating blizzard positions for the same time modulo in the BFS.

4. **Complexity Analysis**: 
   - **Precomputation**: For each time modulo the period, we compute blizzard positions in O(B) time, where B is the number of blizzards. The period T is at most (H-2)*(W-2) (LCM of H-2 and W-2), leading to O(T*B) time.
   - **BFS**: In the worst case, BFS explores O(T*H*W) states. Each state processes up to 5 moves (including waiting), leading to O(5*T*H*W) operations.

### Solution Code

import sys
import math
from collections import deque

def lcm(a, b):
    return a * b // math.gcd(a, b)

def parse_data(data):
    directions = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }
    h = len(data)
    w = len(data[0])
    right_set = set()
    left_set = set()
    down_set = set()
    up_set = set()
    
    for y, line in enumerate(data[1:-1], 1):
        for x, c in enumerate(line[1:-1], 1):
            if c in directions:
                dr = directions[c]
                if dr == (0, 1):
                    right_set.add((y, x))
                elif dr == (0, -1):
                    left_set.add((y, x))
                elif dr == (1, 0):
                    down_set.add((y, x))
                elif dr == (-1, 0):
                    up_set.add((y, x))
                    
    return right_set, left_set, down_set, up_set

def BFS_leg(data, start, target, start_time, w, h, T_cycle, right_set, left_set, down_set, up_set):
    blizzard_cache = {}
    visited = [[[False] * w for _ in range(h)] for _ in range(T_cycle)]
    
    queue = deque()
    t0_mod = start_time % T_cycle
    visited[t0_mod][start[0]][start[1]] = True
    queue.append((start[0], start[1], start_time))
    
    while queue:
        y, x, t = queue.popleft()
        if (y, x) == target:
            return t
        
        t_next = t + 1
        t_mod = t_next % T_cycle
        
        if t_mod not in blizzard_cache:
            moved_set = set()
            for (y0, x0) in right_set:
                new_x = (x0 - 1 + t_mod) % (w - 2) + 1
                moved_set.add((y0, new_x))
            for (y0, x0) in left_set:
                new_x = (x0 - 1 - t_mod) % (w - 2) + 1
                moved_set.add((y0, new_x))
            for (y0, x0) in down_set:
                new_y = (y0 - 1 + t_mod) % (h - 2) + 1
                moved_set.add((new_y, x0))
            for (y0, x0) in up_set:
                new_y = (y0 - 1 - t_mod) % (h - 2) + 1
                moved_set.add((new_y, x0))
            blizzard_cache[t_mod] = moved_set
        else:
            moved_set = blizzard_cache[t_mod]
        
        for d in [(0,1), (1,0), (0,-1), (-1,0), (0,0)]:
            ny = y + d[0]
            nx = x + d[1]
            
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if ny == 0 and nx != 1:
                continue
            if ny == h - 1 and nx != w - 2:
                continue
            if 0 < ny < h - 1 and (nx == 0 or nx == w - 1):
                continue
            
            if (ny, nx) == (0, 1) or (ny, nx) == (h - 1, w - 2):
                pass
            else:
                if (ny, nx) in moved_set:
                    continue
                    
            if not visited[t_mod][ny][nx]:
                visited[t_mod][ny][nx] = True
                queue.append((ny, nx, t_next))
                
    return None

def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        data = [line.strip() for line in f]
    
    h = len(data)
    w = len(data[0])
    right_set, left_set, down_set, up_set = parse_data(data)
    T_cycle = lcm(h - 2, w - 2)
    
    start = (0, 1)
    target = (h - 1, w - 2)
    
    part1 = BFS_leg(data, start, target, 0, w, h, T_cycle, right_set, left_set, down_set, up_set)
    t2 = BFS_leg(data, target, start, part1, w, h, T_cycle, right_set, left_set, down_set, up_set)
    part2 = BFS_leg(data, start, target, t2, w, h, T_cycle, right_set, left_set, down_set, up_set)
    
    print(part1)
    print(part2)

if __name__ == "__main__":
    main()


### Explanation
1. **Problem Analysis**: The problem involves navigating a grid with moving blizzards. The blizzards move in specific directions and wrap around the grid edges. The solution requires finding the shortest path from start to target, and for part two, additionally returning to start and then back to the target.
2. **Blizzard Movement**: Blizzard positions are periodic with a period determined by the LCM of the grid's inner dimensions. This periodicity allows efficient caching of blizzard positions for each time modulo the period.
3. **BFS with Caching**: The BFS explores possible moves (including waiting) at each time step. For efficiency, blizzard positions for each time modulo the period are cached to avoid redundant calculations.
4. **Efficiency**: The BFS explores states defined by position and time modulo the period. The caching ensures each state is processed once, leading to an optimal solution within feasible time and memory limits for typical grid sizes. The solution handles part two by running BFS sequentially for each leg of the journey.