import sys
from collections import defaultdict, deque

N,S,W,E=1,2,3,4
dx={N:0,S:0,W:-1,E:1}
dy={N:-1,S:1,W:0,E:0}
opposite={N:S,S:N,W:E,E:W}

def runComputer(data, inp):
    mem=defaultdict(int)
    mem.update(enumerate(data))
    i=0; rel=0
    while True:
        op=mem[i]%100
        if op==99: break
        m1=mem[i]//100%10; m2=mem[i]//1000%10; m3=mem[i]//10000%10
        if m1==0: p1=mem[i+1]
        elif m1==1: p1=i+1
        else: p1=mem[i+1]+rel
        if m2==0: p2=mem[i+2]
        elif m2==1: p2=i+2
        else: p2=mem[i+2]+rel
        if m3==2: p3=mem[i+3]+rel
        else: p3=mem[i+3]
        if op==1:
            mem[p3]=mem[p1]+mem[p2]; i+=4
        elif op==2:
            mem[p3]=mem[p1]*mem[p2]; i+=4
        elif op==3:
            mem[p1]=inp.pop(); i+=2
        elif op==4:
            yield mem[p1]; i+=2
        elif op==5:
            i=mem[p2] if mem[p1]!=0 else i+3
        elif op==6:
            i=mem[p2] if mem[p1]==0 else i+3
        elif op==7:
            mem[p3]=1 if mem[p1]<mem[p2] else 0; i+=4
        elif op==8:
            mem[p3]=1 if mem[p1]==mem[p2] else 0; i+=4
        elif op==9:
            rel+=mem[p1]; i+=2
        else:
            break

def map_explore(data):
    inp=[]; runner=runComputer(data, inp)
    x=y=0
    walls=set(); spaces={(0,0)}; visited={(0,0)}; goal=None
    stack=[]
    while True:
        moved=False
        for d in (N,S,W,E):
            nx,ny=x+dx[d],y+dy[d]
            if (nx,ny) not in visited:
                inp.append(d)
                status=next(runner)
                visited.add((nx,ny))
                if status==0:
                    walls.add((nx,ny))
                else:
                    spaces.add((nx,ny)); x,y=nx,ny; stack.append(d)
                    if status==2: goal=(nx,ny)
                moved=True
                break
        if moved: continue
        if not stack: break
        back=opposite[stack.pop()]
        inp.append(back)
        _=next(runner)
        x+=dx[back]; y+=dy[back]
    return spaces, walls, goal

def part1(data):
    spaces,_,goal=map_explore(data)
    dq=deque([((0,0),0)]); seen={(0,0)}
    while dq:
        (x,y),d=dq.popleft()
        if (x,y)==goal: return d
        for dx_i,dy_i in ((0,1),(1,0),(0,-1),(-1,0)):
            np=(x+dx_i,y+dy_i)
            if np in spaces and np not in seen:
                seen.add(np); dq.append((np,d+1))
    return -1

def part2(data):
    spaces,_,goal=map_explore(data)
    dq=deque([(goal,0)]); dist={goal:0}; m=0
    while dq:
        (x,y),d=dq.popleft(); m=max(m,d)
        for dx_i,dy_i in ((0,1),(1,0),(0,-1),(-1,0)):
            np=(x+dx_i,y+dy_i)
            if np in spaces and np not in dist:
                dist[np]=d+1; dq.append((np,d+1))
    return m

if __name__=='__main__':
    data=list(map(int,open(sys.argv[1]).read().strip().split(',')))
    sys.stdout.write(f"{part1(data)} {part2(data)}")