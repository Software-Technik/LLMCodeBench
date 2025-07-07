import sys
import math

def parse(bits, pos):
    version = int(bits[pos:pos+3], 2); pos += 3
    type_id = int(bits[pos:pos+3], 2); pos += 3
    if type_id == 4:
        literal = 0
        while True:
            group = bits[pos:pos+5]; pos += 5
            literal = (literal << 4) | int(group[1:], 2)
            if group[0] == '0':
                break
        return version, literal, pos
    length_type_id = bits[pos]; pos += 1
    vals = []
    ver_sum = 0
    if length_type_id == '0':
        total_length = int(bits[pos:pos+15], 2); pos += 15
        end = pos + total_length
        while pos < end:
            v, val, new_pos = parse(bits, pos)
            ver_sum += v; vals.append(val); pos = new_pos
    else:
        count = int(bits[pos:pos+11], 2); pos += 11
        for _ in range(count):
            v, val, new_pos = parse(bits, pos)
            ver_sum += v; vals.append(val); pos = new_pos
    if type_id == 0:
        result = sum(vals)
    elif type_id == 1:
        result = math.prod(vals)
    elif type_id == 2:
        result = min(vals)
    elif type_id == 3:
        result = max(vals)
    elif type_id == 5:
        result = int(vals[0] > vals[1])
    elif type_id == 6:
        result = int(vals[0] < vals[1])
    elif type_id == 7:
        result = int(vals[0] == vals[1])
    else:
        result = 0
    return version + ver_sum, result, pos

def main():
    data = open(sys.argv[1]).read().strip()
    bits = bin(int(data, 16))[2:].zfill(len(data)*4)
    v_sum, value, _ = parse(bits, 0)
    sys.stdout.write(f"{v_sum} {value}")

if __name__ == "__main__":
    main()