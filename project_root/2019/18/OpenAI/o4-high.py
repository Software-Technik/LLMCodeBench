import sys
from collections import deque
import heapq

def parse_grid(data):
    grid={}
    keys={}
    start=None
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            grid[(x,y)]=c
            if c=='@': start=(x,y)
            elif 'a'<=c<='z': keys[c]=(x,y)
    grid[start]='.'
    return grid,start,keys

def bfs(grid,start,key_to_index):
    visited={start}
    dists={}
    queue=deque([(start,0,0)])
    while queue:
        pos,dist,mask=queue.popleft()
        cell=grid[pos]
        if cell.islower() and dist>0:
            ki=key_to_index[cell]
            dists[ki]=(dist,mask)
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            npos=(pos[0]+dx,pos[1]+dy)
            if npos not in grid: continue
            cc=grid[npos]
            if cc=='#': continue
            newmask=mask
            if cc.isupper():
                newmask |= 1<<key_to_index[cc.lower()]
            if npos not in visited:
                visited.add(npos)
                queue.append((npos,dist+1,newmask))
    return dists

def dp1(dist_map,nkeys):
    allmask=(1<<nkeys)-1
    seen={}
    heap=[(0,0,0)]
    seen[(0,0)]=0
    while heap:
        dist,i,mask=heapq.heappop(heap)
        if seen[(i,mask)]<dist: continue
        if mask==allmask: return dist
        for ki in range(nkeys):
            bit=1<<ki
            if mask&bit: continue
            target=dist_map[i].get(ki)
            if not target: continue
            d,req=target
            if req&mask!=req: continue
            nm=mask|bit
            ni=ki+1
            nd=dist+d
            st=(ni,nm)
            if seen.get(st,1e18)>nd:
                seen[st]=nd
                heapq.heappush(heap,(nd,ni,nm))
    return -1

def dp2(dist_map,nkeys):
    allmask=(1<<nkeys)-1
    seen={}
    init_pos=(0,1,2,3)
    seen[(init_pos,0)]=0
    heap=[(0,init_pos,0)]
    while heap:
        dist,poses,mask=heapq.heappop(heap)
        if seen[(poses,mask)]<dist: continue
        if mask==allmask: return dist
        for ri,pi in enumerate(poses):
            for ki in range(nkeys):
                bit=1<<ki
                if mask&bit: continue
                target=dist_map[pi].get(ki)
                if not target: continue
                d,req=target
                if req&mask!=req: continue
                nm=mask|bit
                newpi=4+ki
                newposes=list(poses)
                newposes[ri]=newpi
                newposes=tuple(newposes)
                nd=dist+d
                st=(newposes,nm)
                if seen.get(st,1e18)>nd:
                    seen[st]=nd
                    heapq.heappush(heap,(nd,newposes,nm))
    return -1

def main():
    data=open(sys.argv[1]).read().splitlines()
    grid0,start0,keys0=parse_grid(data)
    keys_list=sorted(keys0)
    nkeys=len(keys_list)
    key_to_index={c:i for i,c in enumerate(keys_list)}
    key_positions=[keys0[c] for c in keys_list]
    pos_list1=[start0]+key_positions
    dist_map1=[None]*(1+nkeys)
    for i,pos in enumerate(pos_list1):
        dist_map1[i]=bfs(grid0,pos,key_to_index)
    r1=dp1(dist_map1,nkeys)
    grid2=grid0.copy()
    x0,y0=start0
    for dx,dy in ((0,0),(1,0),(-1,0),(0,1),(0,-1)):
        grid2[(x0+dx,y0+dy)]='#'
    starts2=[(x0-1,y0-1),(x0-1,y0+1),(x0+1,y0-1),(x0+1,y0+1)]
    pos_list2=starts2+key_positions
    dist_map2=[None]*(4+nkeys)
    for i,pos in enumerate(pos_list2):
        dist_map2[i]=bfs(grid2,pos,key_to_index)
    r2=dp2(dist_map2,nkeys)
    sys.stdout.write(f"{r1} {r2}")

if __name__=="__main__":
    main()