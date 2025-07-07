import sys

def part1(data):
    trees = [list(map(int, line)) for line in data]
    h, w = len(trees), len(trees[0])
    row_max_left = [[0]*w for _ in range(h)]
    row_max_right = [[0]*w for _ in range(h)]
    col_max_top = [[0]*w for _ in range(h)]
    col_max_bottom = [[0]*w for _ in range(h)]
    for y in range(h):
        m = -1
        for x in range(w):
            row_max_left[y][x] = m
            m = max(m, trees[y][x])
        m = -1
        for x in range(w-1, -1, -1):
            row_max_right[y][x] = m
            m = max(m, trees[y][x])
    for x in range(w):
        m = -1
        for y in range(h):
            col_max_top[y][x] = m
            m = max(m, trees[y][x])
        m = -1
        for y in range(h-1, -1, -1):
            col_max_bottom[y][x] = m
            m = max(m, trees[y][x])
    n = 0
    for y in range(h):
        for x in range(w):
            if x==0 or y==0 or x==w-1 or y==h-1:
                n += 1
            else:
                if trees[y][x] > min(row_max_left[y][x], row_max_right[y][x], col_max_top[y][x], col_max_bottom[y][x]):
                    n += 1
    return n

def part2(data):
    trees = [list(map(int, line)) for line in data]
    h, w = len(trees), len(trees[0])
    cols = [[trees[y][x] for y in range(h)] for x in range(w)]
    def view(arr, t):
        cnt = 0
        for v in arr:
            cnt +=1
            if v>=t: break
        return cnt
    best = 0
    for y in range(1, h-1):
        row = trees[y]
        for x in range(1, w-1):
            t = row[x]
            ls = view(reversed(row[:x]), t)
            rs = view(row[x+1:], t)
            ts = view(reversed(cols[x][:y]), t)
            bs = view(cols[x][y+1:], t)
            score = ls*rs*ts*bs
            if score>best: best=score
    return best

data = [line.strip() for line in open(sys.argv[1])]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")