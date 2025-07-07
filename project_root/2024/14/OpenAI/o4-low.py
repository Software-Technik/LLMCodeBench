import sys

def parse(lines):
    robots = []
    for line in lines:
        left, right = line.split()
        px, py = left.split(",")
        vx, vy = right.split(",")
        robots.append((int(px.split("=")[1]), int(py), int(vx.split("=")[1]), int(vy)))
    return robots

def part1(robots):
    W, H = 101, 103
    vm, hm = W//2, H//2
    q1 = q2 = q3 = q4 = 0
    for px, py, vx, vy in robots:
        x = (px + vx*100) % W
        y = (py + vy*100) % H
        if x<vm and y<hm: q1+=1
        if x>vm and y<hm: q2+=1
        if x<vm and y>hm: q3+=1
        if x>vm and y>hm: q4+=1
    return q1*q2*q3*q4

def part2(robots):
    W, H = 101, 103
    vm, hm = W//2, H//2
    best_s = 0
    best = 10**18
    for s in range(W*H):
        q1 = q2 = q3 = q4 = 0
        for px, py, vx, vy in robots:
            nx = (px + vx*s) % H
            ny = (py + vy*s) % W
            if nx<vm and ny<hm: q1+=1
            if nx>vm and ny<hm: q2+=1
            if nx<vm and ny>hm: q3+=1
            if nx>vm and ny>hm: q4+=1
        val = q1*q2*q3*q4
        if val<best:
            best = val
            best_s = s
    return best_s

lines = open(sys.argv[1]).read().splitlines()
robots = parse(lines)
print(part1(robots), part2(robots))