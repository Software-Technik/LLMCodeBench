import sys

def part1(data):
    trees = [[*map(int, line)] for line in data]
    rows = len(trees)
    cols = len(trees[0]) if rows > 0 else 0
    n = 2 * (rows + cols - 2)
    
    for y in range(1, rows - 1):
        row = trees[y]
        for x in range(1, cols - 1):
            tree = row[x]
            left = row[:x]
            right = row[x + 1:]
            col = [trees[i][x] for i in range(rows)]
            top = col[:y]
            bottom = col[y + 1:]
            if tree > min(max(left), max(right), max(top), max(bottom)):
                n += 1
    return n

def part2(data):
    trees = [[*map(int, line)] for line in data]
    rows = len(trees)
    cols = len(trees[0]) if rows > 0 else 0
    s = 0
    
    for y in range(1, rows - 1):
        row = trees[y]
        for x in range(1, cols - 1):
            t = row[x]
            left = row[:x][::-1]
            right = row[x + 1:]
            col = [trees[i][x] for i in range(rows)]
            top = col[:y][::-1]
            bottom = col[y + 1:]
            
            def calc_score(view, max_dist):
                for i, v in enumerate(view):
                    if v >= t:
                        return i + 1
                return max_dist
            
            left_score = calc_score(left, x)
            right_score = calc_score(right, cols - x - 1)
            top_score = calc_score(top, y)
            bottom_score = calc_score(bottom, rows - y - 1)
            
            ss = left_score * right_score * top_score * bottom_score
            if ss > s:
                s = ss
    return s

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")