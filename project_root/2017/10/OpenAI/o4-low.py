import sys

def knot_logic(lengths, iterations):
    size = 256
    nums = list(range(size))
    pos = skip = 0
    for _ in range(iterations):
        for length in lengths:
            if length > size: continue
            half = length // 2
            for i in range(half):
                a = (pos + i) % size
                b = (pos + length - 1 - i) % size
                nums[a], nums[b] = nums[b], nums[a]
            pos = (pos + length + skip) % size
            skip += 1
    return nums

def knot_hash(s):
    lengths = [*map(ord, s.strip())] + [17, 31, 73, 47, 23]
    nums = knot_logic(lengths, 64)
    out = []
    for i in range(0, 256, 16):
        x = 0
        for v in nums[i:i+16]:
            x ^= v
        out.append(f"{x:02x}")
    return "".join(out)

data = open(sys.argv[1]).read().strip()
lengths1 = list(map(int, data.split(',')))
r = knot_logic(lengths1, 1)
print(r[0] * r[1])
print(knot_hash(data))