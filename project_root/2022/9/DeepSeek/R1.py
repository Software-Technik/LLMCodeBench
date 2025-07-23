import sys

def part1(data):
    return simulate(data, 2)

def part2(data):
    return simulate(data, 10)

def simulate(data, knots_num):
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    knots = [[0, 0] for _ in range(knots_num)]
    positions = set()
    positions.add(tuple(knots[-1]))
    
    for line in data:
        _dir, n = line.split()
        dx_head, dy_head = directions[_dir]
        for _ in range(int(n)):
            knots[0][0] += dx_head
            knots[0][1] += dy_head
            
            for i in range(knots_num - 1):
                dx = knots[i][0] - knots[i+1][0]
                dy = knots[i][1] - knots[i+1][1]
                if abs(dx) <= 1 and abs(dy) <= 1:
                    break
                knots[i+1][0] += (dx > 0) - (dx < 0)
                knots[i+1][1] += (dy > 0) - (dy < 0)
            positions.add(tuple(knots[-1]))
    return len(positions)

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")