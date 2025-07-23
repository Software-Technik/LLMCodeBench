import sys

def part1(lines):
    rows = len(lines) - (len(lines) - sum(1 for line in lines if '#' in line[0]))
    cols = 50
    final_grid = [["."] * cols for _ in range(rows)]
    
    moves = []
    row_idx = 0
    for line in lines:
        if '#' in line[0]:
            line = line.strip()
            for col_idx, char in enumerate(line):
                if col_idx < cols:
                    final_grid[row_idx][col_idx] = char
            row_idx += 1
        else:
            moves.extend(list(line.strip()))
    
    robot_row, robot_col = None, None
    for r in range(rows):
        for c in range(cols):
            if final_grid[r][c] == '@':
                robot_row, robot_col = r, c
                break
        if robot_row is not None:
            break
    
    def move_from_to(from_row, from_col, dr, dc, grid):
        new_row, new_col = from_row + dr, from_col + dc
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
        if grid[new_row][new_col] == '.':
            grid[from_row][from_col] = '.'
            grid[new_row][new_col] = '@'
            return True, new_row, new_col
        if grid[new_row][new_col] == 'O':
            r_offset, c_offset = dr, dc
            while True:
                r_offset += dr
                c_offset += dc
                next_row, next_col = from_row + r_offset, from_col + c_offset
                if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
                    return False, from_row, from_col
                if grid[next_row][next_col] == '#':
                    return False, from_row, from_col
                if grid[next_row][next_col] == '.':
                    grid[from_row][from_col] = '.'
                    grid[from_row + dr][from_col + dc] = '@'
                    grid[next_row][next_col] = 'O'
                    return True, from_row + dr, from_col + dc
        return False, from_row, from_col

    for move in moves:
        if move == '<':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, 0, -1, final_grid)
        elif move == '>':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, 0, 1, final_grid)
        elif move == '^':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, -1, 0, final_grid)
        elif move == 'v':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, 1, 0, final_grid)
    
    total = 0
    for r in range(len(final_grid)):
        for c in range(len(final_grid[0])):
            if final_grid[r][c] == 'O':
                total += r * 100 + c
    return total

def part2(lines):
    rows = len(lines) - (len(lines) - sum(1 for line in lines if '#' in line[0]))
    cols = 50
    final_grid = [["."] * cols for _ in range(rows)]
    
    moves = []
    row_idx = 0
    for line in lines:
        if '#' in line[0]:
            line = line.strip()
            for col_idx, char in enumerate(line):
                if col_idx < cols:
                    final_grid[row_idx][col_idx] = char
            row_idx += 1
        else:
            moves.extend(list(line.strip()))
    
    temp_grid = [["."] * 100 for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            char = final_grid[r][c]
            if char == '#':
                temp_grid[r][2*c-1] = '#'
                temp_grid[r][2*c] = '#'
            elif char == 'O':
                temp_grid[r][2*c-1] = '['
                temp_grid[r][2*c] = ']'
            elif char == '.':
                temp_grid[r][2*c-1] = '.'
                temp_grid[r][2*c] = '.'
            elif char == '@':
                temp_grid[r][2*c-1] = '@'
                temp_grid[r][2*c] = '.'
    final_grid = temp_grid
    rows = len(final_grid)
    cols = len(final_grid[0])
    
    robot_row, robot_col = None, None
    for r in range(rows):
        for c in range(cols):
            if final_grid[r][c] == '@':
                robot_row, robot_col = r, c
                break
        if robot_row is not None:
            break
    
    def find_soulmate(grid, r, c):
        if grid[r][c] == '[':
            return r, c+1
        if grid[r][c] == ']':
            return r, c-1
        return None
    
    def collect_boxes_and_validate(grid, start_r, start_c, dr, dc):
        visited = set()
        stack = [(start_r, start_c)]
        boxes = set()
        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            boxes.add((r, c))
            soul = find_soulmate(grid, r, c)
            if soul and soul not in visited:
                stack.append(soul)
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                cell = grid[nr][nc]
                if cell in ['[', ']'] and (nr, nc) not in visited:
                    stack.append((nr, nc))
                elif cell == '#':
                    return None
            else:
                return None
        return sorted(boxes, reverse=(dr == 1))
    
    def move_from_to(from_row, from_col, dr, dc, grid):
        new_row, new_col = from_row + dr, from_col + dc
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False, from_row, from_col
        if grid[new_row][new_col] == '.':
            grid[from_row][from_col] = '.'
            grid[new_row][new_col] = '@'
            return True, new_row, new_col
        if dr == 0 and dc == -1 and grid[new_row][new_col] == ']':
            steps = [(-1, 0)]
            while True:
                new_col -= 1
                if not (0 <= new_col < len(grid[0])):
                    return False, from_row, from_col
                if grid[new_row][new_col] == '#':
                    return False, from_row, from_col
                if grid[new_row][new_col] == '.':
                    grid[from_row][from_col] = '.'
                    grid[from_row][from_col-1] = '@'
                    for i in range(len(steps)-1, 0, -1):
                        prev_r, prev_c = steps[i]
                        grid[new_row][new_col+1] = grid[new_row - prev_r][new_col+1 - prev_c]
                    grid[new_row][new_col] = ']'
                    return True, from_row, from_col-1
                steps.append((-1, 0))
        if dr == 0 and dc == 1 and grid[new_row][new_col] == '[':
            steps = [(0, 1)]
            while True:
                new_col += 1
                if not (0 <= new_col < len(grid[0])):
                    return False, from_row, from_col
                if grid[new_row][new_col] == '#':
                    return False, from_row, from_col
                if grid[new_row][new_col] == '.':
                    grid[from_row][from_col] = '.'
                    grid[from_row][from_col+1] = '@'
                    for i in range(len(steps)-1, 0, -1):
                        prev_r, prev_c = steps[i]
                        grid[new_row][new_col-1] = grid[new_row - prev_r][new_col-1 - prev_c]
                    grid[new_row][new_col] = '['
                    return True, from_row, from_col+1
                steps.append((0, 1))
        if grid[new_row][new_col] in ['[', ']']:
            boxes = collect_boxes_and_validate(grid, new_row, new_col, dr, dc)
            if not boxes:
                return False, from_row, from_col
            boxes = sorted(boxes, reverse=(dr==1))
            for r, c in boxes:
                nr, nc = r + dr, c + dc
                grid[nr][nc] = grid[r][c]
                grid[r][c] = '.'
            grid[from_row][from_col] = '.'
            grid[new_row][new_col] = '@'
            return True, new_row, new_col
        return False, from_row, from_col

    for move in moves:
        if move == '<':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, 0, -1, final_grid)
        elif move == '>':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, 0, 1, final_grid)
        elif move == '^':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, -1, 0, final_grid)
        elif move == 'v':
            success, robot_row, robot_col = move_from_to(robot_row, robot_col, 1, 0, final_grid)
    
    total = 0
    for r in range(len(final_grid)):
        for c in range(len(final_grid[0])):
            if final_grid[r][c] == ']':
                total += r * 100 + c
    return total

input_path = sys.argv[1]
with open(input_path, 'r') as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))