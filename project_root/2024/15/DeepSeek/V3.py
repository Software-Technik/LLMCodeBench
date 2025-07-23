import sys

def part1(lines):
    grid_height = len(lines[0]) - 1
    final_grid = [["."] * 50 for _ in range(grid_height)]

    def move_from_to(from_row, from_col, go_row, go_col, final_grid):
        new_row = from_row + go_row
        new_col = from_col + go_col
        if final_grid[new_row][new_col] == ".":
            final_grid[from_row][from_col] = "."
            final_grid[new_row][new_col] = "@"
            return True
        if final_grid[new_row][new_col] == "O":
            while True:
                new_row += go_row
                new_col += go_col
                if final_grid[new_row][new_col] == "#":
                    return False
                if final_grid[new_row][new_col] == ".":
                    final_grid[from_row][from_col] = "."
                    final_grid[from_row + go_row][from_col + go_col] = "@"
                    final_grid[new_row][new_col] = "O"
                    return True
        return False

    moves = []
    row = 0
    for line in lines:
        if "#" in line[0]:
            line = line.rstrip()
            for col, char in enumerate(line):
                final_grid[row][col] = char
            row += 1
        else:
            line = line.rstrip()
            moves.extend(list(line))

    def find_robot(final_grid):
        for r in range(len(final_grid)):
            for c in range(len(final_grid[0])):
                if final_grid[r][c] == "@":
                    return r, c

    def calculate_points(final_grid):
        total = 0
        for r in range(len(final_grid)):
            for c in range(len(final_grid[0])):
                if final_grid[r][c] == "O":
                    total += r * 100 + c
        return total

    for move in moves:
        r, c = find_robot(final_grid)
        if move == "<":
            move_from_to(r, c, 0, -1, final_grid)
        elif move == ">":
            move_from_to(r, c, 0, 1, final_grid)
        elif move == "^":
            move_from_to(r, c, -1, 0, final_grid)
        elif move == "v":
            move_from_to(r, c, 1, 0, final_grid)
    return calculate_points(final_grid)

def part2(lines):
    grid_height = len(lines[0]) - 1
    final_grid = [["."] * 50 for _ in range(grid_height)]

    def find_soulmate(grid, row, col):
        if grid[row][col] == "[":
            return row, col + 1
        if grid[row][col] == "]":
            return row, col - 1
        return None

    def collect_boxes(grid, start_row, start_col, dr, dc):
        boxes = []
        queue = [(start_row, start_col)]
        visited = set()
        while queue:
            r, c = queue.pop(0)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if grid[r][c] in ["[", "]"]:
                boxes.append((r, c))
                mate = find_soulmate(grid, r, c)
                if mate:
                    queue.append(mate)
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] in ["[", "]"] and (nr, nc) not in visited:
                    queue.append((nr, nc))
                elif grid[nr][nc] == "#":
                    return None
        return boxes

    def move_from_to(from_row, from_col, dr, dc, grid):
        nr, nc = from_row + dr, from_col + dc
        if grid[nr][nc] == ".":
            grid[from_row][from_col] = "."
            grid[nr][nc] = "@"
            return True
        if (dr == 0 and dc == -1 and grid[nr][nc] == "]") or (dr == 0 and dc == 1 and grid[nr][nc] == "["):
            boxes = []
            pos = []
            current_r, current_c = nr, nc
            while True:
                pos.append((current_r, current_c))
                current_r += dr
                current_c += dc
                if not (0 <= current_r < len(grid) and 0 <= current_c < len(grid[0])):
                    return False
                if grid[current_r][current_c] == "#":
                    return False
                if grid[current_r][current_c] == ".":
                    break
            grid[from_row][from_col] = "."
            for i in range(len(pos) - 1, 0, -1):
                grid[pos[i][0]][pos[i][1]] = grid[pos[i-1][0]][pos[i-1][1]]
            grid[pos[0][0]][pos[0][1]] = "@"
            return True
        if grid[nr][nc] in ["[", "]"]:
            boxes = collect_boxes(grid, nr, nc, dr, dc)
            if not boxes:
                return False
            boxes.sort(reverse=(dr == 1))
            for r, c in boxes:
                grid[r + dr][c + dc] = grid[r][c]
                grid[r][c] = "."
            grid[from_row][from_col] = "."
            grid[nr][nc] = "@"
            return True
        return False

    moves = []
    row = 0
    for line in lines:
        if "#" in line:
            line = line.rstrip()
            for col, char in enumerate(line):
                final_grid[row][col] = char
            row += 1
        else:
            line = line.rstrip()
            moves.extend(list(line))

    temp_grid = [["."] * 100 for _ in range(grid_height)]
    for r in range(len(final_grid)):
        for c in range(len(final_grid[0])):
            if final_grid[r][c] == "#":
                temp_grid[r][2*c-1] = "#"
                temp_grid[r][2*c] = "#"
            elif final_grid[r][c] == "O":
                temp_grid[r][2*c-1] = "["
                temp_grid[r][2*c] = "]"
            elif final_grid[r][c] == "@":
                temp_grid[r][2*c-1] = "@"
                temp_grid[r][2*c] = "."
    final_grid = temp_grid

    def find_robot(grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "@":
                    return r, c

    def calculate_points(grid):
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "]":
                    total += r * 100 + c
        return total

    for move in moves:
        r, c = find_robot(final_grid)
        if move == "<":
            move_from_to(r, c, 0, -1, final_grid)
        elif move == ">":
            move_from_to(r, c, 0, 1, final_grid)
        elif move == "^":
            move_from_to(r, c, -1, 0, final_grid)
        elif move == "v":
            move_from_to(r, c, 1, 0, final_grid)
    return calculate_points(final_grid)

input_path = sys.argv[1]
with open(input_path, "r") as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))