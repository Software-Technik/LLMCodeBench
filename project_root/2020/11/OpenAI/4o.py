import png
import os
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines = []

seats = [[c for c in line] for line in lines]
seats_part2 = [row[:] for row in seats]

MOVES = [(dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy, dx) != (0, 0)]


def adjacent(_seats, x, y):
    adj = 0
    for dy, dx in MOVES:
        yy = y + dy
        xx = x + dx
        if 0 <= yy < len(_seats) and 0 <= xx < len(_seats[0]):
            if _seats[yy][xx] == "#":
                adj += 1
    return adj


def save_as_png(arrs, idx, folder):
    trans = {"L": 0, ".": 150, "#": 255}
    _arrs = [[trans[c] for c in row] for row in arrs]
    if not os.path.exists(folder):
        os.mkdir(folder)
    outfile = os.path.join(folder, str(idx).zfill(5) + ".png")
    png.from_array(_arrs, "L").save(outfile)


def occd(seats):
    return sum(row.count("#") for row in seats)


def eq(s1, s2):
    return all(s1[y][x] == s2[y][x] for y in range(len(s1)) for x in range(len(s1[0])))


def round(_seats):
    nu_seats = [row[:] for row in _seats]
    for y in range(len(_seats)):
        for x in range(len(_seats[0])):
            adj = adjacent(_seats, x, y)
            cur = _seats[y][x]
            if cur == "L" and adj == 0:
                nu_seats[y][x] = "#"
            elif cur == "#" and adj >= 4:
                nu_seats[y][x] = "L"
    return nu_seats


def visible(_seats, x, y):
    adj = 0
    for dy, dx in MOVES:
        step = 1
        yy = y + dy
        xx = x + dx
        while 0 <= yy < len(_seats) and 0 <= xx < len(_seats[0]):
            if _seats[yy][xx] == "#":
                adj += 1
                break
            elif _seats[yy][xx] == "L":
                break
            step += 1
            yy = y + dy * step
            xx = x + dx * step
    return adj


def round2(_seats):
    nu_seats = [row[:] for row in _seats]
    for y in range(len(_seats)):
        for x in range(len(_seats[0])):
            adj = visible(_seats, x, y)
            cur = _seats[y][x]
            if cur == "L" and adj == 0:
                nu_seats[y][x] = "#"
            elif cur == "#" and adj >= 5:
                nu_seats[y][x] = "L"
    return nu_seats


for i in range(5000):
    save_as_png(seats, i, "pt1_frames")
    nu_seats = round(seats)
    if eq(nu_seats, seats):
        result1 = occd(nu_seats)
        break
    seats = nu_seats

seats = seats_part2
for i in range(500000000):
    save_as_png(seats, i, "pt2_frames")
    nu_seats = round2(seats)
    if eq(nu_seats, seats):
        result2 = occd(nu_seats)
        break
    seats = nu_seats

print(result1, result2)