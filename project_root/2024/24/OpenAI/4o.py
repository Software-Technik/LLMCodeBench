import sys

def part1(lines):
    first_clean = {}
    second_clean = {}
    switch = False
    for line in lines:
        if line == "\n":
            switch = True
            continue
        if not switch:
            left, right = line.strip().split(":")
            first_clean[left] = int(right)
        else:
            data1, operator, data2, _, data3 = line.strip().split(" ")
            second_clean[data3] = (data1, data2, operator)

    def operate(data3):
        if data3 in wire_values:
            return wire_values[data3]

        data1, data2, operator = second_clean[data3]
        wire_values[data1] = wire_values.get(data1, operate(data1))
        wire_values[data2] = wire_values.get(data2, operate(data2))

        if operator == "AND":
            wire_values[data3] = wire_values[data1] & wire_values[data2]
        elif operator == "OR":
            wire_values[data3] = wire_values[data1] | wire_values[data2]
        elif operator == "XOR":
            wire_values[data3] = wire_values[data1] ^ wire_values[data2]

        return wire_values[data3]

    wire_values = first_clean.copy()

    for wire in second_clean.keys():
        operate(wire)

    z_wires = sorted(wire for wire in wire_values if wire.startswith("z"))
    binary_result = "".join(str(wire_values[z]) for z in reversed(z_wires))
    return int(binary_result, 2)

def part2(lines):
    formulas = {}
    for line in lines:
        if "->" in line:
            data1, operator, data2, _, data3 = line.strip().split()
            formulas[data3] = (data1, data2, operator)

    def make_wire(prefix, num):
        return f"{prefix}{str(num).zfill(2)}"

    def verify_z(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op == "XOR":
            if num == 0:
                return sorted([x, y]) == ["x00", "y00"]
            return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or (
                verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
            )
        return False

    def verify_intermediate_xor(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        return op == "XOR" and sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_carry_bit(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if num == 1:
            return op == "AND" and sorted([x, y]) == ["x00", "y00"]
        if op == "OR":
            return (verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1)) or (
                verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)
            )
        return False

    def verify_direct_carry(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        return op == "AND" and sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_recarry(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op == "AND":
            return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or (
                verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
            )
        return False

    def verify(num):
        return verify_z(make_wire("z", num), num)

    def progress():
        i = 0
        while verify(i):
            i += 1
        return i

    swaps = []
    for _ in range(4):
        baseline = progress()
        for x in formulas:
            for y in formulas:
                if x == y:
                    continue
                formulas[x], formulas[y] = formulas[y], formulas[x]
                if progress() > baseline:
                    swaps.append(x)
                    swaps.append(y)
                    break
                formulas[x], formulas[y] = formulas[y], formulas[x]
            else:
                continue
            break

    return ",".join(sorted(set(swaps)))

input_path = sys.argv[1]

with open(input_path, "r") as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))