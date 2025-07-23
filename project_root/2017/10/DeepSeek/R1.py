import sys

def knot_logic(lengths, iterations=64):
    size = 256
    nums = list(range(size))
    pos = skip = 0
    mask = size - 1

    for _ in range(iterations):
        for length in lengths:
            for i in range(length // 2):
                left = (pos + i) & mask
                right = (pos + length - 1 - i) & mask
                nums[left], nums[right] = nums[right], nums[left]
            pos = (pos + length + skip) & mask
            skip += 1
            
    return nums

def knot_hash(input_str, bin_out=False):
    lengths = [ord(c) for c in input_str.strip()] + [17, 31, 73, 47, 23]
    sparse_hash = knot_logic(lengths, 64)
    
    dense_hash = []
    for i in range(0, 256, 16):
        xor = 0
        for j in range(16):
            xor ^= sparse_hash[i+j]
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