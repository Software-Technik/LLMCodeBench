import sys
import numpy as np

def part1(data):
    mapping = {'.': 0, '>': 1, 'v': 2}
    board = np.array([[mapping[x] for x in line] for line in data], dtype=np.uint8)
    
    count = 0
    while True:
        moved = False
        
        # East-moving cucumbers
        east_mask = (board == 1)
        empty_east = (board == 0)
        can_move_east = east_mask & np.roll(empty_east, -1, axis=1)
        if np.any(can_move_east):
            moved = True
            board[can_move_east] = 0
            moved_east = np.roll(can_move_east, 1, axis=1)
            board[moved_east] = 1
        
        # South-moving cucumbers
        south_mask = (board == 2)
        empty_south = (board == 0)
        can_move_south = south_mask & np.roll(empty_south, -1, axis=0)
        if np.any(can_move_south):
            moved = True
            board[can_move_south] = 0
            moved_south = np.roll(can_move_south, 1, axis=0)
            board[moved_south] = 2
        
        if not moved:
            break
        count += 1
    return count + 1

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)}")