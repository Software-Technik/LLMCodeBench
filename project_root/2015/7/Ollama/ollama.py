import sys

def eval_signal(parts, wires):
    if parts[0].isdigit():
        val = int(parts[0])
    else:
        val = wires[parts[0]]

    op = parts[1]
    if len(parts) == 2 and op == "NOT":
        return ~val & 0xFFFF

    right = parts[2]
    if right.isdigit():
        rval = int(right)
    else:
        rval = wires[right]

    if op == "AND":
        return val & rval
    elif op == "OR":
        return val | rval
    elif op == "LSHIFT":
        return val << rval
    elif op == "RSHIFT":
        return val >> rval

def main(data):
    wires = {}
    insts = [i.split(" -> ") for i in data]

    while insts:
        done = []

        for inst in list(insts):
            src, dst = inst
            parts = src.split()
            if len(parts) == 1 and (parts[0].isdigit() or parts[0] in wires):
                val = int(parts[0]) if parts[0].isdigit() else wires[parts[0]]
            elif len(parts) == 2 and parts[0] == "NOT" and parts[1] in wires:
                val = ~wires[parts[1]] & 0xFFFF
            elif len(parts) == 3:
                if (parts[0].isdigit() or parts[0] in wires) and \
                   ((parts[2].isdigit()) or parts[2] in wires):
                    val = eval_signal(parts, wires)
            else:
                continue

            wires[dst] = val
            done.append(inst)

        for inst in done:
            insts.remove(inst)

    return wires["a"]

def secondary(data):
    initial_a = main(data)
    modified_data = [i for i in data if " b" not in i]
    modified_data += [f"{initial_a} -> b"]
    return main(modified_data)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

output = f"{main(data)}\n{secondary(data)}\n"
sys.stdout.write(output)