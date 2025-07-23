import sys

def part1(data):
    rock = parse_data(data)
    obstacles = rock.copy()
    rest_count = 0
    max_depth = max(y for _, y in rock)

    while True:
        x, y = 500, 0
        while y < max_depth:
            if (x, y+1) not in obstacles:
                y += 1
                continue
            if (x-1, y+1) not in obstacles:
                x -= 1
                y += 1
                continue
            if (x+1, y+1) not in obstacles:
                x += 1
                y += 1
                continue
            obstacles.add((x, y))
            rest_count += 1
            break
        else:
            break

    return rest_count

def part2(data):
    rock = parse_data(data)
    obstacles = rock.copy()
    rest_count = 0
    ground = max(y for _, y in rock) + 2

    while (500, 0) not in obstacles:
        x, y = 500, 0
        while True:
            if y + 1 < ground:
                if (x, y+1) not in obstacles:
                    y += 1
                    continue
                if (x-1, y+1) not in obstacles:
                    x -= 1
                    y += 1
                    continue
                if (x+1, y+1) not in obstacles:
                    x += 1
                    y += 1
                    continue
            obstacles.add((x, y))
            rest_count += 1
            break

    return rest_count

def parse_data(data):
    rock = set()

    for line in data:
        coords = [tuple(map(int, i.split(","))) for i in line.split(" -> ")]
        for i in range(len(coords) - 1):
            if coords[i][0] == coords[i + 1][0]:
                a, b = sorted([coords[i][1], coords[i + 1][1]])
                for j in range(a, b + 1):
                    rock.add((coords[i][0], j))
            else:
                a, b = sorted([coords[i][0], coords[i + 1][0]])
                for j in range(a, b + 1):
                    rock.add((j, coords[i][1]))

    return rock

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")