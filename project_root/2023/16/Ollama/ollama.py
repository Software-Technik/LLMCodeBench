import sys

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

def traverse(matrix, start, direction, beans):
    i, j = start
    if (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or (i, j, direction) in beans):
        return

    while True:
        beans.add((i, j, direction))
        if matrix[i][j] == "|":
            if direction in (UP, DOWN):
                yield i + (-1 if direction == UP else 1), j
            elif direction in (LEFT, RIGHT):
                for d in (UP, DOWN):
                    yield i - 1, j
                    i += 2
        elif matrix[i][j] == "-":
            if direction in (UP, DOWN):
                for d in (LEFT, RIGHT):
                    yield i, j + (-1 if d == LEFT else 1)
                    j += 2
        elif matrix[i][j] == "\\":
            delta = (-1, -1) if direction == UP else (1, -1) if direction == DOWN else (0, 1)
            i += delta[0]
            j += delta[1]
            yield i + delta[0], j + delta[1]
        elif matrix[i][j] == "/":
            delta = (-1, -1) if direction == UP else (1, 1) if direction == DOWN else (-1, 0)
            i += delta[0]
            j += delta[1]

        if not (0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j] != "."):
            break

def part1(text: str) -> int:
    matrix = [line for line in text.splitlines()]
    beans = set(traverse(matrix, (0, 0), RIGHT, beans))
    return len(set((i, j) for i, j, _ in beans))

def energize(matrix, start, direction):
    return len(set(traverse(matrix, start, direction, set()).unique_beans))

def part2(text: str) -> int:
    matrix = [line for line in text.splitlines()]
    max_val = 0
    for i in range(len(matrix[0])):
        for d in (UP, DOWN):
            yield energize(matrix, (i, 0), d)
    for j in range(len(matrix)):
        for d in (LEFT, RIGHT):
            yield len(set(traverse(energize(matrix, (j, len(matrix[i]) - 1))))).unique_beans()])

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {max(part2(text), default=0)}")