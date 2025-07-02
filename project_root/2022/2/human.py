import sys

def part1(data):
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 1, "Y": 2, "Z": 3}
    scores = {"L": 0, "D": 3, "W": 6}

    total_score = 0

    for line in data:
        shape1, shape2 = line.split()
        x = col1[shape1]
        y = col2[shape2]

        match y - x:
            case 0:
                round = "D"
            case -2 | 1:
                round = "W"
            case -1 | 2:
                round = "L"

        total_score += y + scores[round]

    return total_score

def part2(data):
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 0, "Y": 3, "Z": 6}

    total_score = 0

    for line in data:
        shape1, shape2 = line.split()
        x = col1[shape1]
        round_score = col2[shape2]

        match round_score:
            case 6:  # win
                y = x % 3 + 1
            case 3:  # draw
                y = x
            case 0:  # loss
                y = (x + 1) % 3 + 1

        total_score += y + round_score

    return total_score

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")