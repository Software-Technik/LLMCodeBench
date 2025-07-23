import sys

def part1(data):
    if not data:
        return 1
    _map = data[0]
    locations = {(0, 0)}
    x, y = 0, 0
    directions = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    for d in _map:
        dx, dy = directions[d]
        x += dx
        y += dy
        locations.add((x, y))
    return len(locations)

def part2(data):
    if not data:
        return 1
    _map = data[0]
    locations = {(0, 0)}
    santa_x, santa_y = 0, 0
    robot_x, robot_y = 0, 0
    directions = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    for i, d in enumerate(_map):
        dx, dy = directions[d]
        if i % 2 == 0:
            santa_x += dx
            santa_y += dy
            locations.add((santa_x, santa_y))
        else:
            robot_x += dx
            robot_y += dy
            locations.add((robot_x, robot_y))
    return len(locations)

input_strings = sys.argv[1]
with open(input_strings) as f:
    first_line = next(f, None)
    if first_line is not None:
        data = [first_line.strip()]
    else:
        data = []

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")