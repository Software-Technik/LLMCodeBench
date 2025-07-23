import sys

axial_map = {
    "n": (0, -1),
    "nw": (-1, 0),
    "sw": (-1, 1),
    "s": (0, 1),
    "se": (1, 0),
    "ne": (1, -1)
}

with open(sys.argv[1]) as f:
    instructions = f.read().strip().split(',')

p, q = 0, 0
max_distance = 0
for direction in instructions:
    dp, dq = axial_map[direction]
    p += dp
    q += dq
    d = max(abs(p), abs(q), abs(p+q))
    if d > max_distance:
        max_distance = d

final_distance = max(abs(p), abs(q), abs(p+q))
print(final_distance)
print(max_distance)