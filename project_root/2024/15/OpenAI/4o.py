import sys
from collections import deque


def part1(lines):
    final_grid = [list(line.strip()) for line in lines if '#' in line]

    def move_from_to(from_row, from_col, go_row, go_col):
        target_row, target_col = from_row + go_row, from_col + go_col
        if final_grid[target_row][target_col] == ".":
            final_grid[target_row][target_col], final_grid[from_row][from_col] = "@", "."
            return True
        if final_grid[target_row][target_col] == "O":
            move_row, move_col = go_row, go_col
            while final_grid[from_row + move_row][from_col + move_col] == "O":
                move_row += go_row
                move_col += go_col
            if final_grid[from_row + move_row][from_col + move_col] != ".":
                return False
            final_grid[from_row][from_col] = "."
            final_grid[from_row + go_row][from_col + go_col] = "@"
            final_grid[from_row + move_row][from_col + move_col] = "O"
            return True
        return False

    moves = [move for line in lines if '#' not in line for move in line.strip()]

    def findRobotCoords():
        for r, row in enumerate(final_grid):
            for c, cell in enumerate(row):
                if cell == "@":
                    return r, c

    def boxPoints():
        return sum(r * 100 + c for r, row in enumerate(final_grid) for c, cell in enumerate(row) if cell == "O")

    for move in moves:
        robot_row, robot_col = findRobotCoords()
        if move == "<":
            move_from_to(robot_row, robot_col, 0, -1)
        elif move == ">":
            move_from_to(robot_row, robot_col, 0, 1)
        elif move == "^":
            move_from_to(robot_row, robot_col, -1, 0)
        elif move == "v":
            move_from_to(robot_row, robot_col, 1, 0)

    return boxPoints()


def part2(lines):
    final_grid = [list(line.strip()) for line in lines if '#' in line]

    def find_soulmate(check_row, check_col):
        check = final_grid[check_row][check_col]
        return (check_row, check_col + 1) if check == "[" else (check_row, check_col - 1)

    def collect_boxes_and_validate(start_row, start_col, go_row, go_col):
        boxes_to_move = []
        queue = deque([(start_row, start_col)])
        while queue:
            current_row, current_col = queue.popleft()
            if (current_row, current_col) not in boxes_to_move:
                boxes_to_move.append((current_row, current_col))
                soulmate = find_soulmate(current_row, current_col)
                queue.append(soulmate)
            next_row, next_col = current_row + go_row, current_col + go_col
            if (0 <= next_row < len(final_grid) and 0 <= next_col < len(final_grid[0])
                    and final_grid[next_row][next_col] not in {"#", ".", (next_row, next_col) in boxes_to_move}):
                queue.append((next_row, next_col))
            elif final_grid[next_row][next_col] == "#":
                return None
        return boxes_to_move

    def move_from_to(from_row, from_col, go_row, go_col):
        next_row, next_col = from_row + go_row, from_col + go_col
        if final_grid[next_row][next_col] == ".":
            final_grid[next_row][next_col], final_grid[from_row][from_col] = "@", "."
            return True
        if not (final_grid[next_row][next_col] in ["[", "]"]):
            return False
        boxes = collect_boxes_and_validate(next_row, next_col, go_row, go_col)
        if boxes is None:
            return False
        boxes.sort(reverse=(go_row == 1))
        for r, c in boxes:
            final_grid[r + go_row][c + go_col] = final_grid[r][c]
            final_grid[r][c] = "."
        final_grid[from_row][from_col] = "."
        final_grid[next_row][next_col] = "@"
        return True

    moves = [move for line in lines if '#' not in line for move in line.strip()]

    temp_grid = [['.'] * (100) for _ in range(len(final_grid))]
    for r, row in enumerate(final_grid):
        for c, cell in enumerate(row):
            if cell == "#":
                temp_grid[r][2 * c:2 * c + 2] = ("#", "#")
            elif cell == "O":
                temp_grid[r][2 * c:2 * c + 2] = ("[", "]")
            elif cell == "@":
                temp_grid[r][2 * c:2 * c + 2] = ("@", ".")
            else:
                temp_grid[r][2 * c:2 * c + 2] = (".", ".")
    final_grid = temp_grid

    def findRobotCoords():
        for r, row in enumerate(final_grid):
            for c, cell in enumerate(row):
                if cell == "@":
                    return r, c

    def boxPoints():
        return sum(r * 100 + c for r, row in enumerate(final_grid) for c, cell in enumerate(row) if cell == "]")

    for move in moves:
        robot_row, robot_col = findRobotCoords()
        if move == "<":
            move_from_to(robot_row, robot_col, 0, -1)
        elif move == ">":
            move_from_to(robot_row, robot_col, 0, 1)
        elif move == "^":
            move_from_to(robot_row, robot_col, -1, 0)
        elif move == "v":
            move_from_to(robot_row, robot_col, 1, 0)

    return boxPoints()


input_path = sys.argv[1]
with open(input_path, "r") as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))