import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = [line.split() for line in f.read().splitlines()]
except Exception:
    lines = []

acc = 0
idx = 0
visited = set()
while idx not in visited and idx < len(lines):
    cur = lines[idx]
    visited.add(idx)
    ins, val = cur
    if ins == "acc":
        acc += int(val)
        idx += 1
    elif ins == "nop":
        idx += 1
    else:
        idx += int(val)

result1 = acc

def try_chg(index):
    global acc, idx, visited
    acc, idx, visited = 0, 0, set()
    while idx not in visited and idx < len(lines):
        cur = lines[idx]
        if index == idx:
            ins, val = cur[0] + "mp", cur[1] if cur[0] == "jmp" else cur[1]
        else:
            ins, val = cur
        visited.add(idx)
        if ins == "acc":
            acc += int(val)
            idx += 1
        elif ins == "nop":
            idx += 1
        else:
            idx += int(val)
    return False if idx in visited else acc

for i in range(len(lines)):
    result2 = try_chg(i)
    if result2 != False:
        break

print(result1, result2)