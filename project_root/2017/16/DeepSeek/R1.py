To solve this problem, we need to efficiently simulate a sequence of dance moves performed by a group of programs. The challenge involves two parts: performing a single dance and performing a billion dances. Given the constraints, we need an optimized solution that avoids excessive computation and memory usage, especially for the billion-dance scenario.

### Approach
1. **Parsing Instructions**: The input consists of a series of dance moves (spin, exchange, partner) which are parsed into a structured format for easy processing.
2. **Single Dance Simulation**: The `dance` function processes each move in sequence:
   - **Spin (sX)**: Rotates the list of programs by moving the last X programs to the front.
   - **Exchange (xA/B)**: Swaps programs at positions A and B.
   - **Partner (pA/B)**: Swaps programs A and B regardless of their positions.
3. **Billion Dances Simulation**: The `long_dance` function efficiently handles the billion iterations by detecting cycles in the sequence of states. Once a cycle is detected, it calculates the result based on the cycle's start and length, avoiding unnecessary repeated computations.

### Solution Code

import sys

def parse_instruction(instruction):
    first = instruction[0]
    rest = instruction[1:]
    if first == 's':
        return ('s', int(rest))
    elif first == 'x':
        a, b = map(int, rest.split('/'))
        return ('x', a, b)
    elif first == 'p':
        a, b = rest.split('/')
        return ('p', a, b)
    else:
        return None

def dance(dancers, instructions):
    dancers = list(dancers)
    for instr in instructions:
        if instr[0] == 's':
            x = instr[1]
            dancers = dancers[-x:] + dancers[:-x]
        elif instr[0] == 'x':
            a, b = instr[1], instr[2]
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif instr[0] == 'p':
            a_idx = dancers.index(instr[1])
            b_idx = dancers.index(instr[2])
            dancers[a_idx], dancers[b_idx] = dancers[b_idx], dancers[a_idx]
    return ''.join(dancers)

def long_dance(dancers, instructions, iterations):
    seen = {}
    states = []
    current = dancers
    for i in range(iterations):
        if current in seen:
            cycle_start = seen[current]
            cycle_length = i - cycle_start
            idx = (iterations - cycle_start) % cycle_length + cycle_start
            return states[idx]
        seen[current] = i
        states.append(current)
        current = dance(current, instructions)
    return current

input_file = sys.argv[1]
with open(input_file) as f:
    content = f.read().strip()

instructions_strs = [inst.strip() for inst in content.split(',') if inst.strip()]
parsed_instructions = [parse_instruction(inst) for inst in instructions_strs]

programs = "abcdefghijklmnop"
print(dance(programs, parsed_instructions))
print(long_dance(programs, parsed_instructions, 1000000000))


### Explanation
1. **Parsing Instructions**: The `parse_instruction` function converts each move string into a tuple representing the move type and parameters. For example, "s3" becomes `('s', 3)`.
2. **Single Dance Simulation**: The `dance` function processes each move:
   - **Spin (sX)**: Uses list slicing to rotate the programs.
   - **Exchange (xA/B)**: Directly swaps elements at positions A and B.
   - **Partner (pA/B)**: Finds the positions of programs A and B and swaps them.
3. **Billion Dances Simulation**: The `long_dance` function:
   - Tracks encountered states in a dictionary (`seen`) and a list (`states`).
   - For each iteration, checks if the current state has been seen before. If a cycle is detected, it calculates the result using the cycle's start and length, leveraging modular arithmetic to avoid redundant computations.
   - This approach efficiently handles the large number of iterations by minimizing repeated work through cycle detection and early termination.

This solution ensures optimal performance by leveraging cycle detection to avoid unnecessary computations, making it feasible to handle the billion-iteration scenario efficiently.