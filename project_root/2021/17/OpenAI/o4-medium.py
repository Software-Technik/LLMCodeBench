import sys,math

with open(sys.argv[1]) as f:
    line=f.read().strip()
p=line.split()
x1,x2=map(int,p[2][2:-1].split('..'))
y1,y2=map(int,p[3][2:].split('..'))
min_vx=math.ceil((math.sqrt(1+8*x1)-1)/2)
max_vy=-y1-1
best_y=count=0

for vx0 in range(min_vx,x2+1):
    for vy0 in range(y1,max_vy+1):
        x=y=0
        vx,vy=vx0,vy0
        curr_max=0
        while x<=x2 and y>=y1:
            x+=vx; y+=vy
            if y>curr_max: curr_max=y
            if x1<=x<=x2 and y1<=y<=y2:
                count+=1
                if curr_max>best_y: best_y=curr_max
                break
            vx=max(0,vx-1); vy-=1
            if vx==0 and x<x1: break

sys.stdout.write(f"{best_y} {count}")