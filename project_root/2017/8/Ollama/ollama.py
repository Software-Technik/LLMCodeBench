import sys
from collections import defaultdict

parse_instruction = lambda line: {
    "reg": line[0],
    "instr": line[1],
    "amount": int(line[2]),
    "condReg": line[4],
    "condOp": line[5],
    "value": int(line[6])
} if (line := line.strip().split()) and len(line) == 7 else None

is_condition_satisfied = lambda op, reg_val, value: ({
    "<": lambda x, y: x < y,
    ">": lambda x, y: x > y,
    "<=": lambda x, y: x <= y,
    ">=": lambda x, y: x >= y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y
}[op])(reg_val, value)

with open(sys.argv[1]) as f:
    instructions = [parse_instruction(line) for line in f if parse_instruction(line)]

registers = defaultdict(int)
maximum_ever = float('-inf')

for instr in instructions:
    reg_val = registers[instr["condReg"]]
    if is_condition_satisfied(instr["condOp"], reg_val, instr["value"]):
        new_val = registers[instr["reg"]] + (instr["amount"] if instr["instr"] == "inc" else -instr["amount"])
        maximum_ever = max(maximum_ever, new_val)
        registers[instr["reg"]] = new_val

print(max(registers.values()))
print(maximum_ever)