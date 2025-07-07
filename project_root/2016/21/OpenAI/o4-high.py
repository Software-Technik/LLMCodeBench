import sys
instr=[]
for line in open(sys.argv[1]):
    t=line.split()
    if not t: continue
    if t[0]=='swap':
        if t[1]=='position':
            instr.append((0,int(t[2]),int(t[5])))
        else:
            instr.append((1,t[2],t[5]))
    elif t[0]=='rotate':
        if t[1]=='based':
            instr.append((3,t[6],0))
        else:
            instr.append((2,int(t[2])*(1 if t[1]=='right' else -1),0))
    elif t[0]=='reverse':
        instr.append((4,int(t[2]),int(t[4])))
    elif t[0]=='move':
        instr.append((5,int(t[2]),int(t[5])))
derot=[-1,-1,2,-2,1,-3,0,-4]
pw=list('abcdefgh');n=len(pw)
for op,x,y in instr:
    if op==0:
        pw[x],pw[y]=pw[y],pw[x]
    elif op==1:
        i=pw.index(x);j=pw.index(y);pw[i],pw[j]=pw[j],pw[i]
    elif op==2:
        r=x%n
        if r: pw=pw[-r:]+pw[:-r]
    elif op==3:
        i=pw.index(x);r=(i+1+(i>=4))%n
        if r: pw=pw[-r:]+pw[:-r]
    elif op==4:
        pw[x:y+1]=pw[x:y+1][::-1]
    else:
        c=pw.pop(x);pw.insert(y,c)
first=''.join(pw)
pw=list('fbgdceah');n=len(pw)
for op,x,y in instr[::-1]:
    if op==0:
        pw[x],pw[y]=pw[y],pw[x]
    elif op==1:
        i=pw.index(x);j=pw.index(y);pw[i],pw[j]=pw[j],pw[i]
    elif op==2:
        r=(-x)%n
        if r: pw=pw[-r:]+pw[:-r]
    elif op==3:
        j=pw.index(x);r=derot[j]%n
        if r: pw=pw[-r:]+pw[:-r]
    elif op==4:
        pw[x:y+1]=pw[x:y+1][::-1]
    else:
        c=pw.pop(y);pw.insert(x,c)
second=''.join(pw)
sys.stdout.write(first+' '+second)