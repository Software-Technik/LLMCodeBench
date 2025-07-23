import sys

def part1(data):
    sand_pos = (500, 0)
    rock = parse_data(data)
    rest = set()
    max_depth = max(i[1] for i in rock)
    falls = [(0, 1), (-1, 1), (1, 1)]
    while sand_pos[1] < max_depth:
        for dx, dy in falls:
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
    ground = max(i[1] for i in rock) + 2
    falls = [(0, 1), (-1, 1), (1, 1)]
    while (500, 0) not in rest:
        for dx, dy in falls:
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
        x0, y0 = coords[0]
        for x1, y1 in coords[1:]:
            if x0 == x1:
                rock.update((x0, y) for y in range(min(y0, y1), max(y0, y1) + 1))
            else:
                rock.update((x, y0) for x in range(min(x0, x1), max(x0, x1) + 1))
            x0, y0 = x1, y1
    return rock

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")