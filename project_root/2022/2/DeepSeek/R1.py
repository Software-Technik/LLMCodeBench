import sys

def part1(data):
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 1, "Y": 2, "Z": 3}
    outcome_arr = [3, 6, 0]
    total_score = 0
    for line in data:
        a, b = line.split()
        x = col1[a]
        y = col2[b]
        mod_index = (y - x) % 3
        total_score += y + outcome_arr[mod_index]
    return total_score

def part2(data):
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 0, "Y": 3, "Z": 6}
    offset_arr = [2, 0, 1]
    total_score = 0
    for line in data:
        a, b = line.split()
        x = col1[a]
        round_score = col2[b]
        offset = offset_arr[round_score // 3]
        y = (x - 1 + offset) % 3 + 1
        total_score += y + round_score
    return total_score

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")