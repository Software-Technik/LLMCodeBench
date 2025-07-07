import sys

def main():
    with open(sys.argv[1]) as f:
        s = f.read().strip()
    x = y = 0
    visited = {(0, 0)}
    for c in s:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '<':
            x -= 1
        else:
            x += 1
        visited.add((x, y))
    p1 = len(visited)
    x0 = y0 = x1 = y1 = 0
    visited2 = {(0, 0)}
    turn = True
    for c in s:
        if c == '^':
            dx, dy = 0, 1
        elif c == 'v':
            dx, dy = 0, -1
        elif c == '<':
            dx, dy = -1, 0
        else:
            dx, dy = 1, 0
        if turn:
            x0 += dx
            y0 += dy
            visited2.add((x0, y0))
        else:
            x1 += dx
            y1 += dy
            visited2.add((x1, y1))
        turn = not turn
    p2 = len(visited2)
    sys.stdout.write(f"{p1}\n{p2}\n")

if __name__ == '__main__':
    main()