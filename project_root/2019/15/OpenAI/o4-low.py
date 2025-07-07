import sys
from collections import defaultdict, deque

def runComputer(data, inp):
    prog = defaultdict(int, enumerate(data))
    i = 0
    rel = 0
    while True:
        op = prog[i] % 100
        if op == 99:
            return
        m1 = prog[i]//100%10; m2 = prog[i]//1000%10; m3 = prog[i]//10000%10
        def arg(n,m):
            if m==0: return prog[i+n]
            if m==1: return i+n
            return prog[i+n]+rel
        if op in (1,2,7,8):
            a1=arg(1,m1); a2=arg(2,m2); a3=arg(3,m3)
            if op==1: prog[a3]=prog[a1]+prog[a2]
            elif op==2: prog[a3]=prog[a1]*prog[a2]
            elif op==7: prog[a3]=int(prog[a1]<prog[a2])
            else: prog[a3]=int(prog[a1]==prog[a2])
            i+=4
        elif op==3:
            a1=arg(1,m1)
            prog[a1]=inp.pop()
            i+=2
        elif op==4:
            a1=arg(1,m1)
            yield prog[a1]
            i+=2
        elif op in (5,6):
            a1=arg(1,m1); a2=arg(2,m2)
            if (op==5 and prog[a1]!=0) or (op==6 and prog[a1]==0):
                i=prog[a2]
            else:
                i+=3
        elif op==9:
            a1=arg(1,m1)
            rel+=prog[a1]
            i+=2

N, S, W, E = 1,2,3,4
dx = {N:0,S:0,W:-1,E:1}
dy = {N:-1,S:1,W:0,E:0}
opp = {N:S,S:N,W:E,E:W}

def solve(data):
    inp = []
    runner = runComputer(data, inp)
    m = {(0,0):1}
    goal = None
    def dfs(x,y):
        nonlocal goal
        for d in (N,S,W,E):
            nx, ny = x+dx[d], y+dy[d]
            if (nx,ny) not in m:
                inp.append(d)
                status = next(runner)
                m[(nx,ny)] = status
                if status:
                    if status==2: goal=(nx,ny)
                    dfs(nx,ny)
                    inp.append(opp[d]); next(runner)
    dfs(0,0)
    def bfs(start):
        q=deque([(start,0)])
        seen={start}
        dist={}
        while q:
            (x,y),d=q.popleft()
            dist[(x,y)]=d
            for d2 in (N,S,W,E):
                nx,ny=x+dx[d2],y+dy[d2]
                if m.get((nx,ny),0)>0 and (nx,ny) not in seen:
                    seen.add((nx,ny))
                    q.append(((nx,ny),d+1))
        return dist
    dist1 = bfs((0,0))[goal]
    dist2 = max(bfs(goal).values())
    return dist1, dist2

if __name__=="__main__":
    data = list(map(int, open(sys.argv[1]).read().strip().split(',')))
    a,b = solve(data)
    print(a, b)