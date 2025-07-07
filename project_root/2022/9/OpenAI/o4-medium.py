import sys

def main():
    f = open(sys.argv[1])
    knots1 = [[0, 0], [0, 0]]
    knots2 = [[0, 0] for _ in range(10)]
    pos1 = {(0, 0)}
    pos2 = {(0, 0)}
    pos1_add = pos1.add
    pos2_add = pos2.add

    for line in f:
        c = line[0]
        n = int(line[2:])
        if c == 'R':
            dx0, dy0 = 1, 0
        elif c == 'L':
            dx0, dy0 = -1, 0
        elif c == 'U':
            dx0, dy0 = 0, -1
        else:
            dx0, dy0 = 0, 1
        for _ in range(n):
            # rope1
            k1 = knots1
            k1[0][0] += dx0; k1[0][1] += dy0
            w = k1[0][0] - k1[1][0]; h = k1[0][1] - k1[1][1]
            if w == 2 or w == -2 or h == 2 or h == -2:
                dx = 1 if w > 0 else -1 if w < 0 else 0
                dy = 1 if h > 0 else -1 if h < 0 else 0
                k1[1][0] += dx; k1[1][1] += dy
            pos1_add((k1[1][0], k1[1][1]))
            # rope2
            k2 = knots2
            k2[0][0] += dx0; k2[0][1] += dy0
            for i in range(9):
                w = k2[i][0] - k2[i+1][0]; h = k2[i][1] - k2[i+1][1]
                if w == 2 or w == -2 or h == 2 or h == -2:
                    dx = 1 if w > 0 else -1 if w < 0 else 0
                    dy = 1 if h > 0 else -1 if h < 0 else 0
                    k2[i+1][0] += dx; k2[i+1][1] += dy
            pos2_add((k2[9][0], k2[9][1]))

    sys.stdout.write(str(len(pos1)) + "\n" + str(len(pos2)) + "\n")

if __name__ == '__main__':
    main()