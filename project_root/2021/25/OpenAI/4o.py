import sys

def part1(data):
    mapping = {'.': 0, '>': 1, 'v': 2}
    board1 = [[mapping[x] for x in line] for line in data]
    rows, cols = len(board1), len(board1[0])

    count, moved = 0, True
    while moved:
        moved = False
        new_board1 = [row[:] for row in board1]

        for r in range(rows):
            for c in range(cols):
                if board1[r][c] == 1 and board1[r][(c + 1) % cols] == 0:
                    new_board1[r][c] = 0
                    new_board1[r][(c + 1) % cols] = 1
                    moved = True

        board1 = [row[:] for row in new_board1]

        for r in range(rows):
            for c in range(cols):
                if new_board1[r][c] == 2 and new_board1[(r + 1) % rows][c] == 0:
                    board1[r][c] = 0
                    board1[(r + 1) % rows][c] = 2
                    moved = True

        count += 1
    
    return count

# Reading input
input_path = sys.argv[1]
with open(input_path) as f:
    data = f.read().strip().splitlines()

# Output the result
sys.stdout.write(f"{part1(data)}")