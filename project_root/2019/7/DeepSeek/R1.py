To solve this problem, we need to optimize the given Python code for the Advent of Code challenge. The challenge involves simulating a series of amplifiers connected in sequence (part 1) and in a feedback loop (part 2) using an Intcode computer. The goal is to maximize the output signal by finding the optimal phase settings for the amplifiers.

### Approach
1. **Intcode Computer Optimization**:
   - **Parameter Handling**: Simplify the handling of parameters in the Intcode computer. Specifically, for the input instruction (opcode 3), we directly use the next value in the program as the address, ignoring the mode parameter since the problem specifies that parameters for write operations will never be in immediate mode.
   - **Local Variables**: Use local variables to store intermediate values during instruction processing to reduce memory access and improve performance.
   - **Early Termination**: For part 2, the computer stops execution after producing an output and resumes from the same state when provided with new input, allowing efficient feedback loop processing.

2. **Efficient Result Calculation**:
   - **Part 1**: Instead of storing all results for each permutation of phase settings, we keep track of the maximum output encountered during iteration.
   - **Part 2**: Similarly, we compute the maximum output during iteration without storing all intermediate results, reducing memory usage.

3. **Feedback Loop Handling**:
   - **Computer Class**: For part 2, each amplifier is represented as a computer instance that maintains its state (instruction pointer, phase usage, and last output). The feedback loop runs until all amplifiers halt, passing the output of the last amplifier to the first in each iteration.

### Solution Code

import sys
import itertools
import collections

def runComputer1(data, phase, input_val):
    program = data.copy()
    i = 0
    hasUsedPhase = False
    last_output = None

    while i < len(program):
        op = program[i]
        opcode = op % 100
        if opcode == 99:
            break

        mode1 = (op // 100) % 10
        mode2 = (op // 1000) % 10

        if opcode == 1:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = p1 + p2
            i += 4
        elif opcode == 2:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = p1 * p2
            i += 4
        elif opcode == 3:
            addr = program[i+1]
            program[addr] = input_val if hasUsedPhase else phase
            hasUsedPhase = True
            i += 2
        elif opcode == 4:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            last_output = p1
            i += 2
        elif opcode == 5:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            if p1 != 0:
                i = p2
            else:
                i += 3
        elif opcode == 6:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            if p1 == 0:
                i = p2
            else:
                i += 3
        elif opcode == 7:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = 1 if p1 < p2 else 0
            i += 4
        elif opcode == 8:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = 1 if p1 == p2 else 0
            i += 4
        else:
            raise ValueError(f'opcode {opcode} from {op}')
  
    if last_output is None:
        raise ValueError(f'input {input_val} resulted in no output')

    return last_output

def part1(data):
    max_amp = -10**9
    for seq in itertools.permutations(range(5), 5):
        amplification = 0
        for phase in seq:
            amplification = runComputer1(data, phase, amplification)
        if amplification > max_amp:
            max_amp = amplification
    return max_amp

def runComputer2(program, i, input_val, phase, hasUsedPhase):
    while i < len(program):
        op = program[i]
        opcode = op % 100
        if opcode == 99:
            return (i, None, hasUsedPhase)

        mode1 = (op // 100) % 10
        mode2 = (op // 1000) % 10

        if opcode == 1:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = p1 + p2
            i += 4
        elif opcode == 2:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = p1 * p2
            i += 4
        elif opcode == 3:
            addr = program[i+1]
            program[addr] = input_val if hasUsedPhase else phase
            hasUsedPhase = True
            i += 2
        elif opcode == 4:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            i += 2
            return (i, p1, hasUsedPhase)
        elif opcode == 5:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            if p1 != 0:
                i = p2
            else:
                i += 3
        elif opcode == 6:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            if p1 == 0:
                i = p2
            else:
                i += 3
        elif opcode == 7:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = 1 if p1 < p2 else 0
            i += 4
        elif opcode == 8:
            p1 = program[i+1] if mode1 == 1 else program[program[i+1]]
            p2 = program[i+2] if mode2 == 1 else program[program[i+2]]
            p3 = program[i+3]
            program[p3] = 1 if p1 == p2 else 0
            i += 4
        else:
            raise ValueError(f'opcode {opcode} from {op}')
  
    return (i, None, hasUsedPhase)

class Computer:
    def __init__(self, program, phase):
        self.i = 0
        self.lastOutput = None
        self.halted = False
        self.phase = phase
        self.hasUsedPhase = False
        self.program = program.copy()

    def run(self, input_val):
        if self.halted:
            raise RuntimeError("Computer was halted already")
        i, output, hasUsedPhase = runComputer2(self.program, self.i, input_val, self.phase, self.hasUsedPhase)
        self.i = i
        self.halted = (output is None)
        if output is not None:
            self.lastOutput = output
        self.hasUsedPhase = hasUsedPhase
        return output

def part2(data):
    max_amp = -10**9
    for seq in itertools.permutations(range(5, 10), 5):
        computers = []
        for phase in seq:
            computers.append(Computer(data, phase))
        computers[4].lastOutput = 0
        running = True
        while running:
            running = False
            for n in range(5):
                if computers[n].halted:
                    continue
                x = n - 1 if n > 0 else 4
                input_val = computers[x].lastOutput
                computers[n].run(input_val)
                if not computers[n].halted:
                    running = True
            if not computers[4].halted:
                current_output = computers[4].lastOutput
                if current_output > max_amp:
                    max_amp = current_output
    return max_amp

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data_line = f.read().splitlines()[0]
    data = list(map(int, data_line.split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")


### Explanation
1. **Intcode Computer**:
   - The `runComputer1` function processes the Intcode program for part 1, running each amplifier to completion and returning the last output.
   - The `runComputer2` function processes the Intcode program for part 2, pausing after each output to allow feedback between amplifiers.
   - The `Computer` class manages the state of each amplifier in part 2, including its instruction pointer, phase setting, and last output.

2. **Part 1**:
   - Iterates over all permutations of phase settings (0-4), runs each amplifier in sequence, and tracks the maximum output signal.

3. **Part 2**:
   - Iterates over all permutations of phase settings (5-9), initializes each amplifier as a `Computer` instance, and runs them in a feedback loop.
   - The loop continues until all amplifiers halt, passing the output of the last amplifier to the first in each iteration.
   - The maximum output from the last amplifier during these iterations is recorded.

4. **Efficiency**:
   - By avoiding storage of all intermediate results and optimizing the Intcode interpreter, the solution reduces memory usage and improves runtime performance.
   - The use of local variables and direct address handling in opcode 3 streamlines the interpreter's execution.