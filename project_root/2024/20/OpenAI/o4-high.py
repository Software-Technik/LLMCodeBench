import sys
def main():
    data=open(sys.argv[1]).read().strip().split('\n')
    grid=[list(line) for line in data]
    N=len(grid)
    for i,row in enumerate(grid):
        for j,ch in enumerate(row):
            if ch=='S': si,sj=i,j
            elif ch=='E': ei,ej=i,j
    dd=((1,0),(0,1),(-1,0),(0,-1))
    off2=((2,0),(0,2),(-2,0),(0,-2),(1,1),(1,-1),(-1,1),(-1,-1))
    max_len=20
    offsets=[(dx,dy) for dx in range(-max_len,max_len+1) for dy in range(-max_len,max_len+1) if abs(dx)+abs(dy)<=max_len]
    path=[(si,sj)]
    while path[-1]!=(ei,ej):
        i,j=path[-1]
        for di,dj in dd:
            ii,jj=i+di,j+dj
            if 0<=ii<N and 0<=jj<N and grid[ii][jj]!="#" and (len(path)<=1 or (ii,jj)!=path[-2]):
                path.append((ii,jj)); break
    og=len(path)-1
    times={coord:og-t for t,coord in enumerate(path)}
    tg=times.__getitem__
    ans1=ans2=0
    for t,(i,j) in enumerate(path):
        for dx,dy in off2:
            ii,jj=i+dx,j+dy
            if 0<=ii<N and 0<=jj<N and grid[ii][jj]!="#":
                if og-(t+tg((ii,jj))+2)>=100: ans1+=1
        for dx,dy in offsets:
            ii,jj=i+dx,j+dy
            if 0<=ii<N and 0<=jj<N and grid[ii][jj]!="#":
                td=abs(dx)+abs(dy)
                if og-(t+tg((ii,jj))+td)>=100: ans2+=1
    print(ans1, ans2)
if __name__=="__main__":
    main()