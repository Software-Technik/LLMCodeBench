import sys
def main():
    text = open(sys.argv[1]).read()
    matrix = [list(line) for line in text.splitlines()]
    n = len(matrix)
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    TRANS = [[[[] for _ in range(4)] for _ in row] for row in matrix]
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            for d in range(4):
                if c == '.':
                    k, l = i, j
                    while True:
                        k += dx[d]; l += dy[d]
                        if k < 0 or k >= n or l < 0 or l >= len(matrix[k]): break
                        if matrix[k][l] != '.': break
                    if 0 <= k < n and 0 <= l < len(matrix[k]):
                        TRANS[i][j][d].append((k, l, d))
                elif c == '|':
                    if d in (1, 3):
                        for nd in (0, 2):
                            ni, nj = i + dx[nd], j + dy[nd]
                            if 0 <= ni < n and 0 <= nj < len(matrix[ni]):
                                TRANS[i][j][d].append((ni, nj, nd))
                    else:
                        ni, nj = i + dx[d], j + dy[d]
                        if 0 <= ni < n and 0 <= nj < len(matrix[ni]):
                            TRANS[i][j][d].append((ni, nj, d))
                elif c == '-':
                    if d in (0, 2):
                        for nd in (1, 3):
                            ni, nj = i + dx[nd], j + dy[nd]
                            if 0 <= ni < n and 0 <= nj < len(matrix[ni]):
                                TRANS[i][j][d].append((ni, nj, nd))
                    else:
                        ni, nj = i + dx[d], j + dy[d]
                        if 0 <= ni < n and 0 <= nj < len(matrix[ni]):
                            TRANS[i][j][d].append((ni, nj, d))
                elif c == '\\':
                    nd = (3,2,1,0)[d]
                    ni, nj = i + dx[nd], j + dy[nd]
                    if 0 <= ni < n and 0 <= nj < len(matrix[ni]):
                        TRANS[i][j][d].append((ni, nj, nd))
                elif c == '/':
                    nd = (1,0,3,2)[d]
                    ni, nj = i + dx[nd], j + dy[nd]
                    if 0 <= ni < n and 0 <= nj < len(matrix[ni]):
                        TRANS[i][j][d].append((ni, nj, nd))
    def traverse(si, sj, sd):
        visited = [[[False]*4 for _ in row] for row in matrix]
        seen = [[False]*len(row) for row in matrix]
        cnt = 0
        stack = [(si, sj, sd)]
        while stack:
            i, j, d = stack.pop()
            if i < 0 or i >= n or j < 0 or j >= len(matrix[i]): continue
            if visited[i][j][d]: continue
            visited[i][j][d] = True
            if not seen[i][j]:
                pass
            if not seen[i][j]:
                seen[i][j] = True
                cnt += 1
            for ni, nj, nd in TRANS[i][j][d]:
                if not visited[ni][nj][nd]:
                    stack.append((ni, nj, nd))
        return cnt
    p1 = traverse(0, 0, 1)
    p2 = 0
    for i in range(n):
        p2 = max(p2, traverse(i, 0, 1), traverse(i, len(matrix[i]) - 1, 3))
    m0 = len(matrix[0])
    for j in range(m0):
        p2 = max(p2, traverse(0, j, 2), traverse(n-1, j, 0))
    sys.stdout.write(f"{p1} {p2}")
if __name__ == "__main__":
    main()