import sys

class Packet:
    __slots__ = 'version', 'type_id', 'literal', 'length', 'sub_packets'
    
    def __init__(self, version, type_id, literal, length, sub_packets):
        self.version = version
        self.type_id = type_id
        self.literal = literal
        self.length = length
        self.sub_packets = sub_packets


def parse_packet(bits):
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    position = 6

    if type_id == 4:
        literal, is_last = 0, False
        while not is_last:
            is_last = bits[position] == "0"
            literal = (literal << 4) | int(bits[position + 1 : position + 5], 2)
            position += 5
        return Packet(version, type_id, literal, position, [])

    length_type_id = int(bits[position], 2)
    position += 1
    sub_packets = []
    if length_type_id == 0:
        total_length = int(bits[position : position + 15], 2)
        position += 15
        length = 0
        while length != total_length:
            sub = parse_packet(bits[position : position + total_length - length])
            sub_packets.append(sub)
            length += sub.length
            position += sub.length
    else:
        number = int(bits[position : position + 11], 2)
        position += 11
        for _ in range(number):
            sub = parse_packet(bits[position:])
            sub_packets.append(sub)
            position += sub.length
    return Packet(version, type_id, 0, position, sub_packets)


def add_versions(packet):
    return packet.version + sum(add_versions(sub) for sub in packet.sub_packets)


def compute(p):
    if p.type_id == 4:
        return p.literal
    values = [compute(x) for x in p.sub_packets]
    if p.type_id == 0:
        return sum(values)
    if p.type_id == 1:
        result = 1
        for v in values:
            result *= v
        return result
    if p.type_id == 2:
        return min(values)
    if p.type_id == 3:
        return max(values)
    if p.type_id == 5:
        return int(values[0] > values[1])
    if p.type_id == 6:
        return int(values[0] < values[1])
    if p.type_id == 7:
        return int(values[0] == values[1])
    raise ValueError(f"Unknown type_id {p.type_id}")


def part1(data):
    bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
    packets = parse_packet(bits)
    return add_versions(packets)

def part2(data):
    bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
    packets = parse_packet(bits)
    return compute(packets)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")