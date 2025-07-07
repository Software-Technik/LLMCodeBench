import sys

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
trans = {
    '|': {LEFT: [UP, DOWN], RIGHT: [UP, DOWN], UP: [UP], DOWN: [DOWN]},
    '-': {UP: [LEFT, RIGHT], DOWN: [LEFT, RIGHT], LEFT: [LEFT], RIGHT: [RIGHT]},
    '\\': {UP: [LEFT], DOWN: [RIGHT], LEFT: [UP], RIGHT: [DOWN]},
    '/': {UP: [RIGHT], DOWN: [LEFT], LEFT: [DOWN], RIGHT: [UP]},
}

def traverse(matrix, start_i, start_j, start_d):
    beans = set()
    stack = [(start_i, start_j, start_d)]
    n = len(matrix)
    m = [len(row) for row in matrix]
    while stack:
        i, j, d = stack.pop()
        if i < 0 or i >= n or j < 0 or j >= m[i] or (i, j, d) in beans:
            continue
        beans.add((i, j, d))
        cell = matrix[i][j]
        if cell == '.':
            stack.append((i + di[d], j + dj[d], d))
        else:
            for nd in trans.get(cell, {}).get(d, []):
                stack.append((i + di[nd], j + dj[nd], nd))
    return beans

def part1(text):
    matrix = [list(line) for line in text.splitlines()]
    beans = traverse(matrix, 0, 0, RIGHT)
    return len({(i, j) for i, j, _ in beans})

def energize(matrix, i, j, d):
    beans = traverse(matrix, i, j, d)
    return len({(i, j) for i, j, _ in beans})

def part2(text):
    matrix = [list(line) for line in text.splitlines()]
    res = 0
    n = len(matrix)
    m0 = len(matrix[0]) if n else 0
    for i in range(n):
        res = max(res, energize(matrix, i, 0, RIGHT), energize(matrix, i, len(matrix[i]) - 1, LEFT))
    for j in range(m0):
        res = max(res, energize(matrix, 0, j, DOWN), energize(matrix, n - 1, j, UP))
    return res

if __name__ == "__main__":
    text = open(sys.argv[1]).read()
    print(part1(text), part2(text))