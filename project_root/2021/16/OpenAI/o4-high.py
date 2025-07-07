import sys

with open(sys.argv[1]) as f:
    data = f.read().strip()
bits = bin(int(data, 16))[2:].zfill(len(data) * 4)

def parse(i, end):
    version = int(bits[i:i+3], 2); type_id = int(bits[i+3:i+6], 2); i += 6; vsum = version
    if type_id == 4:
        val = 0
        while True:
            group = bits[i:i+5]; val = (val << 4) + int(group[1:], 2); i += 5
            if group[0] == '0': break
        return i, vsum, val
    lt = bits[i]; i += 1; values = []
    if lt == '0':
        total_length = int(bits[i:i+15], 2); i += 15; end_sub = i + total_length
        while i < end_sub:
            i, sv, v = parse(i, end_sub); vsum += sv; values.append(v)
    else:
        count = int(bits[i:i+11], 2); i += 11
        for _ in range(count):
            i, sv, v = parse(i, end); vsum += sv; values.append(v)
    if type_id == 0:
        res = sum(values)
    elif type_id == 1:
        p = 1
        for x in values: p *= x
        res = p
    elif type_id == 2:
        res = min(values)
    elif type_id == 3:
        res = max(values)
    elif type_id == 5:
        res = 1 if values[0] > values[1] else 0
    elif type_id == 6:
        res = 1 if values[0] < values[1] else 0
    else:
        res = 1 if values[0] == values[1] else 0
    return i, vsum, res

_, part1, part2 = parse(0, len(bits))
sys.stdout.write(f"{part1} {part2}")