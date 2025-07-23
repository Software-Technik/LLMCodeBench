import sys

def part1(data):
    trees = list(map(lambda line: list(map(int, line)), data))

    n = 2 * (len(trees[0]) + len(trees) - 2)

    for y in range(1, len(trees) - 1):
        row = trees[y]
        col = [trees[i][y] for i in range(len(trees))]

        for x in range(1, len(row) - 1):
            tree = row[x]
            left = max((row[:x]), default=0)
            right = max((row[(x + 1):]), default=0)
            top = max((col[:y]), default=0)
            bottom = max((col[(y + 1):]), default=0)

            if tree > min(left, right, top, bottom):
                n += 1

    return n

def part2(data):
    trees = list(map(lambda line: list(map(int, line)), data))

    s = 0
    w = len(trees[0])
    h = len(trees)

    for y in range(1, h - 1):
        row = trees[y]
        col = [trees[i][y] for i in range(h)]

        for x in range(1, w - 1):
            tree = row[x]

            left = []
            for i in range(x - 1, -1, -1):
                left.append(i + 1)
                if row[i] >= tree:
                    break

            right = []
            for i in range(x + 1, len(row)):
                right.append(len(row) - i)
                if row[i] >= tree:
                    break

            top = []
            for t in range(y - 1, -1, -1):
                top.append(t + 1)
                if col[t] >= tree:
                    break

            bottom = []
            for b in range(y + 1, len(col)):
                bottom.append(len(col) - b)
                if col[b] >= tree:
                    break

            s = max(s, (left[0] if left else w - x - 1) *
                         (right[0] if right else x) *
                         (top[0] if top else h - y - 1) *
                         (bottom[0] if bottom else y))

    return s

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")