import sys

def main():
    input_path = sys.argv[1]
    try:
        with open(input_path) as f:
            lines = f.read().splitlines()
    except:
        lines = []

    # Part 1
    ship_x, ship_y = 0, 0
    facing = 0  # 0: East, 90: North, 180: West, 270: South

    for line in lines:
        d = line[0]
        mag = int(line[1:])
        dx, dy = 0, 0
        if d == 'N':
            dy = -mag
        elif d == 'S':
            dy = mag
        elif d == 'W':
            dx = -mag
        elif d == 'E':
            dx = mag
        elif d == 'L':
            facing = (facing + mag) % 360
        elif d == 'R':
            facing = (facing - mag) % 360
        elif d == 'F':
            if facing == 0:
                dx = mag
            elif facing == 90:
                dy = -mag
            elif facing == 180:
                dx = -mag
            elif facing == 270:
                dy = mag
        ship_x += dx
        ship_y += dy

    result1 = abs(ship_x) + abs(ship_y)

    # Part 2
    ship_x, ship_y = 0, 0
    way_x, way_y = 10, -1

    for line in lines:
        d = line[0]
        mag = int(line[1:])
        wdx, wdy = 0, 0
        dx, dy = 0, 0
        if d == 'N':
            way_y -= mag
        elif d == 'S':
            way_y += mag
        elif d == 'W':
            way_x -= mag
        elif d == 'E':
            way_x += mag
        elif d in ['L', 'R']:
            if d == 'R':
                mag = -mag
            mag = mag % 360
            for _ in range(mag // 90):
                way_x, way_y = way_y, -way_x
        elif d == 'F':
            dx = mag * way_x
            dy = mag * way_y
        ship_x += dx
        ship_y += dy
        way_x += wdx
        way_y += wdy

    result2 = abs(ship_x) + abs(ship_y)

    print(result1, result2)

if __name__ == "__main__":
    main()