import sys

def run(data, init_c):
    regs = {'a':0,'b':0,'c':init_c,'d':0}
    instrs = [line.split() for line in data]
    i = 0
    n = len(instrs)
    while i < n:
        op, x, *rest = instrs[i]
        y = rest[0] if rest else None
        if op=='jnz':
            vx = regs[x] if x in regs else int(x)
            if vx!=0:
                i += int(y)
                continue
        elif op=='cpy':
            if y in regs:
                regs[y] = regs[x] if x in regs else int(x)
        elif op=='inc':
            regs[x]+=1
        elif op=='dec':
            regs[x]-=1
        # pattern for mul: cpy b c; inc a; dec c; jnz c -2; dec d; jnz d -5
        if op=='cpy' and i+5<n:
            p1,p2,p3,p4,p5,p6 = instrs[i:i+6]
            if p1[0]=='cpy' and p2[0]=='inc' and p3[0]=='dec' and p4[0]=='jnz' and p5[0]=='dec' and p6[0]=='jnz':
                b,c = p1[1],p1[2]
                if p2[1]=='a' and p3[1]==c and p4[1]==c and p4[2]=='-2' and p5[1]=='d' and p6[1]=='d' and p6[2]=='-5':
                    regs['a'] += (regs[b] if b in regs else int(b)) * regs['d']
                    regs[c]=0; regs['d']=0
                    i+=6
                    continue
        i+=1
    return regs['a']

data = open(sys.argv[1]).read().splitlines()
print(run(data,0), run(data,1))