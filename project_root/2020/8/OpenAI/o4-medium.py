import sys
def run(cmds):
    n=len(cmds)
    acc=0; idx=0
    vis=[False]*n
    while idx<n and not vis[idx]:
        vis[idx]=True
        op,val=cmds[idx]
        if op==0:
            acc+=val; idx+=1
        elif op==1:
            idx+=val
        else:
            idx+=1
    return acc, idx>=n

lines=open(sys.argv[1]).read().splitlines()
cmds=[]
for l in lines:
    a,b=l.split()
    v=int(b)
    if a=='acc': o=0
    elif a=='jmp': o=1
    else: o=2
    cmds.append((o,v))
p1,_=run(cmds)
p2=None
for i,(o,v) in enumerate(cmds):
    if o!=0:
        cmds[i]=(3-o,v)
        a,term=run(cmds)
        if term:
            p2=a;break
        cmds[i]=(o,v)
print(p1,p2)