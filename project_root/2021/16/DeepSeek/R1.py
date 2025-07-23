import sys
from dataclasses import dataclass
from numpy import prod


@dataclass
class Packet:
    version: int
    type_id: int
    literal: int
    sub_packets: list


def parse_packet(bits, start_index):
    version = int(bits[start_index:start_index+3], 2)
    type_id = int(bits[start_index+3:start_index+6], 2)
    pos = start_index + 6

    if type_id == 4:
        literal = 0
        while True:
            group = bits[pos:pos+5]
            literal = (literal << 4) | int(group[1:5], 2)
            pos += 5
            if group[0] == '0':
                break
        return Packet(version, type_id, literal, []), pos

    sub_packets = []
    length_type_id = bits[pos]
    pos += 1
    if length_type_id == '0':
        total_length = int(bits[pos:pos+15], 2)
        pos += 15
        end_pos = pos + total_length
        while pos < end_pos:
            sub, pos = parse_packet(bits, pos)
            sub_packets.append(sub)
    else:
        num_sub = int(bits[pos:pos+11], 2)
        pos += 11
        for _ in range(num_sub):
            sub, pos = parse_packet(bits, pos)
            sub_packets.append(sub)
    return Packet(version, type_id, 0, sub_packets), pos


def add_versions(root):
    stack = [root]
    total = 0
    while stack:
        p = stack.pop()
        total += p.version
        stack.extend(p.sub_packets)
    return total


def compute(p):
    if p.type_id == 4:
        return p.literal
    values = [compute(x) for x in p.sub_packets]
    if p.type_id == 0:
        return sum(values)
    elif p.type_id == 1:
        return prod(values)
    elif p.type_id == 2:
        return min(values)
    elif p.type_id == 3:
        return max(values)
    elif p.type_id == 5:
        return int(values[0] > values[1])
    elif p.type_id == 6:
        return int(values[0] < values[1])
    elif p.type_id == 7:
        return int(values[0] == values[1])
    raise ValueError(f"Unknown type_id {p.type_id}")


def part1(data):
    bits = bin(int(data, 16))[2:]
    bits = bits.zfill(len(data) * 4)
    packet, _ = parse_packet(bits, 0)
    return add_versions(packet)

def part2(data):
    bits = bin(int(data, 16))[2:]
    bits = bits.zfill(len(data) * 4)
    packet, _ = parse_packet(bits, 0)
    return compute(packet)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")