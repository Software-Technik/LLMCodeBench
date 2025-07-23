import sys

def parse_robot(robot):
    sides = robot.split(" ")
    Px, Py = map(int, [sides[0].split(",")[0].split("=")[-1], sides[0].split(",")[1]])
    Vx, Vy = map(int, [sides[1].split(",")[0].split("=")[-1], sides[1].split(",")[1]])
    return Px, Py, Vx, Vy

def get_result(robots, second):
    q1 = q2 = q3 = q4 = 0
    WIDE = 101
    TALL = 103
    vertical_middle = WIDE // 2
    horizontal_middle = TALL // 2

    for Px, Py, Vx, Vy in robots:
        new_Px = (Px + Vx * second) % WIDE
        new_Py = (Py + Vy * second) % TALL

        if new_Px < vertical_middle and new_Py < horizontal_middle:
            q1 += 1
        elif new_Px > vertical_middle and new_Py < horizontal_middle:
            q2 += 1
        elif new_Px < vertical_middle and new_Py > horizontal_middle:
            q3 += 1
        else:
            q4 += 1

    return q1 * q2 * q3 * q4, second

def part1(lines):
    robots = [parse_robot(robot) for robot in lines]
    return get_result(robots, 100)[0]

def part2(lines):
    robots = [parse_robot(robot) for robot in lines]
    smallest_answer = float('inf')
    found_at_second = 0
    WIDE = 101
    TALL = 103

    for second in range(WIDE * TALL):
        answer = get_result(robots, second)[0]
        if answer < smallest_answer:
            smallest_answer = answer
            found_at_second = second

    return found_at_second

input_path = sys.argv[1]

with open(input_path, "r") as file:
    lines = file.readlines()

print(part1(lines), part2(lines))