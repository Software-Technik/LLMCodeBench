import sys
from collections import defaultdict

def parse_instruction(line):
    parts = line.split()
    return {
        "reg": parts[0],
        "instr": parts[1],
        "amount": int(parts[2]),
        "condReg": parts[4],
        "condOp": parts[5],
        "value": int(parts[6])
    }

def is_condition_satisfied(op, reg_val, value):
    return {
        "<": reg_val < value,
        ">": reg_val > value,
        "<=": reg_val <= value,
        ">=": reg_val >= value,
        "==": reg_val == value,
        "!=": reg_val != value
    }[op]

# Lecture du fichier depuis sys.argv
input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [line.strip() for line in f if line.strip()]

registers = defaultdict(int)
maximum_ever = float('-inf')

for line in instructions:
    instr = parse_instruction(line)
    reg_val = registers[instr["condReg"]]

    if is_condition_satisfied(instr["condOp"], reg_val, instr["value"]):
        if instr["instr"] == "inc":
            registers[instr["reg"]] += instr["amount"]
        elif instr["instr"] == "dec":
            registers[instr["reg"]] -= instr["amount"]

        maximum_ever = max(maximum_ever, registers[instr["reg"]])

# Partie 1 : plus grande valeur finale dans les registres
# Partie 2 : plus grande valeur jamais atteinte durant l'exécution
print(max(registers.values()))
print(maximum_ever)