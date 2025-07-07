import sys

def part1(data):
    _map = data[0]
    locations = {(0, 0)}
    santa = (0, 0)
    directions = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    add_location = locations.add
    for d in _map:
        x, y = santa
        dx, dy = directions[d]
        santa = (x + dx, y + dy)
        add_location(santa)
    return len(locations)

def part2(data):
    _map = data[0]
    locations = {(0, 0)}
    santas = [(0, 0), (0, 0)]
    directions = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    add_location = locations.add
    for i, d in enumerate(_map):
        idx = i % 2
        x, y = santas[idx]
        dx, dy = directions[d]
        santas[idx] = (x + dx, y + dy)
        add_location(santas[idx])
    return len(locations)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")