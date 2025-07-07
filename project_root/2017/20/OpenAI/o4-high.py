import sys,math
from collections import defaultdict
with open(sys.argv[1]) as f: lines=[l.strip() for l in f if l.strip()]
particles=[]
for line in lines:
    tmp=''; nums=[]
    for c in line:
        if c=='-' or '0'<=c<='9': tmp+=c
        elif tmp:
            nums.append(int(tmp)); tmp=''
    if tmp: nums.append(int(tmp))
    particles.append(tuple(nums))
min_idx=0; min_mag=None
for i,p in enumerate(particles):
    ax,ay,az=p[6],p[7],p[8]; m=ax*ax+ay*ay+az*az
    if min_mag is None or m<min_mag:
        min_mag=m; min_idx=i
print(min_idx)
n=len(particles)
collisions=defaultdict(list)
for i in range(n):
    pi=particles[i]
    for j in range(i+1,n):
        pj=particles[j]
        px,py,pz=pi[0]-pj[0],pi[1]-pj[1],pi[2]-pj[2]
        vx,vy,vz=pi[3]-pj[3],pi[4]-pj[4],pi[5]-pj[5]
        ax,ay,az=pi[6]-pj[6],pi[7]-pj[7],pi[8]-pj[8]
        a=ax; b=vx*2+ax; c=px*2; t=None
        if a==0:
            if b!=0 and -c%b==0:
                tt=-c//b
                if tt>0:
                    c2=py*2; b2=vy*2+ay; aa=ay
                    if aa*tt*tt+b2*tt+c2==0:
                        c3=pz*2; b3=vz*2+az; aa3=az
                        if aa3*tt*tt+b3*tt+c3==0: t=tt
        else:
            D=b*b-4*a*c
            if D>=0:
                sd=math.isqrt(D)
                if sd*sd==D:
                    denom=2*a; numb=-b
                    num1=numb-sd
                    if num1%denom==0:
                        tt=num1//denom
                        if tt>0:
                            c2=py*2; b2=vy*2+ay; aa=ay
                            if aa*tt*tt+b2*tt+c2==0:
                                c3=pz*2; b3=vz*2+az; aa3=az
                                if aa3*tt*tt+b3*tt+c3==0: t=tt
                    if t is None:
                        num2=numb+sd
                        if num2%denom==0:
                            tt=num2//denom
                            if tt>0:
                                c2=py*2; b2=vy*2+ay; aa=ay
                                if aa*tt*tt+b2*tt+c2==0:
                                    c3=pz*2; b3=vz*2+az; aa3=az
                                    if aa3*tt*tt+b3*tt+c3==0: t=tt
        if t is not None:
            collisions[t].append((i,j))
dead=set()
for time in sorted(collisions):
    colliding=set()
    for i,j in collisions[time]:
        if i not in dead and j not in dead:
            colliding.add(i)
            colliding.add(j)
    dead|=colliding
print(n-len(dead))