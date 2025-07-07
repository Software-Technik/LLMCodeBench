import sys

def process_input(data):
    return [[*map(int, x.replace(' -> ', ',').split(','))] for x in data]

def max_size(data):
    return max(max(x) for x in data) + 1

def part1(data):
    data = process_input(data)
    size = max_size(data)
    diagram = [[0] * size for _ in range(size)]

    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            if x1 > x2 or y1 > y2:
                x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    diagram[j][i] += 1

    return sum(1 for row in diagram for cell in row if cell > 1)

def part2(data):
    data = process_input(data)
    size = max_size(data)
    diagram = [[0] * size for _ in range(size)]

    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            if x1 > x2 or y1 > y2:
                x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    diagram[j][i] += 1
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            x_step = 1 if x1 <= x2 else -1
            y_step = 1 if y1 <= y2 else -1
            for i, j in zip(range(x1, x2 + x_step, x_step), range(y1, y2 + y_step, y_step)):
                diagram[j][i] += 1

    return sum(1 for row in diagram for cell in row if cell > 1)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

print(f"{part1(data)} {part2(data)}")