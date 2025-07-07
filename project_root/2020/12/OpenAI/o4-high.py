import sys
dirs = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
x1 = y1 = x2 = y2 = 0
wx, wy = 10, -1
facing = 0
with open(sys.argv[1]) as f:
    for l in f:
        d = l[0]; m = int(l[1:])
        if d in dirs:
            dx, dy = dirs[d]
            x1 += dx*m; y1 += dy*m
            wx += dx*m; wy += dy*m
        elif d == 'L':
            k = (m//90) & 3
            facing = (facing - k) & 3
            if k == 1:
                wx, wy = -wy, wx
            elif k == 2:
                wx, wy = -wx, -wy
            elif k == 3:
                wx, wy = wy, -wx
        elif d == 'R':
            k = (m//90) & 3
            facing = (facing + k) & 3
            if k == 1:
                wx, wy = wy, -wx
            elif k == 2:
                wx, wy = -wx, -wy
            elif k == 3:
                wx, wy = -wy, wx
        else:
            x1 += dxs[facing]*m; y1 += dys[facing]*m
            x2 += wx*m; y2 += wy*m
print(abs(x1)+abs(y1), abs(x2)+abs(y2))