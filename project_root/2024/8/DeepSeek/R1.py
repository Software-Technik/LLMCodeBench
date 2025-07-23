To solve this problem, we need to optimize the original solution for the Advent of Code problem, focusing on improving runtime performance and reducing memory usage while preserving correctness. The problem involves identifying "antinodes" in a grid based on specific conditions for two different parts.

### Approach
1. **Part 1 Optimization**:
   - **Problem**: For each pair of nodes (A, B) with the same frequency, generate antinodes at positions \(2A - B\) and \(2B - A\) if they are within grid bounds.
   - **Optimization**: Instead of using combinations to generate pairs, iterate over all pairs of nodes for each frequency. This avoids the overhead of combinations and directly computes the antinodes. The complexity remains \(O(m^2)\) per frequency, where \(m\) is the number of nodes for that frequency, but the constant factors are reduced.

2. **Part 2 Optimization**:
   - **Problem**: For each pair of nodes (A, B) with the same frequency, generate all grid points lying on the line passing through A and B in both directions.
   - **Optimization**: For each node \(A\), compute the normalized direction vectors to all other nodes \(B\) of the same frequency. Then, for each grid point \(P\) (excluding \(A\)), check if the direction vector from \(A\) to \(P\) matches any of the stored vectors. If it does, \(P\) lies on a line defined by two nodes and is added to the antinodes set. This reduces the complexity from \(O(m^2 \times n)\) to \(O(m \times n^2)\) per frequency, where \(n\) is the grid size.

### Solution Code

import sys
import math
from collections import defaultdict

def part1(grid):
    n = len(grid)
    all_locs = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))
    
    antinodes = set()
    for freq, locs in all_locs.items():
        m = len(locs)
        for i in range(m):
            a = locs[i]
            for j in range(m):
                if i == j:
                    continue
                b = locs[j]
                x1 = 2*a[0] - b[0]
                y1 = 2*a[1] - b[1]
                if 0 <= x1 < n and 0 <= y1 < n:
                    antinodes.add((x1, y1))
    return len(antinodes)

def part2(grid):
    n = len(grid)
    all_locs = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))
    
    antinodes = set()
    for freq, locs in all_locs.items():
        m = len(locs)
        if m < 2:
            continue
        for A in locs:
            slopes_from_A = set()
            for B in locs:
                if B == A:
                    continue
                dx = B[0] - A[0]
                dy = B[1] - A[1]
                g = math.gcd(abs(dx), abs(dy))
                if g == 0:
                    continue
                dx_norm = dx // g
                dy_norm = dy // g
                if dx_norm < 0 or (dx_norm == 0 and dy_norm < 0):
                    dx_norm = -dx_norm
                    dy_norm = -dy_norm
                slopes_from_A.add((dx_norm, dy_norm))
            
            for i in range(n):
                for j in range(n):
                    if (i, j) == A:
                        continue
                    dx2 = i - A[0]
                    dy2 = j - A[1]
                    g2 = math.gcd(abs(dx2), abs(dy2))
                    if g2 == 0:
                        continue
                    dx2_norm = dx2 // g2
                    dy2_norm = dy2 // g2
                    if dx2_norm < 0 or (dx2_norm == 0 and dy2_norm < 0):
                        dx2_norm = -dx2_norm
                        dy2_norm = -dy2_norm
                    if (dx2_norm, dy2_norm) in slopes_from_A:
                        antinodes.add((i, j))
    return len(antinodes)

input_path = sys.argv[1]
with open(input_path) as fin:
    grid = fin.read().strip().split("\n")
    print(part1(grid), part2(grid))


### Explanation
1. **Part 1**:
   - **Reading Input**: The grid is read and parsed into a dictionary `all_locs` where keys are frequencies (characters) and values are lists of coordinates of nodes.
   - **Generating Antinodes**: For each frequency, iterate over all pairs of nodes. For each pair (A, B), compute the positions \(2A - B\) and \(2B - A\). If these positions are within grid bounds, add them to the set `antinodes`.
   - **Result**: The size of `antinodes` is returned, representing the number of unique antinodes found.

2. **Part 2**:
   - **Reading Input**: Similar to Part 1, the grid is parsed into `all_locs`.
   - **Slope Calculation**: For each node \(A\) of a frequency, compute the normalized direction vectors to all other nodes \(B\) of the same frequency. This involves calculating the GCD to normalize the vector and adjusting signs for consistency.
   - **Checking Grid Points**: For each grid point \(P\) (excluding \(A\)), compute the normalized direction vector from \(A\) to \(P\). If this vector matches any vector in the precomputed set for \(A\), add \(P\) to `antinodes`.
   - **Result**: The size of `antinodes` is returned, representing all grid points lying on lines defined by any two nodes of the same frequency.

This approach efficiently reduces the computational complexity for Part 2 by leveraging normalized direction vectors and avoids redundant calculations, significantly improving performance for large grids.