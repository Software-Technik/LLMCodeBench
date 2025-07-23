import sys
import numpy as np

def part1(data):
    mapping = {'.': 0, '>': 1, 'v': 2}
    current = np.array([[mapping[x] for x in line] for line in data])
    count = 0
    moved = True
    while moved:
        can_move_east = (current == 1) & (np.roll(current, -1, axis=1) == 0)
        next_east = current.copy()
        next_east[can_move_east] = 0
        next_east[np.roll(can_move_east, 1, axis=1)] = 1
        
        can_move_south = (next_east == 2) & (np.roll(next_east, -1, axis=0) == 0)
        next_board = next_east.copy()
        next_board[can_move_south] = 0
        next_board[np.roll(can_move_south, 1, axis=0)] = 2
        
        moved = not np.array_equal(current, next_board)
        current = next_board
        count += 1
    return count

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)}")