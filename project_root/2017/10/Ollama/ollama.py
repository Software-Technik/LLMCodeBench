import sys
from functools import reduce

def knot_logic(lengths):
    nums, pos, skip = list(range(256)), 0, 0
    for length in lengths:
        if length > 1:  # Ensure we're not just reversing a single element
            length %= 256
            nums[pos:(pos + length)] = reversed(nums[pos:(pos + length)])
        pos = (pos + length + skip) % 256
        skip += 1

    return nums[0] * nums[1]

def knot_hash(input_str):
    lengths = [*map(ord, input_str.strip()), 17, 31, 73, 47, 23]
    sparse = list(range(256))
    pos, skip = 0, 0

    for _ in range(64):
        for length in lengths:
            length %= 256
            if length > 1:  # Ensure we're not just reversing a single element
                sparse[pos:(pos + length)] = reversed(sparse[pos:(pos + length)])
            pos = (pos + length + skip) % 256
            skip += 1

    dense_hash = [str(reduce(lambda x, y: x ^ y, sparse[i:i+16])) for i in range(0, 256, 16)]
    return ''.join(dense_hash).lower()

input_str = open(sys.argv[1]).read().strip()
print(knot_logic(list(map(int, input_str.split(',')))))
print(knot_hash(input_str))