import sys
from collections import defaultdict

def part1(data):
    neighbor_offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    direction_checks = {
        'N': [(-1,-1), (-1,0), (-1,1)],
        'S': [(1,-1), (1,0), (1,1)],
        'W': [(-1,-1), (0,-1), (1,-1)],
        'E': [(-1,1), (0,1), (1,1)]
    }
    direction_move = {
        'N': (-1,0),
        'S': (1,0),
        'W': (0,-1),
        'E': (0,1)
    }
    elves = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '#':
                elves.add((i, j))
    order = ["N", "S", "W", "E"]

    for _ in range(10):
        proposals = {}
        for (y, x) in elves:
            if not any((y+dy, x+dx) in elves for (dy, dx) in neighbor_offsets):
                continue
            moved = False
            for d in order:
                check_offsets = direction_checks[d]
                if not any((y+dy, x+dx) in elves for (dy, dx) in check_offsets):
                    dy_move, dx_move = direction_move[d]
                    new_pos = (y+dy_move, x+dx_move)
                    proposals[(y, x)] = new_pos
                    moved = True
                    break
        freq = defaultdict(int)
        for new_pos in proposals.values():
            freq[new_pos] += 1
        new_elves = set()
        for pos in elves:
            if pos in proposals:
                new_pos = proposals[pos]
                if freq[new_pos] == 1:
                    new_elves.add(new_pos)
                else:
                    new_elves.add(pos)
            else:
                new_elves.add(pos)
        elves = new_elves
        order = order[1:] + [order[0]]
    
    min_x = min(x for y, x in elves)
    max_x = max(x for y, x in elves)
    min_y = min(y for y, x in elves)
    max_y = max(y for y, x in elves)
    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)

def part2(data):
    neighbor_offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    direction_checks = {
        'N': [(-1,-1), (-1,0), (-1,1)],
        'S': [(1,-1), (1,0), (1,1)],
        'W': [(-1,-1), (0,-1), (1,-1)],
        'E': [(-1,1), (0,1), (1,1)]
    }
    direction_move = {
        'N': (-1,0),
        'S': (1,0),
        'W': (0,-1),
        'E': (0,1)
    }
    elves = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '#':
                elves.add((i, j))
    order = ["N", "S", "W", "E"]
    round = 1

    while True:
        proposals = {}
        for (y, x) in elves:
            if not any((y+dy, x+dx) in elves for (dy, dx) in neighbor_offsets):
                continue
            moved = False
            for d in order:
                check_offsets = direction_checks[d]
                if not any((y+dy, x+dx) in elves for (dy, dx) in check_offsets):
                    dy_move, dx_move = direction_move[d]
                    new_pos = (y+dy_move, x+dx_move)
                    proposals[(y, x)] = new_pos
                    moved = True
                    break
        freq = defaultdict(int)
        for new_pos in proposals.values():
            freq[new_pos] += 1
        new_elves = set()
        any_moved = False
        for pos in elves:
            if pos in proposals:
                new_pos = proposals[pos]
                if freq[new_pos] == 1:
                    new_elves.add(new_pos)
                    any_moved = True
                else:
                    new_elves.add(pos)
            else:
                new_elves.add(pos)
        if not any_moved:
            break
        elves = new_elves
        order = order[1:] + [order[0]]
        round += 1

    return round

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")