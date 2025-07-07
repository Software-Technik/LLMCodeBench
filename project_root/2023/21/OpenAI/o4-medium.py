import sys

def parse(text):
    lines = text.strip().splitlines()
    grid = set()
    start = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                grid.add((x, y))
            elif c == 'S':
                start = (x, y)
    return grid, start, len(lines[0])

def part1(grid, start):
    deltas = ((1,0),(-1,0),(0,1),(0,-1))
    frontier = {start}
    for _ in range(64):
        new = set()
        for x, y in frontier:
            for dx, dy in deltas:
                n = (x+dx, y+dy)
                if n not in grid:
                    new.add(n)
        frontier = new
    return len(frontier)

def part2(grid, start, width):
    deltas = ((1,0),(-1,0),(0,1),(0,-1))
    frontier = {start}
    pts = []
    step = 0
    target = 26501365
    half = width//2
    while len(pts) < 3:
        step += 1
        new = set()
        for x, y in frontier:
            for dx, dy in deltas:
                nx = (x+dx) % width
                ny = (y+dy) % width
                if (nx, ny) not in grid:
                    new.add((nx, ny))
        frontier = new
        if step % width == half:
            pts.append(len(frontier))
    c = pts[0]
    b = pts[1] - pts[0]
    a = pts[2] - pts[1]
    x = target // width
    return c + b * x + (x*(x-1)//2)*(a-b)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
    grid, start, width = parse(text)
    r1 = part1(grid, start)
    r2 = part2(grid, start, width)
    print(r1, r2)