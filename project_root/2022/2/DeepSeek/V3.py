import sys

def part1(data):
    col1 = {'A': 1, 'B': 2, 'C': 3}
    col2 = {'X': 1, 'Y': 2, 'Z': 3}
    scores = [3, 0, 6]  # L, D, W
    
    total_score = 0

    for line in data:
        shape1, shape2 = line.split()
        x = col1[shape1]
        y = col2[shape2]
        res = (y - x) % 3
        total_score += y + scores[res]

    return total_score

def part2(data):
    col1 = {'A': 1, 'B': 2, 'C': 3}
    col2 = {'X': 0, 'Y': 3, 'Z': 6}
    shape_map = [0, 2, 1]  # for X (0), Y (3), Z (6)
    
    total_score = 0

    for line in data:
        shape1, shape2 = line.split()
        x = col1[shape1]
        round_score = col2[shape2]
        y = (x + shape_map[round_score // 3]) % 3 or 3
        total_score += y + round_score

    return total_score

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")