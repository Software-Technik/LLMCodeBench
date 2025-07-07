import sys

WIDE = 101
TALL = 103
VM = WIDE // 2
HM = TALL // 2

def get_num(s):
    return int(s.split('=')[-1])

def parse(lines):
    robots = []
    for line in lines:
        a, b = line.split()
        x_s, y_s = a.split(','), b.split(',')
        robots.append((get_num(x_s[0]), get_num(x_s[1]), get_num(y_s[0]), get_num(y_s[1])))
    return robots

def part1(robots):
    q1 = q2 = q3 = q4 = 0
    for x, y, vx, vy in robots:
        nx = (x + vx * 100) % WIDE
        ny = (y + vy * 100) % TALL
        if nx < VM and ny < HM:
            q1 += 1
        elif nx > VM and ny < HM:
            q2 += 1
        elif nx < VM and ny > HM:
            q3 += 1
        elif nx > VM and ny > HM:
            q4 += 1
    return q1 * q2 * q3 * q4

def part2(robots):
    best = float('inf')
    ans = 0
    for t in range(WIDE * TALL):
        q1 = q2 = q3 = q4 = 0
        for x, y, vx, vy in robots:
            tmp_py = x + vx * t
            tmp_px = y + vy * t
            new_px = tmp_px % TALL
            new_py = tmp_py % WIDE
            if new_px < VM and new_py < HM:
                q1 += 1
            elif new_px > VM and new_py < HM:
                q2 += 1
            elif new_px < VM and new_py > HM:
                q3 += 1
            elif new_px > VM and new_py > HM:
                q4 += 1
        prod = q1 * q2 * q3 * q4
        if prod < best:
            best = prod
            ans = t
    return ans

if __name__ == '__main__':
    lines = open(sys.argv[1]).read().splitlines()
    robots = parse(lines)
    print(part1(robots), part2(robots))