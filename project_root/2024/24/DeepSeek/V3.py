import sys


def part1(lines):
    first_data = []
    second_data = []
    switch = False
    for line in lines:
        if line == "\n":
            switch = True
            continue
        if not switch:
            first_data.append(line.strip())
        else:
            second_data.append(line.strip())

    first_clean = {}
    second_clean = {}
    for first in first_data:
        left, right = first.split(":")
        first_clean[left] = int(right)
    for second in second_data:
        parts = second.split()
        second_clean[parts[-1]] = (parts[0], parts[2], parts[1])

    wire_values = first_clean.copy()
    stack = []

    def operate(data3):
        stack.append(data3)
        while stack:
            current = stack[-1]
            if current in wire_values:
                stack.pop()
                continue
            data1, data2, operator = second_clean[current]
            if data1 not in wire_values:
                stack.append(data1)
                continue
            if data2 not in wire_values:
                stack.append(data2)
                continue
            if operator == "AND":
                wire_values[current] = wire_values[data1] & wire_values[data2]
            elif operator == "OR":
                wire_values[current] = wire_values[data1] | wire_values[data2]
            elif operator == "XOR":
                wire_values[current] = wire_values[data1] ^ wire_values[data2]
            stack.pop()

    for wire in second_clean:
        operate(wire)

    z_wires = sorted([key for key in wire_values if key.startswith("z")], reverse=True)
    binary_result = "".join(str(wire_values[z]) for z in z_wires)
    decimal_result = int(binary_result, 2)

    return decimal_result


def part2(lines):
    formulas = {}
    for line in lines:
        if "->" in line:
            parts = line.strip().split()
            formulas[parts[-1]] = (parts[0], parts[2], parts[1])

    def make_wire(prefix, num):
        return f"{prefix}{num:02d}"

    def verify_z(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op != "XOR":
            return False
        if num == 0:
            return sorted([x, y]) == ["x00", "y00"]
        return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or (
            verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
        )

    def verify_intermediate_xor(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op != "XOR":
            return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_carry_bit(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if num == 1:
            return op == "AND" and sorted([x, y]) == ["x00", "y00"]
        if op != "OR":
            return False
        return (verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1)) or (
            verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)
        )

    def verify_direct_carry(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op != "AND":
            return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_recarry(wire, num):
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op != "AND":
            return False
        return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or (
            verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
        )

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
        for x in list(formulas.keys()):
            for y in list(formulas.keys()):
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

    return ",".join(sorted(swaps))


with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))