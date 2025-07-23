import sys

def get_wires_data(lines):
    signal_values = {}
    gates = {}
    for line in lines:
        line = line.strip()
        if not line or '->' in line:
            continue
        parts = line.split(' ')
        wires_value = int(parts[-1])
        wire = parts[0]
        signal_values[wire] = get_wire_value(wires_value)
    for line in lines:
        line = line.strip()
        if not line or '->' not in line:
            continue
        data, *operation, target = line.split(' ')
        if len(operation) == 1:  # It's a single value assignment
            signal_values[target] = get_wire_value(data)
        else:
            op = operation[-2]
            source_a, source_b = operation[0], operation[2]
            gates[target] = (source_a, op, source_b)
    return signal_values, gates

def get_wire_value(src):
    if src.isdigit():
        return int(src)
    return src

# Function to evaluate all wires in order with memoization
def resolve_wires(target, current_wires, gates):
    if target not in gates:
        return
    for wire in current_wires:
        resolve_wires(wire[0], sorted(set(current_wires + [wire]), key=lambda x: int(x.split(' ')[1])), gates)

    if isinstance(source_a, str):
        source_a = resolve_wires(current_wires, gates, source_a)
        if isinstance(source_b, str):
            source_b = resolve_wires(current_wires, gates, source_b)

    return signal_values[target]

def part1(lines):
    signal_values, gates = get_wires_data(lines)
    z_wires = [key for key in gates.keys() if key.startswith('z')]
    binary_result = "".join(str(resolve_wires(z, sorted(signal_values.items()), gates))for z in z_wires[::-1])
    return int(binary_result, 2)

def part2(input_path):
    with open(input_path, "r") as file:
        lines = file.readlines()
    swaps = []
    for _ in range(4): # Four pairs of swaps
        baseline = progress(lines)
        for x in sorted(signal_values.keys()):
            for y in sorted(signal_values.keys(), reverse=True):
                if x == y:
                    continue
                lines[x], lines[y] = lines[y], lines[x]
                lines = swap(x, y, lines)
                if part1(lines) > baseline:
                    swaps.append(x)
                    swaps.append(y)
                    break
                lines[x], lines[y] = lines[y], lines[x]
            else:
                continue
            break
    return ",".join(sorted(swaps))

def progress(lines):
    # Progress calculation logic here
    pass

print(part1(lines), part2(input_path))