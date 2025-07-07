import sys

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


def traverse(matrix, start, direction, beans):
    i, j = start
    while 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and (i, j, direction) not in beans:
        beans.add((i, j, direction))
        cell = matrix[i][j]
        if cell == "|":
            if direction in (LEFT, RIGHT):
                traverse(matrix, (i - 1, j), UP, beans)
                traverse(matrix, (i + 1, j), DOWN, beans)
                return
            elif direction == UP:
                i -= 1
            elif direction == DOWN:
                i += 1
        elif cell == "-":
            if direction in (UP, DOWN):
                traverse(matrix, (i, j - 1), LEFT, beans)
                traverse(matrix, (i, j + 1), RIGHT, beans)
                return
            elif direction == LEFT:
                j -= 1
            elif direction == RIGHT:
                j += 1
        elif cell == "\\":
            if direction == UP:
                direction = LEFT; j -= 1
            elif direction == DOWN:
                direction = RIGHT; j += 1
            elif direction == LEFT:
                direction = UP; i -= 1
            elif direction == RIGHT:
                direction = DOWN; i += 1
        elif cell == "/":
            if direction == UP:
                direction = RIGHT; j += 1
            elif direction == DOWN:
                direction = LEFT; j -= 1
            elif direction == LEFT:
                direction = DOWN; i += 1
            elif direction == RIGHT:
                direction = UP; i -= 1
        else:  # Handle "." case
            if direction == RIGHT:
                j += 1
            elif direction == LEFT:
                j -= 1
            elif direction == UP:
                i -= 1
            elif direction == DOWN:
                i += 1


def part1(text):
    matrix = [list(line) for line in text.splitlines()]
    beans = set()
    traverse(matrix, (0, 0), RIGHT, beans)
    return len({(i, j) for i, j, _ in beans})


def energize(matrix, start, direction):
    beans = set()
    traverse(matrix, start, direction, beans)
    return len({(i, j) for i, j, _ in beans})


def part2(text):
    matrix = [list(line) for line in text.splitlines()]
    result = 0
    for i in range(len(matrix)):
        result = max(result, energize(matrix, (i, 0), RIGHT))
        result = max(result, energize(matrix, (i, len(matrix[i]) - 1), LEFT))
    for j in range(len(matrix[0])):
        result = max(result, energize(matrix, (0, j), DOWN))
        result = max(result, energize(matrix, (len(matrix) - 1, j), UP))
    return result

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")