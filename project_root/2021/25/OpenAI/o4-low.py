import sys

def part1(data):
    h, w = len(data), len(data[0])
    east = {(i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == '>'}
    south = {(i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == 'v'}
    steps = 0
    while True:
        moved = False
        new_east = set()
        for i, j in east:
            nj = (j + 1) % w
            if (i, nj) not in east and (i, nj) not in south:
                new_east.add((i, nj))
                moved = True
            else:
                new_east.add((i, j))
        east = new_east
        new_south = set()
        for i, j in south:
            ni = (i + 1) % h
            if (ni, j) not in east and (ni, j) not in south:
                new_south.add((ni, j))
                moved = True
            else:
                new_south.add((i, j))
        south = new_south
        steps += 1
        if not moved:
            return steps

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
print(part1(data))