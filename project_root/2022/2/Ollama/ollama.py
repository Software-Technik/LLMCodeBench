import sys

def part1(data):
    col_map = {"A": 0, "B": 1, "C": 2}
    scores = {0: 3, 1: 6}

    total_score = 0

    for line in data:
        shape1, shape2 = line.split()
        x = col_map[shape1]
        y = ord(shape2) - ord("X")

        result = y - x
        total_score += (y + 1) + scores.get(result % 3, result)

    return total_score

def part2(data):
    col_map = {"A": 0, "B": 1, "C": 2}
    round_scores = {"X": 0, "Y": 3, "Z": 6}

    total_score = 0

    for line in data:
        shape1, shape2 = line.split()
        x = col_map[shape1]
        y = ord(shape2) - ord("X")

        match y % 3:
            case 0:  # loss
                y = (x + 2) % 3
            case 1:  # draw
                y = x
            case 2:  # win
                y = (x + 1) % 3

        total_score += (y + 1) + round_scores[shape2]

    return total_score

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")