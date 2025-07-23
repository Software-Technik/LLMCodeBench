import sys

def parse_robots(lines):
    robots = []
    for robot in lines:
        parts = robot.split()
        left = parts[0].split(',')
        right = parts[1].split(',')
        Px = int(left[0].split('=')[1])
        Py = int(left[1].split('=')[1])
        Vx = int(right[0].split('=')[1])
        Vy = int(right[1].split('=')[1])
        robots.append((Px, Py, Vx, Vy))
    return robots

def part1(lines):
    WIDE = 101
    TALL = 103
    robots = parse_robots(lines)
    q1 = q2 = q3 = q4 = 0
    vertical_middle = WIDE // 2
    horizontal_middle = TALL // 2
    
    for Px, Py, Vx, Vy in robots:
        new_Px = (Px + Vx * 100) % WIDE
        new_Py = (Py + Vy * 100) % TALL
        
        if new_Px < vertical_middle:
            if new_Py < horizontal_middle:
                q1 += 1
            else:
                q3 += 1
        else:
            if new_Py < horizontal_middle:
                q2 += 1
            else:
                q4 += 1
    
    return q1 * q2 * q3 * q4

def part2(lines):
    WIDE = 101
    TALL = 103
    robots = parse_robots(lines)
    smallest_answer = float('inf')
    found_at_second = 0
    
    for second in range(WIDE * TALL):
        q1 = q2 = q3 = q4 = 0
        vertical_middle = WIDE // 2
        horizontal_middle = TALL // 2
        
        for Px, Py, Vx, Vy in robots:
            new_Px = (Px + Vx * second) % WIDE
            new_Py = (Py + Vy * second) % TALL
            
            if new_Px < vertical_middle:
                if new_Py < horizontal_middle:
                    q1 += 1
                else:
                    q3 += 1
            else:
                if new_Py < horizontal_middle:
                    q2 += 1
                else:
                    q4 += 1
        
        answer = q1 * q2 * q3 * q4
        if answer < smallest_answer:
            smallest_answer = answer
            found_at_second = second
    
    return found_at_second

input_path = sys.argv[1]
with open(input_path, "r") as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))