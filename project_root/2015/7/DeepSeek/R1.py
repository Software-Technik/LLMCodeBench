import sys

def solve(data):
    instructions = []
    for line in data:
        parts = line.split(" -> ")
        if len(parts) < 2:
            continue
        output = parts[1].strip()
        left = parts[0].split()
        if len(left) == 1:
            token = left[0]
            if token.isdigit():
                instructions.append((output, 'ASSIGN', [int(token)]))
            else:
                instructions.append((output, 'ASSIGN', [token]))
        elif len(left) == 2 and left[0] == 'NOT':
            token = left[1]
            if token.isdigit():
                instructions.append((output, 'NOT', [int(token)]))
            else:
                instructions.append((output, 'NOT', [token]))
        elif len(left) == 3:
            op = left[1]
            inputs = []
            for a in [left[0], left[2]]:
                if a.isdigit():
                    inputs.append(int(a))
                else:
                    inputs.append(a)
            instructions.append((output, op, inputs))
        else:
            continue

    n = len(instructions)
    dep_count = [0] * n
    dependencies = {}

    for idx, (output, op, inputs) in enumerate(instructions):
        count = 0
        for arg in inputs:
            if type(arg) is str:
                count += 1
                if arg not in dependencies:
                    dependencies[arg] = []
                dependencies[arg].append(idx)
        dep_count[idx] = count

    queue = [idx for idx in range(n) if dep_count[idx] == 0]
    wire_values = {}

    while queue:
        idx = queue.pop(0)
        output, op, inputs = instructions[idx]
        resolved = []
        for arg in inputs:
            if type(arg) is str:
                resolved.append(wire_values[arg])
            else:
                resolved.append(arg)

        if op == 'ASSIGN':
            value = resolved[0]
        elif op == 'NOT':
            value = ~resolved[0]
        elif op == 'AND':
            value = resolved[0] & resolved[1]
        elif op == 'OR':
            value = resolved[0] | resolved[1]
        elif op == 'LSHIFT':
            value = resolved[0] << resolved[1]
        elif op == 'RSHIFT':
            value = resolved[0] >> resolved[1]
        else:
            value = 0

        value &= 0xFFFF
        wire_values[output] = value

        if output in dependencies:
            for dep_idx in dependencies[output]:
                dep_count[dep_idx] -= 1
                if dep_count[dep_idx] == 0:
                    queue.append(dep_idx)

    return wire_values['a']

def part1(data):
    return solve(data)

def part2(data):
    a_val = solve(data)
    new_data = [line for line in data if line[-2:] != " b"]
    new_data.append(f"{a_val} -> b")
    return solve(new_data)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")