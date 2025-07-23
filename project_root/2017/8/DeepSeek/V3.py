import sys
from collections import defaultdict

def parse_instruction(line):
    parts = line.split()
    return (parts[0], parts[1], int(parts[2]), parts[4], parts[5], int(parts[6]))

def is_condition_satisfied(op, reg_val, value):
    if op == "<": return reg_val < value
    if op == ">": return reg_val > value
    if op == "<=": return reg_val <= value
    if op == ">=": return reg_val >= value
    if op == "==": return reg_val == value
    if op == "!=": return reg_val != value

with open(sys.argv[1]) as f:
    instructions = [parse_instruction(line.strip()) for line in f if line.strip()]

registers = defaultdict(int)
maximum_ever = float('-inf')

for reg, instr, amount, condReg, condOp, value in instructions:
    reg_val = registers[condReg]
    if is_condition_satisfied(condOp, reg_val, value):
        if instr == "inc":
            registers[reg] += amount
        elif instr == "dec":
            registers[reg] -= amount
        current = registers[reg]
        if current > maximum_ever:
            maximum_ever = current

print(max(registers.values()))
print(maximum_ever)