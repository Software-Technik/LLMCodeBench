import png
import copy
import os
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

line_groups = data.split("\n\n")

result1 = 0
result2 = 0

L, I, D, S = list, int, dict, set

def line_transform(line):
    return [c for c in line]

seats = [line_transform(line) for line in lines]
seats_part2 = copy.deepcopy(seats)

def adjacent(_seats, x, y):
    adj = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            yy, xx = y + dy, x + dx
            if 0 <= yy < len(_seats) and 0 <= xx < len(_seats[0]) and _seats[yy][xx] == "#":
                adj += 1
    return adj

def save_as_png(arrs, idx, folder):
    trans = {"L": 0, ".": 150, "#": 255}
    _arrs = copy.deepcopy(arrs)
    for y in range(len(arrs)):
        for x in range(len(arrs[0])):
            _arrs[y][x] = trans[arrs[y][x]]
    if not os.path.exists(folder):
        os.mkdir(folder)
    outfile = os.path.join(folder, f"{idx:05}.png")
    png.from_array(_arrs, "L").save(outfile)

def occd(seats):
    return sum(row.count("#") for row in seats)

def eq(s1, s2):
    return all(s1[y][x] == s2[y][x] for y in range(len(s1)) for x in range(len(s1[0])))

def round(_seats):
    nu_seats = copy.deepcopy(_seats)
    for y in range(len(_seats)):
        for x in range(len(_seats[0])):
            adj = adjacent(_seats, x, y)
            cur = _seats[y][x]
            if cur == ".":
                continue
            if cur == "L" and adj == 0:
                nu_seats[y][x] = "#"
            if cur == "#" and adj >= 4:
                nu_seats[y][x] = "L"
    return nu_seats

for i in range(5000):
    save_as_png(seats, i, "pt1_frames")
    nu_seats = round(seats)
    if eq(nu_seats, seats):
        result1 = occd(nu_seats)
        break
    seats = nu_seats

def visible(_seats, x, y):
    adj = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            step = 1
            yy, xx = y + dy * step, x + dx * step
            seen = False
            while 0 <= yy < len(_seats) and 0 <= xx < len(_seats[0]) and not seen:
                if _seats[yy][xx] == "#":
                    adj += 1
                    seen = True
                elif _seats[yy][xx] == "L":
                    seen = True
                step += 1
                yy, xx = y + dy * step, x + dx * step
    return adj

def round2(_seats):
    nu_seats = copy.deepcopy(_seats)
    for y in range(len(_seats)):
        for x in range(len(_seats[0])):
            adj = visible(_seats, x, y)
            cur = _seats[y][x]
            if cur == ".":
                continue
            if cur == "L" and adj == 0:
                nu_seats[y][x] = "#"
            if cur == "#" and adj >= 5:
                nu_seats[y][x] = "L"
    return nu_seats

seats = seats_part2
for i in range(5000):
    save_as_png(seats, i, "pt2_frames")
    nu_seats = round2(seats)
    if eq(nu_seats, seats):
        result2 = occd(nu_seats)
        break
    seats = nu_seats

print(result1, result2)