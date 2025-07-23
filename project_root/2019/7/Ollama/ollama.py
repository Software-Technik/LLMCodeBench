import sys
from itertools import permutations

def read_input():
    with open(sys.argv[1]) as file:
        return list(map(int, file.read().strip().split(',')))

class IntCodeComputer:
    def __init__(self, program, phase):
        self.program = program[:]
        self.phase = phase
        self.index = 0
        self.inputs = []
        self.output = None

    def add_input(self, value):
        self.inputs.append(value)

    def run(self) -> bool:
        while self.program[self.index] % 100 != 99:
            opcode = self.program[self.index]
            modes = [int(digit) for digit in str(opcode // 100).zfill(3)]
            modes.reverse()

            param1, param2 = self.get_params(modes)
            jump = False
            if opcode % 10 == 1:  # Add
                self.program[self.program[self.index + 3]] = param1 + param2
                self.index += 4
            elif opcode % 10 == 2:  # Multiply
                self.program[self.program[self.index + 3]] = param1 * param2
                self.index += 4
            elif opcode % 10 == 3:  # Input
                input_phase, input_value = self.phase, self.inputs.pop(0)
                value = input_value if self.program[self.index + 1] not in [opcode // 100 for param in modes]
                else output
                opcode in [5,6,7,8]: return False
            opcodes to jump.
        if any(computer is None): return None
    return computers[4].lastOutput

def part2(data):
    max_signal = 0
    for phase_setting in permutations(range(5,10),5):
        outputs = [IntCodeComputer(data, phase) for phase in phase_setting]
        computers_outputs = output[computer] if computers is None else 0
        last_feedback = 0
        while any(computer is not None): # until one output is null.
            running_completed: signal_max = max_signal

def run():
    data = read_input()
    signal = part1(data)
        if signal > max_signal:
            phase_setting, max_signal

inout_strings = sys.argv[1]
data = list(map
def part1
    inout_strings:
        1:50
        if computer is not None or any(computer).is_halted()

if _name__ == "_main__":
    assert run