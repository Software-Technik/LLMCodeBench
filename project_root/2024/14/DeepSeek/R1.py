import sys

WIDE = 101
TALL = 103

def parse_robots(lines):
    robots = []
    for line in lines:
        clean_line = line.replace('position=<', '').replace('velocity=<', '').replace('>', '').replace(',', ' ').strip()
        tokens = clean_line.split()
        if len(tokens) < 4:
            continue
        try:
            Px = int(tokens[0])
            Py = int(tokens[1])
            Vx = int(tokens[2])
            Vy = int(tokens[3])
        except:
            continue
        robots.append([Px, Py, Vx, Vy])
    return robots

def part1(robots):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    vertical_middle = WIDE // 2
    horizontal_middle = TALL // 2
    for bot in robots:
        Px, Py, Vx, Vy = bot
        new_Px = (Px + Vx * 100) % WIDE
        new_Py = (Py + Vy * 100) % TALL
        if new_Px < vertical_middle and new_Py < horizontal_middle:
            q1 += 1
        if new_Px > vertical_middle and new_Py < horizontal_middle:
            q2 += 1
        if new_Px < vertical_middle and new_Py > horizontal_middle:
            q3 += 1
        if new_Px > vertical_middle and new_Py > horizontal_middle:
            q4 += 1
    return q1 * q2 * q3 * q4

def part2(robots):
    smallest_answer = float('inf')
    found_at_second = 0
    vertical_middle = WIDE // 2
    horizontal_middle = TALL // 2
    for second in range(WIDE * TALL):
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for bot in robots:
            Px, Py, Vx, Vy = bot
            new_Py = (Px + Vx * second) % WIDE
            new_Px = (Py + Vy * second) % TALL
            if new_Px < vertical_middle and new_Py < horizontal_middle:
                q1 += 1
            if new_Px > vertical_middle and new_Py < horizontal_middle:
                q2 += 1
            if new_Px < vertical_middle and new_Py > horizontal_middle:
                q3 += 1
            if new_Px > vertical_middle and new_Py > horizontal_middle:
                q4 += 1
        answer = q1 * q2 * q3 * q4
        if answer < smallest_answer:
            smallest_answer = answer
            found_at_second = second
    return found_at_second

input_path = sys.argv[1]
with open(input_path, "r") as file:
    lines = file.readlines()
    robots = parse_robots(lines)
    print(part1(robots), part2(robots))