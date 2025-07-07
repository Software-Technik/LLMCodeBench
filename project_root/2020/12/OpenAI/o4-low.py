import sys

def main():
    with open(sys.argv[1]) as f:
        lines = [(l[0], int(l[1:])) for l in f.read().splitlines()]

    # Part 1
    x = y = 0
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]  # E,S,W,N
    d = 0
    for cmd, v in lines:
        if cmd == 'N': y -= v
        elif cmd == 'S': y += v
        elif cmd == 'E': x += v
        elif cmd == 'W': x -= v
        elif cmd == 'L': d = (d - v//90) % 4
        elif cmd == 'R': d = (d + v//90) % 4
        elif cmd == 'F':
            dx, dy = dirs[d]
            x += dx*v; y += dy*v
    res1 = abs(x) + abs(y)

    # Part 2
    sx = sy = 0
    wx, wy = 10, -1
    for cmd, v in lines:
        if cmd == 'N': wy -= v
        elif cmd == 'S': wy += v
        elif cmd == 'E': wx += v
        elif cmd == 'W': wx -= v
        elif cmd in ('L','R'):
            t = (v//90)%4
            if cmd == 'L': t = (4-t)%4
            for _ in range(t):
                wx, wy = wy, -wx
        elif cmd == 'F':
            sx += wx*v; sy += wy*v
    res2 = abs(sx) + abs(sy)

    print(res1, res2)

if __name__ == "__main__":
    main()