import copy
import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    lines = data.splitlines()

result1 = 0
result2 = 0

def line_transform(line):
    return list(line)

lines = [line_transform(line) for line in lines]

seats = copy.deepcopy(lines)
seats_part2 = copy.deepcopy(lines)

def adjacent(_seats, x, y):
    adj = 0
    rows = len(_seats)
    cols = len(_seats[0]) if rows > 0 else 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            yy = y + dy
            xx = x + dx
            if 0 <= yy < rows and 0 <= xx < cols and _seats[yy][xx] == '#':
                adj += 1
    return adj

def occd(seats):
    return sum(row.count('#') for row in seats)

def eq(s1, s2):
    for y in range(len(s1)):
        if s1[y] != s2[y]:
            return False
    return True

def round(_seats):
    nu_seats = copy.deepcopy(_seats)
    rows = len(_seats)
    cols = len(_seats[0]) if rows > 0 else 0
    for y in range(rows):
        for x in range(cols):
            cur = _seats[y][x]
            if cur == '.':
                continue
            adj = adjacent(_seats, x, y)
            if cur == 'L' and adj == 0:
                nu_seats[y][x] = '#'
            elif cur == '#' and adj >= 4:
                nu_seats[y][x] = 'L'
    return nu_seats

for i in range(5000):
    nu_seats = round(seats)
    if eq(nu_seats, seats):
        result1 = occd(nu_seats)
        break
    seats = nu_seats

def visible(_seats, x, y):
    adj = 0
    rows = len(_seats)
    cols = len(_seats[0]) if rows > 0 else 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            step = 1
            while True:
                yy = y + dy * step
                xx = x + dx * step
                if not (0 <= yy < rows and 0 <= xx < cols):
                    break
                if _seats[yy][xx] == '#':
                    adj += 1
                    break
                elif _seats[yy][xx] == 'L':
                    break
                step += 1
    return adj

def round2(_seats):
    nu_seats = copy.deepcopy(_seats)
    rows = len(_seats)
    cols = len(_seats[0]) if rows > 0 else 0
    for y in range(rows):
        for x in range(cols):
            cur = _seats[y][x]
            if cur == '.':
                continue
            adj = visible(_seats, x, y)
            if cur == 'L' and adj == 0:
                nu_seats[y][x] = '#'
            elif cur == '#' and adj >= 5:
                nu_seats[y][x] = 'L'
    return nu_seats

seats = seats_part2
for i in range(500000000):
    nu_seats = round2(seats)
    if eq(nu_seats, seats):
        result2 = occd(nu_seats)
        break
    seats = nu_seats

print(result1, result2)