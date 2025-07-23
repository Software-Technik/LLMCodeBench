import sys

def part1(map_data):
    map_len = len(map_data)
    locations = {(0, 0)}
    santa = (0, 0)
    directions = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    for i in range(map_len):
        direction = map_data[i // map_len]
        santa = tuple(x + y for x, y in zip(santa, directions[direction]))
        locations.add(santa)
    return len(locations)

def part2(map_data):
    map_len = len(map_data)
    locations = {(0, 0)}
    santas = [(0, 0), (0, 0)]
    directions = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    for i in range(map_len):
        direction = map_data[i]
        santa_move = santas[i % 2] = tuple(x + y for x, y in zip(santas[i % 2], directions[direction]))
        locations.add(santa_move)
    return len(locations)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data[0])}\n{part2(data[0])}\n")