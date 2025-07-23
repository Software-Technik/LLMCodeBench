import sys

def part1(data):
    insts = [i.split(" -> ") for i in data]
    wires = {}

    while insts:
        done = []
        for i in insts:
            parts = i[0].split()
            matched = False
            if len(parts) == 1:
                if parts[0].isdigit():
                    wires[i[1]] = int(parts[0])
                    matched = True
                elif parts[0] in wires:
                    wires[i[1]] = wires[parts[0]]
                    matched = True
            elif len(parts) == 2 and parts[0] == "NOT" and parts[1] in wires:
                wires[i[1]] = (~wires[parts[1]]) & 0xFFFF
                matched = True
            elif len(parts) == 3:
                a = int(parts[0]) if parts[0].isdigit() else wires.get(parts[0], None)
                b = int(parts[2]) if parts[2].isdigit() else wires.get(parts[2], None)
                if a is not None and b is not None:
                    if parts[1] == "AND":
                        wires[i[1]] = a & b
                        matched = True
                    elif parts[1] == "OR":
                        wires[i[1]] = a | b
                        matched = True
                    elif parts[1] == "LSHIFT":
                        wires[i[1]] = (a << b) & 0xFFFF
                        matched = True
                    elif parts[1] == "RSHIFT":
                        wires[i[1]] = a >> b
                        matched = True
            if matched:
                done.append(i)
        insts = [i for i in insts if i not in done]
    return wires["a"]

def part2(data):
    new_b = part1(data)
    new_data = [i for i in data if not i.endswith("-> b")]
    new_data.append(f"{new_b} -> b")
    return part1(new_data)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n{part2(data)}")