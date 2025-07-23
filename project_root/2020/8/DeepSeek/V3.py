import sys
import copy

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

lines = [line.split() for line in lines]

def run_program(program):
    acc = 0
    idx = 0
    visited = set()
    n = len(program)
    while idx < n:
        if idx in visited:
            return (False, acc)
        visited.add(idx)
        ins, val = program[idx]
        if ins == "acc":
            acc += int(val)
            idx += 1
        elif ins == "nop":
            idx += 1
        elif ins == "jmp":
            idx += int(val)
    return (True, acc)

result1 = run_program(lines)[1]

for i, line in enumerate(lines):
    if line[0] not in ("nop", "jmp"):
        continue
    newlines = copy.deepcopy(lines)
    if line[0] == "nop":
        newlines[i][0] = "jmp"
    else:
        newlines[i][0] = "nop"
    success, acc = run_program(newlines)
    if success:
        result2 = acc
        break

print(result1, result2)