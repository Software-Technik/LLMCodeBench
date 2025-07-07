import sys
from functools import reduce

def knot_logic(lengths, iterations=64):
    size = 256
    nums = list(range(size))
    pos = skip = 0

    for _ in range(iterations):
        for length in lengths:
            if length > size:
                continue
            # Reverse the section
            end = (pos + length) % size
            if end > pos:
                nums[pos:end] = reversed(nums[pos:end])
            else:
                section = (nums[pos:] + nums[:end])
                section.reverse()
                nums[pos:], nums[:end] = section[:size-pos], section[size-pos:]
                
            pos = (pos + length + skip) % size
            skip += 1

    return nums

def knot_hash(input_str, bin_out=False):
    lengths = [ord(c) for c in input_str.strip()] + [17, 31, 73, 47, 23]
    sparse_hash = knot_logic(lengths, 64)
    
    dense_hash = []
    for i in range(0, 256, 16):
        xor = 0
        for num in sparse_hash[i:i+16]:
            xor ^= num
        dense_hash.append(format(xor, '08b' if bin_out else '02x'))

    return ''.join(dense_hash)

# Lecture du fichier d'entrée
input_strings = sys.argv[1]
with open(input_strings) as f:
    content = f.read().strip()

# Partie 1
lengths = list(map(int, content.split(',')))
result1 = knot_logic(lengths, 1)
part1 = result1[0] * result1[1]

# Partie 2
part2 = knot_hash(content).lower()

# Affichage
print(part1)
print(part2)