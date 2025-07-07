import sys
f=sys.argv[1]
lines=open(f).read().splitlines()
mp={'a':0,'b':1,'c':2,'d':3}
instrs=[]
for l in lines:
    p=l.split()
    if p[0]=='cpy':
        x=p[1]; y=mp[p[2]]
        if x.lstrip('-').isdigit(): instrs.append((0,1,int(x),y))
        else: instrs.append((0,0,mp[x],y))
    elif p[0]=='inc':
        instrs.append((1,mp[p[1]]))
    elif p[0]=='dec':
        instrs.append((2,mp[p[1]]))
    else:
        x=p[1]; y=int(p[2])
        if x.lstrip('-').isdigit(): instrs.append((3,1,int(x),y))
        else: instrs.append((3,0,mp[x],y))
def run(initc):
    regs=[0,0,initc,0]; i=0; n=len(instrs)
    while i<n:
        ins=instrs[i]; op=ins[0]
        if op==0:
            _,t,x,y=ins; regs[y]=x if t else regs[x]; i+=1
        elif op==1:
            regs[ins[1]]+=1; i+=1
        elif op==2:
            regs[ins[1]]-=1; i+=1
        else:
            _,t,x,y=ins; v=x if t else regs[x]; i+=y if v else 1
    return regs[0]
sys.stdout.write(f"{run(0)} {run(1)}")