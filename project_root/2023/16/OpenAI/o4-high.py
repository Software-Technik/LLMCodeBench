import sys
matrix = open(sys.argv[1]).read().splitlines()
rows = len(matrix)
cols = len(matrix[0]) if rows else 0
dx = (-1,0,1,0)
dy = (0,1,0,-1)
trans = {
    '.':[[0],[1],[2],[3]],
    '|':[[0],[0,2],[2],[0,2]],
    '-':[[3,1],[1],[3,1],[3]],
    '\\':[[3],[2],[1],[0]],
    '/':[[1],[0],[3],[2]],
}
def energize(si,sj,sd):
    beans=set()
    pos_seen=set()
    st=[(si,sj,sd)]
    pop=st.pop; app=st.append
    m=matrix; t=trans; dx0,dy0=dx,dy
    while st:
        i,j,d = pop()
        if not (0<=i<rows and 0<=j<cols): continue
        code = ((i*cols+j)<<2)|d
        if code in beans: continue
        beans.add(code); pos_seen.add(code>>2)
        for nd in t[m[i][j]][d]:
            app((i+dx0[nd], j+dy0[nd], nd))
    return len(pos_seen)
p1 = energize(0,0,1)
p2 = 0
for i in range(rows):
    r = energize(i,0,1)
    if r>p2: p2=r
    r = energize(i,cols-1,3)
    if r>p2: p2=r
for j in range(cols):
    r = energize(0,j,2)
    if r>p2: p2=r
    r = energize(rows-1,j,0)
    if r>p2: p2=r
sys.stdout.write(f"{p1} {p2}")