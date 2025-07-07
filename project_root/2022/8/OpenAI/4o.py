import sys

def part1(data):
    trees = [[*map(int, line)] for line in data]

    n = 2 * (len(trees[0]) + len(trees) - 2)

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            tree = trees[y][x]

            left_max = max(trees[y][:x])
            right_max = max(trees[y][x + 1:])
            top_max = max(trees[i][x] for i in range(y))
            bottom_max = max(trees[i][x] for i in range(y + 1, len(trees)))

            if tree > min(left_max, right_max, top_max, bottom_max):
                n += 1

    return n

def part2(data):
    trees = [[*map(int, line)] for line in data]

    s = 0
    w = len(trees[0])
    h = len(trees)

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            t = trees[y][x]

            left_score = next((i + 1 for i in range(x - 1, -1, -1) if trees[y][i] >= t), x)
            right_score = next((i - x for i in range(x + 1, w) if trees[y][i] >= t), w - x - 1)
            top_score = next((i + 1 for i in range(y - 1, -1, -1) if trees[i][x] >= t), y)
            bottom_score = next((i - y for i in range(y + 1, h) if trees[i][x] >= t), h - y - 1)

            ss = left_score * right_score * top_score * bottom_score
            if ss > s:
                s = ss

    return s

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")