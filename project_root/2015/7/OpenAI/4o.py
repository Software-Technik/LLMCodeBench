import sys
from collections import deque

def evaluate_instruction(inst, wires):
    parts = inst[0].split(" ")
    if len(parts) == 1:
        return int(parts[0]) if parts[0].isdigit() else wires.get(parts[0])
    elif len(parts) == 2 and parts[0] == "NOT":
        return (~wires[parts[1]]) & 0xFFFF if parts[1] in wires else None
    elif len(parts) == 3:
        op1 = int(parts[0]) if parts[0].isdigit() else wires.get(parts[0])
        op2 = int(parts[2]) if parts[2].isdigit() else wires.get(parts[2])
        if parts[1] == "AND":
            return op1 & op2 if op1 is not None and op2 is not None else None
        elif parts[1] == "OR":
            return op1 | op2 if op1 is not None and op2 is not None else None
        elif parts[1] == "LSHIFT":
            return op1 << op2 if op1 is not None else None
        elif parts[1] == "RSHIFT":
            return op1 >> op2 if op1 is not None else None
    return None

def compute_wires(data, override=None):
    insts = [i.split(" -> ") for i in data]
    wires = {}
    if override:
        wires.update(override)
    queue = deque(insts)
    
    while queue:
        inst = queue.popleft()
        result = evaluate_instruction(inst, wires)
        if result is not None:
            wires[inst[1]] = result
        else:
            queue.append(inst)
    
    return wires

def part1(data):
    return compute_wires(data)["a"]

def part2(data):
    value_a = part1(data)
    return compute_wires(data, override={'b': value_a})["a"]

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n{part2(data)}")