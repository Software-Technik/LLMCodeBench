import sys

def part1(data):
    rock = parse_data(data)
    rest = set()
    max_depth = max(y for _, y in rock)
    falls = [(0, 1), (-1, 1), (1, 1)]
    sand_pos = (500, 0)
    count = 0

    while True:
        x, y = sand_pos
        if y >= max_depth:
            break
        moved = False
        for dx, dy in falls:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in rock and (nx, ny) not in rest:
                sand_pos = (nx, ny)
                moved = True
                break
        if not moved:
            rest.add(sand_pos)
            count += 1
            sand_pos = (500, 0)

    return count

def part2(data):
    rock = parse_data(data)
    rest = set()
    ground = max(y for _, y in rock) + 2
    falls = [(0, 1), (-1, 1), (1, 1)]
    sand_pos = (500, 0)
    count = 0

    while (500, 0) not in rest:
        x, y = sand_pos
        moved = False
        for dx, dy in falls:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in rock and (nx, ny) not in rest and ny < ground:
                sand_pos = (nx, ny)
                moved = True
                break
        if not moved:
            rest.add(sand_pos)
            count += 1
            sand_pos = (500, 0)

    return count

def parse_data(data):
    rock = set()

    for line in data:
        coords = [tuple(map(int, i.split(","))) for i in line.split(" -> ")]
        for i in range(len(coords) - 1):
            x1, y1 = coords[i]
            x2, y2 = coords[i + 1]
            if x1 == x2:
                y_start, y_end = sorted([y1, y2])
                for y in range(y_start, y_end + 1):
                    rock.add((x1, y))
            else:
                x_start, x_end = sorted([x1, x2])
                for x in range(x_start, x_end + 1):
                    rock.add((x, y1))

    return rock

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")