import sys
import numpy as np

def part1(input_data):
    mapping = {'.': 0, '>': 1, 'v': 2}
    board1 = np.array([[mapping[x] for x in line] for line in input_data])

    count = 0
    moved = True
    while moved:
        before = np.copy(board1)

        conditions = [
            ((np.roll(board1, shift=1, axis=1) == 1) & (board1 == 0)),
            ((board1 == 1) & (np.roll(board1, shift=-1, axis=1) != 0)),
            (board1 == 2)
        ]
        for condition in conditions:
            board1[condition] = np.where(condition, [1], before)[1]

        directions = [
            (np.roll(board1, shift=1, axis=0) == 2),
            ((board1 == 2) & (np.roll(board1, shift=-1, axis=0) != 0))
        ]
        for direction in directions:
            board1[direction] = np.where(direction, 2, before)

        conditions = [
             ((directions[shift==0]) & (board1 == 0))
        ]

        count += 1
        moved = not np.array_equal(before, board1)
    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
     data_input = f.read().splitlines()

sys.stdout.write(str(part1(data_input)))