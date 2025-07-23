import sys

def part1(data):
    x, y = 0, 0
    locations = {(x, y)}
    directions = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0),
    }
    for d in data[0]:
        dx, dy = directions[d]
        x += dx
        y += dy
        locations.add((x, y))
    return len(locations)

def part2(data):
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    locations = {(santa_x, santa_y)}
    directions = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0),
    }
    for i, d in enumerate(data[0]):
        dx, dy = directions[d]
        if i % 2 == 0:
            santa_x += dx
            santa_y += dy
            locations.add((santa_x, santa_y))
        else:
            robo_x += dx
            robo_y += dy
            locations.add((robo_x, robo_y))
    return len(locations)

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")