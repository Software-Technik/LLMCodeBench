import sys
data = open(sys.argv[1]).read().splitlines()
ins = []
m = {'a':0,'b':1}
for l in data:
    op = l[:3]
    if op=='hlf':
        ins.append((0,m[l[4]],0))
    elif op=='tpl':
        ins.append((1,m[l[4]],0))
    elif op=='inc':
        ins.append((2,m[l[4]],0))
    elif op=='jmp':
        ins.append((3,int(l[4:]),0))
    elif op=='jie':
        ins.append((4,m[l[4]],int(l[7:])))
    else:
        ins.append((5,m[l[4]],int(l[7:])))
def run(a0):
    r0 = a0; r1 = 0; idx = 0; n = len(ins)
    while 0<=idx<n:
        op,x,y = ins[idx]
        if op==0:
            if x==0: r0//=2
            else: r1//=2
            idx+=1
        elif op==1:
            if x==0: r0*=3
            else: r1*=3
            idx+=1
        elif op==2:
            if x==0: r0+=1
            else: r1+=1
            idx+=1
        elif op==3:
            idx+=x
        elif op==4:
            val = r0 if x==0 else r1
            idx+= y if val%2==0 else 1
        else:
            val = r0 if x==0 else r1
            idx+= y if val==1 else 1
    return r1
print(run(0),run(1),sep='\n')