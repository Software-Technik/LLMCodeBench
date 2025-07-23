import sys

def parse_packet(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    pos = 6
    if type_id == 4:
        literal, last = 0, False
        while not last:
            last = bits[pos] == '0'
            literal = (literal << 4) | int(bits[pos+1:pos+5], 2)
            pos += 5
        return version, type_id, literal, pos

    length_type_id = bits[pos]
    pos += 1
    sub_packets = []
    if length_type_id == '0':
        total_length = int(bits[pos:pos+15], 2)
        pos += 15
        while (remaining := total_length) > 0:
            version, type_id, literal_or_sub_packet, length = parse_packet(bits[pos:pos+remaining])
            sub_packets.append((version, type_id, literal_or_sub_packet))
            remaining -= length
            pos += length

    else:
        number_of_sub_packets = int(bits[pos:pos+11], 2)
        pos += 11
        for _ in range(number_of_sub_packets):
            version, type_id, literal_or_sub_packet, length = parse_packet(bits[pos:])
            sub_packets.append((version, type_id, literal_or_sub_packet))
            pos += length

    return version, type_id, sub_packets, pos

def add_versions(packet):
    total = packet[0]
    for v, t, sub_pack, _ in packet[2]:
        if t == 4:
            total += v
        else:
            total += v + add_versions((v, t, sub_pack))
    return total

def compute(packet):
    version, type_id, literal_or_sub_packet = packet[:3]
    if type_id == 4:
        return literal_or_sub_packet
    values = [
        (lambda f: [1, lambda p: sum([compute(v) for v in p]), lambda p: prod([compute(v) for v in p]),
                     lambda p: min([compute(v) for v in p]), lambda p: max([compute(v) for v in p]),
                     lambda p: int(compute(p[0]) > compute(p[1])), lambda p: int(compute(p[0]) < compute(p[1])),
                     lambda p: int(compute(p[0]) == compute(p[1]))][type_id](literal_or_sub_packet))(p) for p in literal_or_sub_packet
    ]
    return (lambda f: [sum, prod, min, max, lambda v: 1 if v[0] > v[1] else 0,
                       lambda v: 1 if v[0] < v[1] else 0, lambda v: 1 if v[0] == v[1] else 0][type_id])(literal_or_sub_packet)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = bin(int(f.read(), 16))[2:].zfill(len(data)*4)
version_sum, computation_result = parse_packet(data)
sys.stdout.write(f"{add_versions((0, 0, [version_sum], len(data)))} {compute(computation_result)}")