import numpy as np
from collections import namedtuple
import sys

Slice = namedtuple("Slice", ["x", "y"])
Cursor = namedtuple("Cursor", ["row", "col"])
Location = namedtuple("Location", ["left", "right"])

def create_array(fn):
    axis = {"x": None, "y": None}
    x_min = y_min = float('inf')
    x_max = y_max = -float('inf')
    indices = []

    with open(fn) as f:
        for line in f:
            for part in line.strip().split(", "):
                splice = part[2:].split("..")
                axis[part[0]] = (int(splice[0]), int(splice[-1]))
            x_min = min(axis["x"][0], x_min)
            x_max = max(axis["x"][1], x_max)
            y_min = min(axis["y"][0], y_min)
            y_max = max(axis["y"][1], y_max)
            indices.append(Slice(**axis))

    ground = np.full((y_max+1, x_max - x_min + 3), '.', dtype=str)

    for s in indices:
        x_lower = s.x[0] - x_min + 1
        x_upper = s.x[1] - x_min + 2
        y_lower = s.y[0]
        y_upper = s.y[1] + 1
        ground[y_lower:y_upper, x_lower:x_upper] = "#"
    ground[0][500 + 1 - x_min] = "+"
    return ground, Cursor(0, 500 + 1 - x_min), y_min

def waterfall(cursor, ground):
    water_startpoint = cursor.row + 1
    find_endpoint = np.isin(ground[water_startpoint:, cursor.col], ["#", "~", "|"])
    endpoint = np.argmax(find_endpoint)
    finite = find_endpoint[endpoint] if endpoint != 0 else False
    water_endpoint = endpoint + water_startpoint if finite else ground.shape[0] + 3

    ground[water_startpoint:water_endpoint, cursor.col] = "|"
    if not finite or ground[water_endpoint, cursor.col] == "|":
        return None

    return Cursor(water_endpoint - 1, cursor.col) if finite else None

def spread_water(cursor, ground):
    done = False
    while not done:
        cursor, done = fill_water(cursor, ground)
    return cursor

def check_boundaries(cursor, ground):
    clay_left = np.where(ground[cursor.row, :cursor.col] == "#")[0]
    clay_right = np.where(ground[cursor.row, cursor.col:] == "#")[0]

    left_boundary = clay_left.max() if clay_left.size else 0
    right_boundary = clay_right.min() + cursor.col if clay_right.size else ground.shape[1]

    return Location(left_boundary, right_boundary)

def check_bottom(cursor, ground, boundary):
    left_bottom = np.isin(ground[cursor.row + 1, boundary.left:cursor.col], ["#", "~"])
    right_bottom = np.isin(ground[cursor.row + 1, cursor.col:(boundary.right+1)], ["#", "~"])

    left_closed = np.all(left_bottom)
    right_closed = np.all(right_bottom)

    left_gap = np.where(~left_bottom)[0].max() + boundary.left if not left_closed else None
    right_gap = np.where(~right_bottom)[0].min() + cursor.col if not right_closed else None
    return Location(left_closed, right_closed), Location(left_gap, right_gap)

def fill_water(cursor, ground):
    boundary = check_boundaries(cursor, ground)
    enclosed, gap = check_bottom(cursor, ground, boundary)

    if all(enclosed):
        ground[cursor.row, boundary.left + 1:boundary.right] = "~"
        return Cursor(cursor.row - 1, cursor.col), False
    elif enclosed.left:
        ground[cursor.row, boundary.left+1:gap.right+1] = "|"
        return (Cursor(cursor.row, gap.right), ), True
    elif enclosed.right:
        ground[cursor.row, gap.left:boundary.right] = "|"
        return (Cursor(cursor.row, gap.left), ), True
    else:
        ground[cursor.row, gap.left:gap.right+1] = "|"
        return (Cursor(cursor.row, gap.left), Cursor(cursor.row, gap.right)), True

if __name__ == "__main__":
    input_f = sys.argv[1]
    ground, cursor, y_min = create_array(input_f)

    cursors = {cursor}
    while cursors:
        cursor = cursors.pop()
        cursor = waterfall(cursor, ground)

        if cursor:
            cursor = spread_water(cursor, ground)
            if cursor:
                cursors.update(cursor)

    print(np.isin(ground[y_min:], ['|', '~']).sum(), (ground[y_min:] == '~').sum())