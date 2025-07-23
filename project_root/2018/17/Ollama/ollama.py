import numpy as np
from collections import namedtuple
import sys

Slice = namedtuple("Slice", ["x", "y"])
Cursor = namedtuple("Cursor", ["row", "col"])
Location = namedtuple("Location", ["left", "right"])

def create_array(fn):
    axis = {"x": None, "y": None}
    x_min = y_min = np.inf
    x_max = y_max = -np.inf
    indices = []

    with open(fn) as f:
        for line in f:
            for part in line.strip().split(", "):
                splice = part[2:].split("..")
                axis[part[0]] = (int(splice[0]), int(splice[-1]))
            x_min = min(x_min, axis["x"][0])
            x_max = max(x_max, axis["x"][1])
            y_min = min(y_min, axis["y"][0])
            y_max = max(y_max, axis["y"][1])
            indices.append(Slice(**axis))

    ground = np.full((y_max+1, x_max - x_min + 3), fill_value=".", dtype=str)
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
    endpoint = np.where(find_endpoint)[0]
    if endpoint.size > 0:
        water_endpoint = endpoint[0] + water_startpoint
        finite = True
    else:
        water_endpoint = ground.shape[0] + 3
        finite = False

    ground[water_startpoint:water_endpoint, cursor.col] = "|"
    if finite and ground[water_endpoint, cursor.col] == "|":
        return None

    cursor = Cursor(water_endpoint - 1, cursor.col) if finite else None
    return cursor

def spread_water(cursor, ground):
    done = False
    while not done:
        cursors = fill_water(cursor, ground)
        if len(cursors) == 1 and cursors[0] is None:
            done = True
            continue
        cursor = cursors[0]
        cursors.pop(0)
        for c in cursors: spread_water(c, ground)
    return cursor

def check_boundaries(cursor, ground):
    clay_left = np.where(ground[cursor.row, :cursor.col] == "#")[0]
    clay_right = np.where(ground[cursor.row, cursor.col:] == "#")[0]

    left_boundary = 0 if not clay_left.size else clay_left.max()
    right_boundary = ground.shape[1] if not clay_right.size else clay_right.min() + cursor.col

    return Location(left_boundary, right_boundary)

def check_bottom(cursor, ground, boundary):
    left_bottom = np.isin(ground[cursor.row + 1, boundary.left:cursor.col], ["#", "~"])
    right_bottom = np.isin(ground[cursor.row + 1, cursor.col:(boundary.right+1)], ["#", "~"])

    left_closed = np.all(left_bottom)
    right_closed = np.all(right_bottom)

    left_gap = np.where(np.logical_not(left_closed), np.argmax(np.logical_not(left_bottom)) + boundary.left, None)[0]
    right_gap = np.where(np.logical_not(right_closed), np.argmin(np.logical_not(right_bottom)) + cursor.col, None)[0]

    return Location(left_closed, right_closed), Location(left_gap, right_gap)

def fill_water(cursor, ground):
    boundary = check_boundaries(cursor, ground)
    enclosed, gap = check_bottom(cursor, ground, boundary)

    if all(enclosed): ground[cursor.row, boundary.left + 1:boundary.right] = "~"
    elif enclosed.left: ground[cursor.row, boundary.left+1:gap.right+1] = "|"; return (Cursor(cursor.row, gap[0]),), True
    elif enclosed.right: ground[cursor.row, gap.left:boundary.right] = "|"; return (Cursor(cursor.row, gap[0]),), True
    else: ground[cursor.row, gap.left:gap.right+1] = "|"
    return (Cursor(cursor.row - 1, cursor.col) if all(enclosed) else Cursor(cursor.row, gap[0])), False

if __name__ == "__main__":
    input_f = sys.argv[1]
    ground, cursor, y_min = create_array(input_f)

    cursors = [cursor]
    while cursors:
        cursor = cursors.pop(0)
        cursor = waterfall(cursor, ground)
        if cursor is not None: cursors.append(cursors.pop(spread_water(cursor, ground)))

    sys.stdout.write(f"{np.isin(ground[y_min:,:], ['|', '~']).sum()} {(ground[y_min:,:] == '~').sum()})")