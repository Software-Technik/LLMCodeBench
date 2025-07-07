import sys
sys.setrecursionlimit(10000)
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
def part1(text):
    tiles = text.strip().splitlines()
    h, w = len(tiles), len(tiles[0])
    sx, fx = tiles[0].find('.'), tiles[-1].find('.')
    target = (fx, h-1)
    seen = [0]*(h*w)
    best = 0
    def dfs(x,y,steps):
        nonlocal best
        if (x,y)==target:
            if steps>best: best=steps
            return
        seen[y*w+x]=1
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<w and 0<=ny<h and not seen[ny*w+nx]:
                c = tiles[ny][nx]
                if c=='.' or (dx,dy)==(-1,0) and c=='<' or (dx,dy)==(1,0) and c=='>' or (dx,dy)==(0,-1) and c=='^' or (dx,dy)==(0,1) and c=='v':
                    dfs(nx,ny,steps+1)
        seen[y*w+x]=0
    dfs(sx,1,1)
    return best

def part2(text):
    tiles = text.strip().splitlines()
    h, w = len(tiles), len(tiles[0])
    sx, fx = tiles[0].find('.'), tiles[-1].find('.')
    start, end = (sx,0),(fx,h-1)
    branches = {start:0, end:1}
    graph = [[],[]]
    seen=set()
    def dfs2(x,y,px,py,node,dist):
        seen.add((x,y))
        cnt=0
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if tiles[ny][nx]!='#' and (nx,ny)!=(px,py): cnt+=1
        if cnt>1:
            nid=len(graph); branches[(x,y)]=nid; graph.append([])
            graph[node].append((nid,dist)); graph[nid].append((node,dist))
            node,nid_dist = nid,0
        else: nid_dist=dist
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if (nx,ny)!=(px,py) and tiles[ny][nx]!='#':
                if (nx,ny) in branches:
                    b=branches[(nx,ny)]
                    graph[node].append((b,nid_dist+1)); graph[b].append((node,nid_dist+1))
                elif (nx,ny) not in seen:
                    dfs2(nx,ny,x,y,node,nid_dist+1)
    dfs2(sx,1,sx,0,0,1)
    # trim
    q=[0]
    while q:
        nq=[]
        for u in q:
            for v,_ in graph[u]:
                if len(graph[v])==3:
                    for t,d in graph[v]:
                        if t==u:
                            graph[v].remove((t,d)); break
                    nq.append(v)
        q=nq
    # dfs3
    N=len(graph)
    memo={}
    def dfs3(u,mask):
        if u==1: return 0
        key=(u,mask)
        if key in memo: return memo[key]
        res=0
        m2=mask|(1<<u)
        for v,d in graph[u]:
            if not(mask>>v&1):
                res=max(res, d+dfs3(v,m2))
        memo[key]=res
        return res
    return dfs3(0,1)
if __name__=="__main__":
    t=open(sys.argv[1]).read()
    print(part1(t), part2(t))