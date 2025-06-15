import sys
import numpy as np


def part1(data):
    mapping = {'.': 0, '>': 1, 'v': 2}
    board1 = np.array([[mapping[x] for x in line] for line in data])

    count, moved = 0, True
    while moved:
        before = board1.copy()

        board2 = np.zeros_like(board1)
        board2[(np.roll(board1, 1, axis=1) == 1) & (board1 == 0)] = 1
        board2[(board1 == 1) & (np.roll(board1, -1, axis=1) != 0)] = 1
        board2[board1 == 2] = 2

        board1 = np.zeros_like(board2)
        board1[(np.roll(board2, 1, axis=0) == 2) & (board2 == 0)] = 2
        board1[(board2 == 2) & (np.roll(board2, -1, axis=0) != 0)] = 2
        board1[board2 == 1] = 1

        count += 1
        moved = not np.array_equal(before, board1)
    return count

<<<<<<< HEAD
def part2(data):
    return "There_is_no_part_2"

=======
>>>>>>> 6a5836a4cd32758c4ae8beaea3fb210354fd910a
inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

<<<<<<< HEAD
sys.stdout.write(f"{part1(data)} {part2(data)}")
=======
sys.stdout.write(f"{part1(data)}")
>>>>>>> 6a5836a4cd32758c4ae8beaea3fb210354fd910a
