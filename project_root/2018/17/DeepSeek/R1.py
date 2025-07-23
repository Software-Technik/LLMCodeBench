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
            axis = {"x": None, "y": None}
            for part in line.strip().split(", "):
                key = part[0]
                values = part[2:].split("..")
                if len(values) == 1:
                    axis[key] = (int(values[0]), int(values[0]))
                else:
                    axis[key] = (int(values[0]), int(values[1]))
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
    row = water_startpoint
    finite = True
    while row < ground.shape[0]:
        if ground[row, cursor.col] in ['#', '~', '|']:
            break
        row += 1
    else:
        finite = False

    if finite:
        water_endpoint = row
        ground[water_startpoint:water_endpoint, cursor.col] = "|"
        if ground[water_endpoint, cursor.col] == '|':
            return None
        cursor = Cursor(water_endpoint - 1, cursor.col)
    else:
        if water_startpoint < ground.shape[0]:
            ground[water_startpoint:, cursor.col] = "|"
        cursor = None
    return cursor


def spread_water(cursor, ground):
    done = False
    while not done:
        cursor, done = fill_water(cursor, ground)
    return cursor


def check_boundaries(cursor, ground):
    left_boundary = 0
    col = cursor.col - 1
    while col >= 0:
        if ground[cursor.row, col] == '#':
            left_boundary = col
            break
        col -= 1
    else:
        left_boundary = 0

    right_boundary = ground.shape[1]
    col = cursor.col + 1
    while col < ground.shape[1]:
        if ground[cursor.row, col] == '#':
            right_boundary = col
            break
        col += 1
    else:
        right_boundary = ground.shape[1]

    return Location(left_boundary, right_boundary)


def check_bottom(cursor, ground, boundary):
    left_closed = True
    left_gap = None
    for col in range(cursor.col-1, boundary.left, -1):
        if ground[cursor.row+1, col] not in ['#','~']:
            left_closed = False
            left_gap = col
            break

    right_closed = True
    right_gap = None
    for col in range(cursor.col, boundary.right):
        if ground[cursor.row+1, col] not in ['#','~']:
            right_closed = False
            right_gap = col
            break

    return Location(left_closed, right_closed), Location(left_gap, right_gap)


def fill_water(cursor, ground):
    boundary = check_boundaries(cursor, ground)
    enclosed, gap = check_bottom(cursor, ground, boundary)

    if enclosed.left and enclosed.right:
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

    cursors = set([cursor])
    while cursors:
        cursor = cursors.pop()

        cursor = waterfall(cursor, ground)

        if cursor:
            cursor = spread_water(cursor, ground)
            if isinstance(cursor, tuple):
                cursors.update(cursor)
            else:
                cursors.add(cursor)

    sys.stdout.write(f"{np.isin(ground[y_min:,:], ['|', '~']).sum()} {(ground[y_min:,:] == '~').sum()}")