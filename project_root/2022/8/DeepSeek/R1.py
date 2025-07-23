import sys

def part1(data):
    trees = [[*map(int, line)] for line in data]
    h = len(trees)
    w = len(trees[0])
    total = 2 * (w + h - 2)
    
    left_max = [[-1] * w for _ in range(h)]
    for y in range(h):
        for x in range(1, w):
            left_max[y][x] = max(trees[y][x-1], left_max[y][x-1])
    
    right_max = [[-1] * w for _ in range(h)]
    for y in range(h):
        for x in range(w-2, -1, -1):
            right_max[y][x] = max(trees[y][x+1], right_max[y][x+1])
    
    top_max = [[-1] * w for _ in range(h)]
    for x in range(w):
        for y in range(1, h):
            top_max[y][x] = max(trees[y-1][x], top_max[y-1][x])
    
    bottom_max = [[-1] * w for _ in range(h)]
    for x in range(w):
        for y in range(h-2, -1, -1):
            bottom_max[y][x] = max(trees[y+1][x], bottom_max[y+1][x])
    
    for y in range(1, h-1):
        for x in range(1, w-1):
            t = trees[y][x]
            if t > min(left_max[y][x], right_max[y][x], top_max[y][x], bottom_max[y][x]):
                total += 1
    return total

def part2(data):
    trees = [[*map(int, line)] for line in data]
    h = len(trees)
    w = len(trees[0])
    best = 0
    
    for y in range(1, h-1):
        for x in range(1, w-1):
            t = trees[y][x]
            left = 0
            for i in range(x-1, -1, -1):
                left += 1
                if trees[y][i] >= t:
                    break
            right = 0
            for i in range(x+1, w):
                right += 1
                if trees[y][i] >= t:
                    break
            top = 0
            for i in range(y-1, -1, -1):
                top += 1
                if trees[i][x] >= t:
                    break
            bottom = 0
            for i in range(y+1, h):
                bottom += 1
                if trees[i][x] >= t:
                    break
            score = left * right * top * bottom
            if score > best:
                best = score
    return best

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")