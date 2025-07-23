import sys

def main():
    with open(sys.argv[1]) as f:
        instructions = [line.strip() for line in f]

    size = len(instructions)
    mid = size // 2
    grid1 = {}
    grid2 = {}

    for i in range(size):
        line = instructions[i]
        for j in range(size):
            if line[j] == '#':
                grid1[(i, j)] = 1
                grid2[(i, j)] = 2

    def turn(direction, rotation):
        x, y = direction
        if rotation == "left":
            return (-y, x)
        elif rotation == "right":
            return (y, -x)
        elif rotation == "back":
            return (-x, -y)
        return direction

    def part1():
        direction = (-1, 0)
        position = (mid, mid)
        infections = 0
        grid = grid1.copy()

        for _ in range(10000):
            status = grid.get(position, 0)
            if status == 0:
                direction = turn(direction, "left")
                grid[position] = 1
                infections += 1
            else:
                direction = turn(direction, "right")
                grid[position] = 0
            position = (position[0] + direction[0], position[1] + direction[1])

        return infections

    def part2():
        direction = (-1, 0)
        position = (mid, mid)
        infections = 0
        grid = grid2.copy()

        for _ in range(10000000):
            status = grid.get(position, 0)
            if status == 0:
                direction = turn(direction, "left")
            elif status == 1:
                infections += 1
            elif status == 2:
                direction = turn(direction, "right")
            elif status == 3:
                direction = turn(direction, "back")
            grid[position] = (status + 1) % 4
            position = (position[0] + direction[0], position[1] + direction[1])

        return infections

    print(part1())
    print(part2())

if __name__ == "__main__":
    main()