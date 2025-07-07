import sys
sys.setrecursionlimit(10000)
def part1(text):
    lines=text.strip().splitlines()
    dimy=len(lines); dimx=len(lines[0])
    tile=''.join(lines)
    sx=lines[0].find('.'); sy=0; start=sy*dimx+sx+dimx
    fx=lines[-1].find('.'); fy=dimy-1; goal=fy*dimx+fx
    N=dimx*dimy
    path=bytearray(N)
    dirs=[(-1,'<'),(1,'>'),(-dimx,'^'),(dimx,'v')]
    def dfs(i,plen):
        if i==goal: return plen
        path[i]=1; best=0
        for d,ch in dirs:
            j=i+d
            c=tile[j]
            if (c=='.' or c==ch) and not path[j]:
                r=dfs(j,plen+1)
                if r>best: best=r
        path[i]=0
        return best
    return dfs(start,1)
def part2(text):
    lines=text.strip().splitlines()
    dimy=len(lines); dimx=len(lines[0])
    tile=''.join(lines)
    sx=lines[0].find('.'); sy=0; s0=sy*dimx+sx
    fx=lines[-1].find('.'); fy=dimy-1; f0=fy*dimx+fx
    dirs=[-1,1,-dimx,dimx]
    branches={s0:0,f0:1}
    graph=[[],[]]
    visited=set()
    def dfs2(i,prev,last,steps):
        visited.add(i)
        cnt=0
        for d in dirs:
            j=i+d
            if tile[j]!='#' and j!=prev: cnt+=1
        if cnt>1:
            idx=len(graph); branches[i]=idx; graph.append([])
            graph[idx].append((last,steps)); graph[last].append((idx,steps))
            last=idx; steps=0
        for d in dirs:
            j=i+d
            if j!=prev and j in branches:
                b=branches[j]
                graph[b].append((last,steps+1)); graph[last].append((b,steps+1))
            elif tile[j]!='#' and j not in visited:
                dfs2(j,i,last,steps+1)
    dfs2(s0+dimx,s0,0,1)
    def bfstrim():
        stack=[0]
        while stack:
            ns=[]
            for cur in stack:
                for dst,_ in graph[cur]:
                    if len(graph[dst])==3:
                        for t,d in graph[dst]:
                            if t==cur:
                                graph[dst].remove((t,d)); break
                        ns.append(dst)
            stack=ns
    bfstrim()
    def dfs3(cur,mask,steps):
        if cur==1: return steps
        mask|=1<<cur; best=0
        for dst,add in graph[cur]:
            if not (mask>>dst)&1:
                r=dfs3(dst,mask,steps+add)
                if r>best: best=r
        return best
    return dfs3(0,0,0)
if __name__=="__main__":
    fn=sys.argv[1]
    txt=open(fn).read()
    sys.stdout.write(f"{part1(txt)} {part2(txt)}")