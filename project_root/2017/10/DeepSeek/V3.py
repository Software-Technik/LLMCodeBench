import sys
from functools import reduce

def knot_logic(lengths, iterations=64):
    size = 256
    nums = bytearray(range(size))
    pos = skip = 0

    for _ in range(iterations):
        for length in lengths:
            if length > size:
                continue
            end = pos + length
            if end <= size:
                nums[pos:end] = reversed(nums[pos:end])
            else:
                wrapped = end % size
                section = nums[pos:] + nums[:wrapped]
                section = bytearray(reversed(section))
                nums[pos:] = section[:size - pos]
                nums[:wrapped] = section[size - pos:]
            pos = (pos + length + skip) % size
            skip += 1

    return nums

def knot_hash(input_str, bin_out=False):
    lengths = [ord(c) for c in input_str.strip()] + [17, 31, 73, 47, 23]
    sparse_hash = knot_logic(lengths, 64)
    
    dense_hash = []
    for i in range(0, 256, 16):
        xor = reduce(lambda x, y: x ^ y, sparse_hash[i:i+16])
        dense_hash.append(format(xor, '08b' if bin_out else '02x'))

    return ''.join(dense_hash)

input_strings = sys.argv[1]
with open(input_strings) as f:
    content = f.read().strip()

lengths = list(map(int, content.split(',')))
result1 = knot_logic(lengths, 1)
part1 = result1[0] * result1[1]

part2 = knot_hash(content).lower()

print(part1)
print(part2)