import sys

def part1(lines):
    grid = []
    moves = []
    for line in lines:
        s = line.rstrip()
        if not s: continue
        if set(s) <= set("<>^v"):
            moves.extend(s)
        else:
            grid.append(list(s))
    h = len(grid); w = len(grid[0])
    robot_row = robot_col = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "@":
                robot_row, robot_col = i, j
    dirs = {"<":(0,-1),">":(0,1),"^":(-1,0),"v":(1,0)}
    def move1(dr,dc):
        r,c = robot_row,robot_col
        r1,c1 = r+dr,c+dc
        cell = grid[r1][c1]
        if cell == ".":
            grid[r][c] = "."
            grid[r1][c1] = "@"
            return True
        if cell == "O":
            k = 1
            while True:
                rr,cc = r+k*dr, c+k*dc
                if grid[rr][cc] == "#": return False
                if grid[rr][cc] == ".":
                    grid[r][c] = "."
                    grid[r+dr][c+dc] = "@"
                    grid[rr][cc] = "O"
                    return True
                k += 1
        return False
    for m in moves:
        dr,dc = dirs[m]
        if move1(dr,dc):
            robot_row += dr; robot_col += dc
    total = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "O":
                total += i*100 + j
    return total

def part2(lines):
    grid0 = []
    moves = []
    for line in lines:
        s = line.rstrip()
        if not s: continue
        if set(s) <= set("<>^v"):
            moves.extend(s)
        else:
            grid0.append(list(s))
    h0 = len(grid0); w0 = len(grid0[0])
    temp = [["."]*(2*w0) for _ in range(h0)]
    robot_row = robot_col = 0
    for i in range(h0):
        for j in range(w0):
            c = grid0[i][j]
            if c == "#":
                temp[i][2*j-1] = temp[i][2*j] = "#"
            elif c == "O":
                temp[i][2*j-1] = "["; temp[i][2*j] = "]"
            elif c == "@":
                temp[i][2*j-1] = "@"; temp[i][2*j] = "."
                robot_row, robot_col = i, 2*j-1
            else:
                temp[i][2*j-1] = temp[i][2*j] = "."
    grid = temp
    h = len(grid); w = len(grid[0])
    dirs = {"<":(0,-1),">":(0,1),"^":(-1,0),"v":(1,0)}
    def find_soulmate(r,c):
        if grid[r][c] == "[": return (r,c+1)
        if grid[r][c] == "]": return (r,c-1)
    def collect(r,c,dr,dc):
        seen = set()
        q = [(r,c)]
        while q:
            cr,cc = q.pop()
            if (cr,cc) in seen: continue
            seen.add((cr,cc))
            sm = find_soulmate(cr,cc)
            if sm and sm not in seen: q.append(sm)
            nr,nc = cr+dr, cc+dc
            if nr<0 or nr>=h or nc<0 or nc>=w: return None
            v = grid[nr][nc]
            if v in "[]":
                if (nr,nc) not in seen: q.append((nr,nc))
            elif v == "#":
                return None
        return list(seen)
    def move2(dr,dc):
        r,c = robot_row,robot_col
        nr,nc = r+dr, c+dc
        v = grid[nr][nc]
        if v == ".":
            grid[r][c] = "."
            grid[nr][nc] = "@"
            return True
        if dr==0 and dc==-1 and v=="]":
            rel = []
            k = 1
            while True:
                rel.append((r, c - k))
                if grid[r][c-k] == "#": return False
                if grid[r][c-k] == ".":
                    grid[r][c] = "."
                    for x,y in rel[::-1]:
                        grid[x][y] = grid[x][y+1]
                    grid[r][c-1] = "@"
                    return True
                k += 1
        if dr==0 and dc==1 and v=="[":
            rel = []
            k = 1
            while True:
                rel.append((r, c + k))
                if grid[r][c+k] == "#": return False
                if grid[r][c+k] == ".":
                    grid[r][c] = "."
                    for x,y in rel[::-1]:
                        grid[x][y] = grid[x][y-1]
                    grid[r][c+1] = "@"
                    return True
                k += 1
        if v in "[]":
            boxes = collect(nr,nc,dr,dc)
            if not boxes: return False
            boxes.sort(reverse=(dr==1))
            for br,bc in boxes:
                grid[br+dr][bc+dc] = grid[br][bc]
                grid[br][bc] = "."
            grid[r][c] = "."
            grid[nr][nc] = "@"
            return True
        return False
    for m in moves:
        dr,dc = dirs[m]
        if move2(dr,dc):
            robot_row += dr; robot_col += dc
    total = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "]":
                total += i*100 + j
    return total

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    print(part1(lines), part2(lines))