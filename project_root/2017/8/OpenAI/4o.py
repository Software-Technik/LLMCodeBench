import sys

def parse_instruction(line):
    parts = line.split()
    return (
        parts[0],                  # reg
        parts[1],                  # instr
        int(parts[2]),             # amount
        parts[4],                  # condReg
        parts[5],                  # condOp
        int(parts[6])              # value
    )

def is_condition_satisfied(op, reg_val, value):
    if op == '<': return reg_val < value
    if op == '>': return reg_val > value
    if op == '<=': return reg_val <= value
    if op == '>=': return reg_val >= value
    if op == '==': return reg_val == value
    if op == '!=': return reg_val != value

input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [parse_instruction(line.strip()) for line in f if line.strip()]

registers = {}
maximum_ever = float('-inf')

for reg, instr, amount, condReg, condOp, value in instructions:
    reg_val = registers.get(condReg, 0)
    if is_condition_satisfied(condOp, reg_val, value):
        if instr == "inc":
            registers[reg] = registers.get(reg, 0) + amount
        elif instr == "dec":
            registers[reg] = registers.get(reg, 0) - amount
        
        maximum_ever = max(maximum_ever, registers[reg])

print(max(registers.values(), default=0))
print(maximum_ever)