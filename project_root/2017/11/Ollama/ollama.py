import sys

def to_axial(d):
    return {
        "n": (0, -1),
        "nw": (-1, 0),
        "sw": (-1, 1),
        "s": (0, 1),
        "se": (1, 0),
        "ne": (1, -1)
    }[d]

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def distance_to_origin(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))

position = (0, 0)
max_distance = 0

for instruction in open(sys.argv[1]).read().strip().split(","):
    position = add(position, to_axial(instruction))
    current_distance = distance_to_origin(position)
    if current_distance > max_distance:
        max_distance = current_distance

print(max_distance)
print(distance_to_origin(position))