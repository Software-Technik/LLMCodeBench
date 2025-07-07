import sys

def parse_robots(lines):
    robots = []
    for robot in lines:
        parts = robot.split()
        Px, Py = map(int, parts[0][3:-1].split(","))
        Vx, Vy = map(int, parts[1][3:].split(","))
        robots.append((Px, Py, Vx, Vy))
    return robots

def calculate_quadrants(robots, seconds, WIDE, TALL):
    count = [0, 0, 0, 0]
    vertical_middle = WIDE // 2
    horizontal_middle = TALL // 2

    for Px, Py, Vx, Vy in robots:
        new_Px = (Px + Vx * seconds) % WIDE
        new_Py = (Py + Vy * seconds) % TALL
        if new_Px < vertical_middle:
            if new_Py < horizontal_middle:
                count[0] += 1
            else:
                count[2] += 1
        else:
            if new_Py < horizontal_middle:
                count[1] += 1
            else:
                count[3] += 1

    return count[0] * count[1] * count[2] * count[3]

def part1(lines):
    WIDE, TALL = 101, 103
    robots = parse_robots(lines)
    return calculate_quadrants(robots, 100, WIDE, TALL)

def part2(lines):
    WIDE, TALL = 101, 103
    robots = parse_robots(lines)
    smallest_answer, found_at_second = float('inf'), 0

    for second in range(WIDE * TALL):
        answer = calculate_quadrants(robots, second, TALL, WIDE)
        if answer < smallest_answer:
            smallest_answer = answer
            found_at_second = second

    return found_at_second

if __name__ == "__main__":
    input_path = sys.argv[1]
    with open(input_path, "r") as file:
        lines = file.readlines()
        print(part1(lines), part2(lines))