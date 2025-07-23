To solve this problem, we need to efficiently determine the number of activated reactor cubes after processing a series of toggle commands (either "on" or "off") in a 3D grid. The challenge is to handle both a constrained region (Part 1) and an unbounded region (Part 2) optimally.

### Approach
1. **Part 1 (Constrained Region -50 to 50)**:
   - **Problem Analysis**: The task involves processing toggle commands within a fixed 3D grid (-50 to 50 inclusive). Each command either turns on or off a cuboid region within this grid.
   - **Approach**: We use a 3D boolean array (101x101x101) to represent the grid. For each command, if the cuboid lies entirely within the grid, we update the corresponding region in the array. Finally, we count all activated cubes.
   - **Optimization**: The grid size is manageable (101^3 ≈ 1 million elements), so direct updates are feasible. The solution efficiently checks and processes each command within the grid bounds.

2. **Part 2 (Unbounded Region)**:
   - **Problem Analysis**: The cuboids can now be arbitrarily large, making a direct grid representation infeasible. Instead, we use a non-overlapping cuboid technique to dynamically maintain activated regions.
   - **Approach**: 
     - **Non-overlapping Cuboids**: We maintain a list of non-overlapping cuboids that are currently activated. For each new command:
       - **Overlap Handling**: For each existing activated cuboid overlapping with the new command's cuboid, we split it into up to 6 smaller non-overlapping cuboids (left, right, front, back, bottom, top) around the overlapping region.
       - **Command Processing**: After processing overlaps, if the command is "on", we add the new cuboid to the list.
     - **Volume Calculation**: After processing all commands, the total activated volume is the sum of the volumes of all cuboids in the list.
   - **Optimization**: This method efficiently handles large regions by dynamically adjusting the list of activated cuboids, avoiding the need for an explicit grid. The splitting ensures no overlaps, simplifying volume calculation.

### Solution Code

import sys
import re
import numpy as np
from dataclasses import dataclass

def part1(data):
    regex = r"^(on|off) x=([0-9-]+)\.\.([0-9-]+),y=([0-9-]+)\.\.([0-9-]+),z=([0-9-]+)\.\.([0-9-]+)$"
    steps = [re.match(regex, line).groups() for line in data]

    DIM = 50
    grid = np.zeros((2 * DIM + 1, 2 * DIM + 1, 2 * DIM + 1), dtype=int)

    for toggle, x1, x2, y1, y2, z1, z2 in steps:
        x1, x2 = int(x1) + DIM, int(x2) + DIM
        y1, y2 = int(y1) + DIM, int(y2) + DIM
        z1, z2 = int(z1) + DIM, int(z2) + DIM
        if x1 >= 0 and x2 < 2 * DIM + 1 and y1 >= 0 and y2 < 2 * DIM + 1 and z1 >= 0 and z2 < 2 * DIM + 1:
            grid[x1:x2+1, y1:y2+1, z1:z2+1] = (toggle == "on")

    return np.sum(grid)

@dataclass
class Cube:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

def overlaps(a, b):
    return not (a.x2 < b.x1 or b.x2 < a.x1 or
                a.y2 < b.y1 or b.y2 < a.y1 or
                a.z2 < b.z1 or b.z2 < a.z1)

def part2(data):
    regex = r"^(on|off) x=([0-9-]+)\.\.([0-9-]+),y=([0-9-]+)\.\.([0-9-]+),z=([0-9-]+)\.\.([0-9-]+)$"
    inputs = [re.match(regex, line).groups() for line in data]
    steps = [(toggle == "on", Cube(*map(int, coords))) for toggle, *coords in inputs]
    
    on_set = []
    
    for toggle, new_cube in steps:
        new_on_set = []
        for cube in on_set:
            if not overlaps(cube, new_cube):
                new_on_set.append(cube)
            else:
                if cube.x1 < new_cube.x1:
                    new_on_set.append(Cube(cube.x1, new_cube.x1 - 1, cube.y1, cube.y2, cube.z1, cube.z2))
                if cube.x2 > new_cube.x2:
                    new_on_set.append(Cube(new_cube.x2 + 1, cube.x2, cube.y1, cube.y2, cube.z1, cube.z2))
                
                x_low = max(cube.x1, new_cube.x1)
                x_high = min(cube.x2, new_cube.x2)
                if x_low <= x_high:
                    if cube.y1 < new_cube.y1:
                        new_on_set.append(Cube(x_low, x_high, cube.y1, new_cube.y1 - 1, cube.z1, cube.z2))
                    if cube.y2 > new_cube.y2:
                        new_on_set.append(Cube(x_low, x_high, new_cube.y2 + 1, cube.y2, cube.z1, cube.z2))
                    
                    y_low = max(cube.y1, new_cube.y1)
                    y_high = min(cube.y2, new_cube.y2)
                    if y_low <= y_high:
                        if cube.z1 < new_cube.z1:
                            new_on_set.append(Cube(x_low, x_high, y_low, y_high, cube.z1, new_cube.z1 - 1))
                        if cube.z2 > new_cube.z2:
                            new_on_set.append(Cube(x_low, x_high, y_low, y_high, new_cube.z2 + 1, cube.z2))
        if toggle:
            new_on_set.append(new_cube)
        on_set = new_on_set
    
    total_volume = 0
    for cube in on_set:
        total_volume += (cube.x2 - cube.x1 + 1) * (cube.y2 - cube.y1 + 1) * (cube.z2 - cube.z1 + 1)
    return total_volume

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")


### Explanation
1. **Part 1**:
   - **Grid Initialization**: A 3D numpy array of size 101x101x101 (covering -50 to 50) is initialized to zero (off).
   - **Command Processing**: For each command, if the cuboid lies within the grid, the corresponding region is updated to 1 (on) or 0 (off) based on the command.
   - **Result Calculation**: The total number of activated cubes is the sum of the grid array.

2. **Part 2**:
   - **Non-overlapping Cuboids**: The solution maintains a list of non-overlapping cuboids that are activated.
   - **Splitting Overlaps**: For each new command, existing cuboids overlapping with the new cuboid are split into smaller non-overlapping cuboids around the overlap region.
   - **Command Handling**: If the command is "on", the new cuboid is added to the list. This ensures the list remains non-overlapping.
   - **Volume Calculation**: The total activated volume is computed by summing the volumes of all cuboids in the list, calculated as the product of their dimensions (using inclusive boundaries).

This approach efficiently handles both constrained and unbounded regions by leveraging spatial partitioning and dynamic updates, ensuring optimal performance and correctness.