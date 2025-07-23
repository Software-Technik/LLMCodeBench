import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

def line_transform(line):
    return line.split(" ")

if lines:
    lines = [line_transform(line) for line in lines]

acc = 0
idx = 0
visited = set()
while True:
    cur = lines[idx]
    ins, val = cur
    visited.add(idx)
    if ins == "acc":
        acc += int(val)
        idx += 1
    elif ins == "nop":
        idx += 1
    elif ins == "jmp":
        idx += int(val)
    if idx in visited:
        break
result1 = acc

def run_program(program):
    acc = 0
    idx = 0
    visited = set()
    n = len(program)
    while idx < n:
        if idx in visited:
            return (False, None)
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

result2 = None
for i in range(len(lines)):
    if lines[i][0] == "nop":
        modified = [line[:] for line in lines]
        modified[i] = ["jmp", lines[i][1]]
        success, acc_val = run_program(modified)
        if success:
            result2 = acc_val
            break
    elif lines[i][0] == "jmp":
        modified = [line[:] for line in lines]
        modified[i] = ["nop", lines[i][1]]
        success, acc_val = run_program(modified)
        if success:
            result2 = acc_val
            break

print(result1, result2)