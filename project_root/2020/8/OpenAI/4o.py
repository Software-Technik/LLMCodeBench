import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines = []

lines = [line.split() for line in lines]

acc = 0
idx = 0
visited = set()

while idx not in visited:
    visited.add(idx)
    ins, val = lines[idx]
    if ins == "acc":
        acc += int(val)
        idx += 1
    elif ins == "nop":
        idx += 1
    elif ins == "jmp":
        idx += int(val)

result1 = acc

def try_chg(lines):
    acc = 0
    idx = 0
    visited = set()
    while idx not in visited and idx < len(lines):
        visited.add(idx)
        ins, val = lines[idx]
        if ins == "acc":
            acc += int(val)
            idx += 1
        elif ins == "nop":
            idx += 1
        elif ins == "jmp":
            idx += int(val)
    return acc if idx == len(lines) else False

for i, line in enumerate(lines):
    original_ins = lines[i][0]
    if original_ins == "nop":
        lines[i][0] = "jmp"
    elif original_ins == "jmp":
        lines[i][0] = "nop"
    result2 = try_chg(lines)
    if result2:
        break
    lines[i][0] = original_ins

print(result1, result2)