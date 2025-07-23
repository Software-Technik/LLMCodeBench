import sys
import functools

def part1(lines):
    data = "".join(lines).split("\n\n")
    first_data = [line.strip() for line in data[0].splitlines()]
    second_data = [line.strip() for line in data[1].splitlines()] if len(data) > 1 else []
    
    first_clean = {left: int(right) for left, right in (item.split(':') for item in first_data)}
    second_clean = {}
    for second in second_data:
        parts = second.split()
        second_clean[parts[4]] = (parts[0], parts[2], parts[1])
    
    def operate(data3, wire_values, gates):
        if data3 in wire_values:
            return wire_values[data3]
        
        data1, data2, operator = gates[data3]
        
        if data1 not in wire_values:
            wire_values[data1] = operate(data1, wire_values, gates)
        if data2 not in wire_values:
            wire_values[data2] = operate(data2, wire_values, gates)
        
        if operator == "AND":
            wire_values[data3] = wire_values[data1] & wire_values[data2]
        elif operator == "OR":
            wire_values[data3] = wire_values[data1] | wire_values[data2]
        elif operator == "XOR":
            wire_values[data3] = wire_values[data1] ^ wire_values[data2]
        
        return wire_values[data3]
    
    wire_values = first_clean.copy()
    
    for wire in second_clean:
        operate(wire, wire_values, second_clean)
    
    z_wires = sorted([key for key in wire_values if key.startswith("z")], reverse=True)
    binary_result = "".join(str(wire_values[z]) for z in z_wires)
    decimal_result = int(binary_result, 2)
    
    return decimal_result

def part2(lines):
    formulas = {}
    for line in lines:
        stripped = line.strip()
        if "->" in stripped:
            parts = stripped.split()
            if len(parts) == 5:
                formulas[parts[4]] = (parts[0], parts[2], parts[1])
    
    def make_wire(prefix, num):
        return f"{prefix}{str(num).zfill(2)}"
    
    def verify_z(wire, num, cache):
        key = ('z', wire, num)
        if key in cache:
            return cache[key]
        if wire not in formulas:
            cache[key] = False
            return False
        x, y, op = formulas[wire]
        if op != "XOR":
            cache[key] = False
            return False
        if num == 0:
            res = sorted([x, y]) == ["x00", "y00"]
            cache[key] = res
            return res
        res = (verify_intermediate_xor(x, num, cache) and verify_carry_bit(y, num, cache)) or (verify_intermediate_xor(y, num, cache) and verify_carry_bit(x, num, cache))
        cache[key] = res
        return res
    
    def verify_intermediate_xor(wire, num, cache):
        key = ('ix', wire, num)
        if key in cache:
            return cache[key]
        if wire not in formulas:
            cache[key] = False
            return False
        x, y, op = formulas[wire]
        if op != "XOR":
            cache[key] = False
            return False
        res = sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]
        cache[key] = res
        return res
    
    def verify_carry_bit(wire, num, cache):
        key = ('cb', wire, num)
        if key in cache:
            return cache[key]
        if wire not in formulas:
            cache[key] = False
            return False
        x, y, op = formulas[wire]
        if num == 1:
            res = op == "AND" and sorted([x, y]) == ["x00", "y00"]
            cache[key] = res
            return res
        if op != "OR":
            cache[key] = False
            return False
        res = (verify_direct_carry(x, num-1, cache) and verify_recarry(y, num-1, cache)) or (verify_direct_carry(y, num-1, cache) and verify_recarry(x, num-1, cache))
        cache[key] = res
        return res
    
    def verify_direct_carry(wire, num, cache):
        key = ('dc', wire, num)
        if key in cache:
            return cache[key]
        if wire not in formulas:
            cache[key] = False
            return False
        x, y, op = formulas[wire]
        if op != "AND":
            cache[key] = False
            return False
        res = sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]
        cache[key] = res
        return res
    
    def verify_recarry(wire, num, cache):
        key = ('rc', wire, num)
        if key in cache:
            return cache[key]
        if wire not in formulas:
            cache[key] = False
            return False
        x, y, op = formulas[wire]
        if op != "AND":
            cache[key] = False
            return False
        res = (verify_intermediate_xor(x, num, cache) and verify_carry_bit(y, num, cache)) or (verify_intermediate_xor(y, num, cache) and verify_carry_bit(x, num, cache))
        cache[key] = res
        return res
    
    def verify(num, cache):
        key = ('v', num)
        if key in cache:
            return cache[key]
        res = verify_z(make_wire("z", num), num, cache)
        cache[key] = res
        return res
    
    def progress():
        cache = {}
        i = 0
        while i < 16 and verify(i, cache):
            i += 1
        return i
    
    swaps = []
    for _ in range(4):
        baseline = progress()
        found = False
        for x in formulas:
            for y in formulas:
                if x == y:
                    continue
                formulas[x], formulas[y] = formulas[y], formulas[x]
                new_progress = progress()
                if new_progress > baseline:
                    swaps.append(x)
                    swaps.append(y)
                    found = True
                    break
                formulas[x], formulas[y] = formulas[y], formulas[x]
            if found:
                break
    
    return ",".join(sorted(swaps))

input_path = sys.argv[1]
with open(input_path, "r") as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))