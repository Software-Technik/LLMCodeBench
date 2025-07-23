import sys

def to_axial(direction):
    return {
        "n":  (0, -1),
        "nw": (-1, 0),
        "sw": (-1, 1),
        "s":  (0, 1),
        "se": (1, 0),
        "ne": (1, -1)
    }[direction]

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def distance_to_origin(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))

def main():
    with open(sys.argv[1]) as f:
        instructions = f.read().strip().split(",")
    
    position = (0, 0)
    max_distance = 0
    
    for direction in instructions:
        position = add(position, to_axial(direction))
        current_distance = distance_to_origin(position)
        if current_distance > max_distance:
            max_distance = current_distance
    
    print(distance_to_origin(position))
    print(max_distance)

if __name__ == "__main__":
    main()