import numpy as np
from collections import namedtuple, deque
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
            parts = line.strip().split(", ")
            axis["x"] = axis["y"] = None
            for part in parts:
                key = part[0]
                values = list(map(int, part[2:].split("..")))
                axis[key] = (values[0], values[-1])
            x_min = min(x_min, axis["x"][0])
            x_max = max(x_max, axis["x"][1])
            y_min = min(y_min, axis["y"][0])
            y_max = max(y_max, axis["y"][1])
            indices.append(Slice(**axis))

    ground = np.full((y_max+1, x_max - x_min + 3), ".", dtype=str)

    for s in indices:
        x_lower = s.x[0] - x_min + 1
        x_upper = s.x[1] - x_min + 2
        y_lower = s.y[0]
        y_upper = s.y[1] + 1
        ground[y_lower:y_upper, x_lower:x_upper] = "#"
    ground[0, 500 - x_min + 1] = "+"
    return ground, Cursor(0, 500 - x_min + 1), y_min


def waterfall(cursor, ground):
    row = cursor.row + 1
    col = cursor.col
    while row < ground.shape[0] and ground[row, col] == ".":
        row += 1
    if row < ground.shape[0]:
        ground[cursor.row + 1:row, col] = "|"
        if ground[row, col] == "|":
            return None
        return Cursor(row - 1, col)
    else:
        ground[cursor.row + 1:row, col] = "|"
        return None


def spread_water(cursor, ground):
    cursors = set()
    stack = [cursor]
    while stack:
        current = stack.pop()
        new_cursors = fill_water(current, ground)
        if isinstance(new_cursors, tuple):
            if len(new_cursors) == 2:
                stack.extend(new_cursors)
            else:
                cursors.add(new_cursors[0])
        elif new_cursors:
            stack.append(new_cursors[0])
    return cursors


def check_boundaries(cursor, ground):
    row = cursor.row
    col = cursor.col
    left = np.where(ground[row, :col] == "#")[0]
    right = np.where(ground[row, col:] == "#")[0]
    left_boundary = left[-1] if left.size > 0 else -1
    right_boundary = right[0] + col if right.size > 0 else ground.shape[1]
    return Location(left_boundary, right_boundary)


def check_bottom(cursor, ground, boundary):
    row = cursor.row + 1
    left_part = ground[row, boundary.left + 1:cursor.col]
    right_part = ground[row, cursor.col:boundary.right]
    left_closed = np.all(np.isin(left_part, ["#", "~"]))
    right_closed = np.all(np.isin(right_part, ["#", "~"]))
    left_gap = right_gap = None
    if not left_closed:
        left_gap = np.where(left_part != "#")[0][-1] + boundary.left + 1
    if not right_closed:
        right_gap = np.where(right_part != "#")[0][0] + cursor.col
    return Location(left_closed, right_closed), Location(left_gap, right_gap)


def fill_water(cursor, ground):
    boundary = check_boundaries(cursor, ground)
    enclosed, gap = check_bottom(cursor, ground, boundary)
    if enclosed.left and enclosed.right:
        ground[cursor.row, boundary.left + 1:boundary.right] = "~"
        return (Cursor(cursor.row - 1, cursor.col),)
    elif enclosed.left:
        ground[cursor.row, boundary.left + 1:gap.right + 1] = "|"
        return (Cursor(cursor.row, gap.right),)
    elif enclosed.right:
        ground[cursor.row, gap.left:boundary.right] = "|"
        return (Cursor(cursor.row, gap.left),)
    else:
        ground[cursor.row, gap.left:gap.right + 1] = "|"
        return (Cursor(cursor.row, gap.left), Cursor(cursor.row, gap.right))


if __name__ == "__main__":
    input_f = sys.argv[1]
    ground, cursor, y_min = create_array(input_f)
    cursors = deque([cursor])
    while cursors:
        current = cursors.popleft()
        new_cursor = waterfall(current, ground)
        if new_cursor:
            new_cursors = spread_water(new_cursor, ground)
            cursors.extend(new_cursors)
    sys.stdout.write(f"{np.isin(ground[y_min:,:], ['|', '~']).sum()} {(ground[y_min:,:] == '~').sum()}")