import sys

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

def traverse(matrix, start, direction):
    stack = [(start[0], start[1], direction)]
    visited = set()
    while stack:
        i, j, d = stack.pop()
        if (i, j, d) in visited:
            continue
        visited.add((i, j, d))
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            continue
        cell = matrix[i][j]
        if cell == '.':
            if d == RIGHT:
                stack.append((i, j+1, d))
            elif d == LEFT:
                stack.append((i, j-1, d))
            elif d == UP:
                stack.append((i-1, j, d))
            elif d == DOWN:
                stack.append((i+1, j, d))
        elif cell == '|':
            if d in (LEFT, RIGHT):
                stack.append((i-1, j, UP))
                stack.append((i+1, j, DOWN))
            else:
                if d == UP:
                    stack.append((i-1, j, UP))
                elif d == DOWN:
                    stack.append((i+1, j, DOWN))
        elif cell == '-':
            if d in (UP, DOWN):
                stack.append((i, j-1, LEFT))
                stack.append((i, j+1, RIGHT))
            else:
                if d == LEFT:
                    stack.append((i, j-1, LEFT))
                elif d == RIGHT:
                    stack.append((i, j+1, RIGHT))
        elif cell == '\\':
            if d == UP:
                stack.append((i, j-1, LEFT))
            elif d == DOWN:
                stack.append((i, j+1, RIGHT))
            elif d == LEFT:
                stack.append((i-1, j, UP))
            elif d == RIGHT:
                stack.append((i+1, j, DOWN))
        elif cell == '/':
            if d == UP:
                stack.append((i, j+1, RIGHT))
            elif d == DOWN:
                stack.append((i, j-1, LEFT))
            elif d == LEFT:
                stack.append((i+1, j, DOWN))
            elif d == RIGHT:
                stack.append((i-1, j, UP))
    return visited

def part1(text):
    matrix = [list(line) for line in text.splitlines()]
    beans = traverse(matrix, (0, 0), RIGHT)
    unique_beans = set((i, j) for i, j, _ in beans if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]))
    return len(unique_beans)

def energize(matrix, start, direction):
    beans = traverse(matrix, start, direction)
    return len(set((i, j) for i, j, _ in beans if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])))

def part2(text):
    matrix = [list(line) for line in text.splitlines()]
    result = 0
    for i in range(len(matrix)):
        r = energize(matrix, (i, 0), RIGHT)
        if r > result:
            result = r
        r = energize(matrix, (i, len(matrix[0]) - 1), LEFT)
        if r > result:
            result = r
    for j in range(len(matrix[0])):
        r = energize(matrix, (0, j), DOWN)
        if r > result:
            result = r
        r = energize(matrix, (len(matrix) - 1, j), UP)
        if r > result:
            result = r
    return result

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")