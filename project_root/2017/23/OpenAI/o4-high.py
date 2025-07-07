import sys

def main():
    inst=[]
    with open(sys.argv[1]) as f:
        for line in f:
            parts=line.split()
            if len(parts)>=3:
                inst.append(parts)
                if len(inst)==11: break
    def simulate(a):
        regs=[0]*8
        regs[0]=a
        i=0
        while i<11:
            op,x,y=inst[i]
            if op=='set':
                regs[ord(x)-97] = regs[ord(y)-97] if y.isalpha() else int(y)
            elif op=='sub':
                regs[ord(x)-97] -= regs[ord(y)-97] if y.isalpha() else int(y)
            elif op=='mul':
                regs[ord(x)-97] *= regs[ord(y)-97] if y.isalpha() else int(y)
            else:
                cond = regs[ord(x)-97] if x.isalpha() else int(x)
                if cond:
                    i += regs[ord(y)-97] if y.isalpha() else int(y)
                    continue
            i+=1
        return regs
    r1=simulate(0)
    res1=(r1[1]-r1[4])*(r1[1]-r1[3])
    r2=simulate(1)
    b,c=r2[1],r2[2]
    cnt=0
    for v in range(b,c+1,17):
        if v%2==0:
            cnt+=1
        else:
            lim=int(v**0.5)
            for d in range(3,lim+1,2):
                if v%d==0:
                    cnt+=1
                    break
    sys.stdout.write(f"{res1}\n{cnt}\n")

if __name__=='__main__':
    main()