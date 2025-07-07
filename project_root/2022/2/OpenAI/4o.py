import sys

def part1(data):
    scores = {(1, 1): 3, (2, 2): 3, (3, 3): 3,
              (1, 2): 6, (2, 3): 6, (3, 1): 6,
              (2, 1): 0, (3, 2): 0, (1, 3): 0}

    total_score = 0

    for line in data:
        x, y = ord(line[0]) - 64, ord(line[2]) - 87
        total_score += y + scores[(x, y)]

    return total_score

def part2(data):
    total_score = 0

    for line in data:
        x, round_score = ord(line[0]) - 64, (ord(line[2]) - 88) * 3
        if round_score == 6:
            y = x % 3 + 1
        elif round_score == 3:
            y = x
        else:
            y = (x + 1) % 3 + 1

        total_score += y + round_score

    return total_score

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n{part2(data)}")