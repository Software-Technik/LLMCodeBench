import sys
from collections import deque

def parse():
    data = open(sys.argv[1]).read().split('\n\n',1)
    grid_lines = data[0].splitlines()
    moves_line = data[1].splitlines()[0]
    grid = [list(row) for row in grid_lines]
    moves = list(moves_line.strip())
    return grid, moves

def part1(grid0, moves):
    H, W = len(grid0), len(grid0[0])
    grid = [row.copy() for row in grid0]
    for i in range(H):
        for j in range(W):
            if grid[i][j]=='@':
                rr, cc = i, j
                break
    dirs = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}
    for m in moves:
        dr, dc = dirs[m]
        nr, nc = rr+dr, cc+dc
        cell = grid[nr][nc]
        if cell=='.':
            grid[rr][cc]='.'
            grid[nr][nc]='@'
            rr, cc = nr, nc
        elif cell=='O':
            d = 1
            while grid[rr+dr*(d+1)][cc+dc*(d+1)]=='O':
                d += 1
            er, ec = rr+dr*(d+1), cc+dc*(d+1)
            if grid[er][ec]=='.':
                grid[rr][cc]='.'
                grid[nr][nc]='@'
                grid[er][ec]='O'
                rr, cc = nr, nc
    total = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j]=='O':
                total += i*100 + j
    return total

def part2(grid0, moves):
    H, W = len(grid0), len(grid0[0])
    grid = []
    for i in range(H):
        row = []
        for c in grid0[i]:
            if c=='#': row+=['#','#']
            elif c=='.': row+=['.','.']
            elif c=='O': row+=['[',']']
            elif c=='@': row+=['@','.']
        grid.append(row)
    W2 = W*2
    for i in range(H):
        for j in range(W2):
            if grid[i][j]=='@':
                rr, cc = i, j
                break
    dirs = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}
    brackets = {'[',']'}
    for m in moves:
        dr, dc = dirs[m]
        nr, nc = rr+dr, cc+dc
        cell = grid[nr][nc]
        if cell=='.':
            grid[rr][cc]='.'
            grid[nr][nc]='@'
            rr, cc = nr, nc
        elif dr==0 and dc!=0 and cell in brackets:
            if dc==1 and cell!='[': continue
            if dc==-1 and cell!=']': continue
            seg = []
            cpos = nc
            while 0<=cpos<W2 and grid[nr][cpos] in brackets:
                seg.append(cpos)
                cpos += dc
            dest = seg[-1] + dc
            if grid[nr][dest]!='.': continue
            grid[rr][cc]='.'
            for cpos in reversed(seg):
                grid[nr][cpos+dc] = grid[nr][cpos]
            grid[nr][nc]='@'
            rr, cc = nr, nc
        elif dr!=0 and cell in brackets:
            visited = set()
            queue = deque([(nr,nc)])
            ok = True
            while queue:
                r, c = queue.popleft()
                if (r,c) in visited: continue
                visited.add((r,c))
                if grid[r][c]=='[' and c+1<W2:
                    queue.append((r,c+1))
                elif grid[r][c]==']' and c-1>=0:
                    queue.append((r,c-1))
                r2, c2 = r+dr, c+dc
                ch = grid[r2][c2]
                if ch=='#':
                    ok = False
                    break
                if ch in brackets:
                    queue.append((r2,c2))
            if not ok: continue
            boxes = sorted(visited, key=lambda x: x[0], reverse=(dr>0))
            for r, c in boxes:
                grid[r+dr][c+dc] = grid[r][c]
                grid[r][c] = '.'
            grid[rr][cc]='.'
            grid[nr][nc]='@'
            rr, cc = nr, nc
    total = 0
    for i in range(H):
        for j in range(W2):
            if grid[i][j]==']':
                total += i*100 + j
    return total

def main():
    grid, moves = parse()
    print(part1(grid, moves), part2(grid, moves))

if __name__=='__main__':
    main()