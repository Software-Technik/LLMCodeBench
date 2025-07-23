import sys
from collections import defaultdict, namedtuple

Instruction = namedtuple('Instruction', ['reg', 'instr', 'amount', 'condReg', 'condOp', 'value'])

condition_ops = {
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '<=': lambda a, b: a <= b,
    '>=': lambda a, b: a >= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b
}

def parse_instruction(line):
    parts = line.split()
    return Instruction(parts[0], parts[1], int(parts[2]), parts[4], parts[5], int(parts[6]))

registers = defaultdict(int)
maximum_ever = float('-inf')

with open(sys.argv[1]) as f:
    for line in f:
        stripped = line.strip()
        if not stripped:
            continue
        instr = parse_instruction(stripped)
        cond_val = registers[instr.condReg]
        if condition_ops[instr.condOp](cond_val, instr.value):
            current_val = registers[instr.reg]
            if instr.instr == "inc":
                new_val = current_val + instr.amount
            else:
                new_val = current_val - instr.amount
            registers[instr.reg] = new_val
            if new_val > maximum_ever:
                maximum_ever = new_val

print(max(registers.values()) if registers else 0)
print(maximum_ever)