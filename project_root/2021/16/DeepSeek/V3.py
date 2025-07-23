import sys
from dataclasses import dataclass


@dataclass
class Packet:
    version: int
    type_id: int
    literal: int
    length: int
    sub_packets: list


def parse_packet(bits, depth=0):
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    pos = 6

    if type_id == 4:
        literal = 0
        while True:
            group = bits[pos:pos+5]
            literal = (literal << 4) | int(group[1:], 2)
            pos += 5
            if group[0] == '0':
                break
        return Packet(version, type_id, literal, pos, [])

    length_type_id = bits[pos]
    pos += 1
    sub_packets = []

    if length_type_id == '0':
        total_length = int(bits[pos:pos+15], 2)
        pos += 15
        end_pos = pos + total_length
        while pos < end_pos:
            sub = parse_packet(bits[pos:end_pos], depth + 1)
            sub_packets.append(sub)
            pos += sub.length
    else:
        number = int(bits[pos:pos+11], 2)
        pos += 11
        for _ in range(number):
            sub = parse_packet(bits[pos:], depth + 1)
            sub_packets.append(sub)
            pos += sub.length

    return Packet(version, type_id, 0, pos, sub_packets)


def add_versions(packet):
    total = packet.version
    for sub in packet.sub_packets:
        total += add_versions(sub)
    return total


def compute(p):
    if p.type_id == 4:
        return p.literal
    values = [compute(sub) for sub in p.sub_packets]
    if p.type_id == 0:
        return sum(values)
    elif p.type_id == 1:
        res = 1
        for v in values:
            res *= v
        return res
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
    bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
    packet = parse_packet(bits)
    return add_versions(packet)


def part2(data):
    bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
    packet = parse_packet(bits)
    return compute(packet)


with open(sys.argv[1]) as f:
    data = f.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")