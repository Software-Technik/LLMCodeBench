import sys
import random


def part1(lines):
    # Parse the input
    first_data = []
    second_data = []
    switch = False
    for line in lines:
        if line == "\n":
            switch = True
            continue
        if switch == False:  # First data
            first_data.append(line.strip())
        else:
            second_data.append(line.strip())

    # Clean data
    first_clean = {}
    second_clean = {}
    for first in first_data:
        left, right = first.split(":")
        first_clean[left] = int(right)
    for second in second_data:
        data1, operator, data2, arrow, data3 = second.split(" ")
        second_clean[data3] = (data1, data2, operator)

    def operate(data3, wire_values, gates):
        # If value is already calculated, return it
        if data3 in wire_values:
            return wire_values[data3]

        data1, data2, operator = gates[data3]

        # Resolve inputs recursively
        if data1 not in wire_values:
            wire_values[data1] = operate(data1, wire_values, gates)
        if data2 not in wire_values:
            wire_values[data2] = operate(data2, wire_values, gates)

        # Apply the operator
        if operator == "AND":
            wire_values[data3] = wire_values[data1] & wire_values[data2]
        elif operator == "OR":
            wire_values[data3] = wire_values[data1] | wire_values[data2]
        elif operator == "XOR":
            wire_values[data3] = wire_values[data1] ^ wire_values[data2]

        return wire_values[data3]

    # Initialize wire values with first_clean
    wire_values = first_clean.copy()

    # Calculate values for all outputs
    for wire in second_clean.keys():
        operate(wire, wire_values, second_clean)

    # Extract and sort z wires
    z_wires = sorted([key for key in wire_values.keys() if key.startswith("z")])

    # Combine the binary results from all z_wires
    binary_result = "".join(str(wire_values[z]) for z in z_wires[::-1])
    decimal_result = int(binary_result, 2)

    # Output the sorted results for all wires and the final result
    sorted_results = sorted(wire_values.items())

    return decimal_result


def part2(lines):
    # Separate formulas
    formulas = {}
    for line in lines:
        if "->" in line:
            data1, operator, data2, arrow, data3 = line.strip().split()
            formulas[data3] = (data1, data2, operator)

    # Credit: HyperNeutrino
    # Helper functions
    def make_wire(prefix, num):
        """Create a wire name like x00, y03, z01."""
        return f"{prefix}{str(num).zfill(2)}"

    def verify_z(wire, num):
        """Verify if the final output wire z[num] produces the correct value."""
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
        """Check if a wire correctly computes an intermediate XOR value."""
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op != "XOR":
            return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_carry_bit(wire, num):
        """Check if a wire correctly computes a carry bit."""
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
        """Check if a wire computes a direct carry."""
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op != "AND":
            return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_recarry(wire, num):
        """Check if a wire correctly propagates a carry bit."""
        if wire not in formulas:
            return False
        x, y, op = formulas[wire]
        if op != "AND":
            return False
        return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or (
            verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
        )

    def verify(num):
        """Verify if the output for the nth bit is correct."""
        return verify_z(make_wire("z", num), num)

    def progress():
        """Find the maximum number of bits correctly computed by the system."""
        i = 0
        while verify(i):
            i += 1
        return i

    # Find the swaps
    swaps = []
    for _ in range(4):  # Four pairs of swaps
        baseline = progress()
        for x in formulas:
            for y in formulas:
                if x == y:
                    continue
                # Swap and test
                formulas[x], formulas[y] = formulas[y], formulas[x]
                if progress() > baseline:
                    swaps.append(x)
                    swaps.append(y)
                    break
                # Undo the swap if it didn't improve
                formulas[x], formulas[y] = formulas[y], formulas[x]
            else:
                continue
            break

    # Output sorted swaps
    return ",".join(sorted(swaps))


input_path = sys.argv[1]

with open(input_path, "r") as file:
    lines = file.readlines()

    print(part1(lines), part2(lines))
