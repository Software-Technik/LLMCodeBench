import sys

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


def traverse(matrix, start, direction, beans):
    stack = [(start, direction)]
    while stack:
        (i, j), direction = stack.pop()
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
            continue
        if (i, j, direction) in beans:
            continue
        beans.add((i, j, direction))
        cell = matrix[i][j]
        if cell == "|":
            if direction in (LEFT, RIGHT):
                stack.append(((i - 1, j), UP))
                stack.append(((i + 1, j), DOWN))
            elif direction == UP:
                stack.append(((i - 1, j), UP))
            elif direction == DOWN:
                stack.append(((i + 1, j), DOWN))
            continue
        if cell == "-":
            if direction in (UP, DOWN):
                stack.append(((i, j - 1), LEFT))
                stack.append(((i, j + 1), RIGHT))
            elif direction == LEFT:
                stack.append(((i, j - 1), LEFT))
            elif direction == RIGHT:
                stack.append(((i, j + 1), RIGHT))
            continue
        if cell == "\\":
            if direction == UP:
                stack.append(((i, j - 1), LEFT))
            elif direction == DOWN:
                stack.append(((i, j + 1), RIGHT))
            elif direction == LEFT:
                stack.append(((i - 1, j), UP))
            elif direction == RIGHT:
                stack.append(((i + 1, j), DOWN))
            continue
        if cell == "/":
            if direction == UP:
                stack.append(((i, j + 1), RIGHT))
            elif direction == DOWN:
                stack.append(((i, j - 1), LEFT))
            elif direction == LEFT:
                stack.append(((i + 1, j), DOWN))
            elif direction == RIGHT:
                stack.append(((i - 1, j), UP))
            continue
        if cell == ".":
            ni, nj = i, j
            if direction == RIGHT:
                nj += 1
            elif direction == LEFT:
                nj -= 1
            elif direction == UP:
                ni -= 1
            elif direction == DOWN:
                ni += 1
            stack.append(((ni, nj), direction))


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
        r = energize(matrix, (i, 0), RIGHT)
        if r > result:
            result = r
        r = energize(matrix, (i, len(matrix[i]) - 1), LEFT)
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