import sys

def main():
    lines = open(sys.argv[1]).read().splitlines()
    A = int(lines[0].split(':',1)[1])
    B = int(lines[1].split(':',1)[1])
    C = int(lines[2].split(':',1)[1])
    prog = list(map(int, lines[4].split(':',1)[1].split(',')))

    def combo(v, regs):
        return v if v<4 else regs[v-4]

    def part1():
        regs = [A,B,C]
        out = []
        i=0
        n=len(prog)
        while i<n:
            op=prog[i]; v=prog[i+1]
            if op==0: regs[0]//=1<<combo(v,regs)
            elif op==1: regs[1]^=v
            elif op==2: regs[1]=combo(v,regs)%8
            elif op==3:
                if regs[0]!=0:
                    i=v; continue
            elif op==4: regs[1]^=regs[2]
            elif op==5: out.append(str(combo(v,regs)%8))
            elif op==6: regs[1]=regs[0]//(1<<combo(v,regs))
            elif op==7: regs[2]=regs[0]//(1<<combo(v,regs))
            else: raise
            i+=2
        return ','.join(out)

    def part2():
        assert prog[-2:]==[3,0]
        L=len(prog)-2
        def dfs(tar, ans):
            if not tar: return ans
            for d in range(8):
                regs=[ans*8+d,0,0]
                out=None; adv=False
                for i in range(0,L,2):
                    op=prog[i]; v=prog[i+1]
                    if op==0:
                        if adv or v!=3: raise
                        adv=True
                    elif op==1: regs[1]^=v
                    elif op==2: regs[1]=combo(v,regs)%8
                    elif op==4: regs[1]^=regs[2]
                    elif op==5:
                        if out is not None: raise
                        out=combo(v,regs)%8
                    elif op==6: regs[1]=regs[0]>>combo(v,regs)
                    elif op==7: regs[2]=regs[0]>>combo(v,regs)
                if out==tar[-1]:
                    res=dfs(tar[:-1], regs[0])
                    if res is not None: return res
            return None
        return dfs(prog,0)

    print(part1(), part2())

if __name__=='__main__':
    main()