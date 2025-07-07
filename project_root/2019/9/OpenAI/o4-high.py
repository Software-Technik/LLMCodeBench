import sys
def run(data,inp):
    prog={i:v for i,v in enumerate(data)}
    get=prog.get
    i=0;rel=0;out=None
    while 1:
        instr=get(i,0);op=instr%100
        if op==99:break
        modes=instr//100;m1=modes%10;m2=(modes//10)%10;m3=modes//100
        a1=get(i+1,0);a2=get(i+2,0);a3=get(i+3,0)
        p1=a1 if m1==0 else i+1 if m1==1 else a1+rel
        p2=a2 if m2==0 else i+2 if m2==1 else a2+rel
        p3=a3 if m3==0 else a3+rel
        if op==1:
            prog[p3]=get(p1,0)+get(p2,0);i+=4
        elif op==2:
            prog[p3]=get(p1,0)*get(p2,0);i+=4
        elif op==3:
            prog[p1]=inp;i+=2
        elif op==4:
            out=get(p1,0);i+=2
        elif op==5:
            i=get(p2,0) if get(p1,0) else i+3
        elif op==6:
            i=get(p2,0) if not get(p1,0) else i+3
        elif op==7:
            prog[p3]=1 if get(p1,0)<get(p2,0) else 0;i+=4
        elif op==8:
            prog[p3]=1 if get(p1,0)==get(p2,0) else 0;i+=4
        else:
            rel+=get(p1,0);i+=2
    return out

data=[*map(int,open(sys.argv[1]).read().split(','))]
sys.stdout.write(f"{run(data,1)} {run(data,2)}")