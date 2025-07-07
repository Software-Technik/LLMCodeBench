import sys

def part1(data):
    sand_pos = (500, 0)
    rock = parse_data(data)
    rest = set()
    max_depth = max(y for _, y in rock)
    next_pos = ((0, 1), (-1, 1), (1, 1))

    while sand_pos[1] < max_depth:
        for dx, dy in next_pos:
            next_sand_pos = (sand_pos[0] + dx, sand_pos[1] + dy)
            if next_sand_pos not in rock and next_sand_pos not in rest:
                sand_pos = next_sand_pos
                break
        else:
            rest.add(sand_pos)
            sand_pos = (500, 0)

    return len(rest)

def part2(data):
    sand_pos = (500, 0)
    rock = parse_data(data)
    rest = set()
    ground = max(y for _, y in rock) + 2
    next_pos = ((0, 1), (-1, 1), (1, 1))

    while (500, 0) not in rest:
        for dx, dy in next_pos:
            next_sand_pos = (sand_pos[0] + dx, sand_pos[1] + dy)
            if next_sand_pos not in rock and next_sand_pos not in rest and next_sand_pos[1] < ground:
                sand_pos = next_sand_pos
                break
        else:
            rest.add(sand_pos)
            sand_pos = (500, 0)

    return len(rest)

def parse_data(data):
    rock = set()
    for line in data:
        coords = [tuple(map(int, i.split(","))) for i in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
            if x1 == x2:
                rock.update((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
            else:
                rock.update((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
    return rock

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")