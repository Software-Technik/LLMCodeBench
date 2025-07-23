import sys
from collections import defaultdict

def part1(data):
    grid = defaultdict(int)
    for inst in data:
        parts = inst.split()
        if parts[0] == "turn":
            op = parts[0] + " " + parts[1]
            coord1 = parts[2]
            coord2 = parts[4]
        else:
            op = parts[0]
            coord1 = parts[1]
            coord2 = parts[3]
        
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))
        
        if op == "turn on":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] = 1
        elif op == "turn off":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] = 0
        else:  # toggle
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] = 1 - grid[(x, y)]
    
    return sum(grid.values())

def part2(data):
    grid = defaultdict(int)
    for inst in data:
        parts = inst.split()
        if parts[0] == "turn":
            op = parts[0] + " " + parts[1]
            coord1 = parts[2]
            coord2 = parts[4]
        else:
            op = parts[0]
            coord1 = parts[1]
            coord2 = parts[3]
        
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))
        
        if op == "turn on":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] += 1
        elif op == "turn off":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] = max(grid[(x, y)] - 1, 0)
        else:  # toggle
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] += 2
    
    return sum(grid.values())

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")