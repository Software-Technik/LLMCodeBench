import sys
from functools import lru_cache

def part1(lines):
    idx = lines.index('\n')
    a = dict(line.split(': ') for line in map(str.strip, lines[:idx]))
    a = {k:int(v) for k,v in a.items()}
    gates = {}
    for line in lines[idx+1:]:
        if not line.strip(): continue
        x,op,y,_,z = line.split()
        gates[z] = (x,y,op)
    @lru_cache(None)
    def val(w):
        if w.isdigit() or w in a:
            return a[w] if w in a else int(w)
        x,y,op = gates[w]
        u,v = val(x), val(y)
        if op=='AND': return u&v
        if op=='OR': return u|v
        if op=='XOR': return u^v
    for w in gates: val(w)
    zs = sorted((w for w in list(a.keys())+list(gates.keys()) if w.startswith('z')), reverse=True)
    b=''.join(str(val(w)) for w in zs)
    return int(b,2)

def part2(lines):
    f = {}
    for l in lines:
        if '->' in l:
            x,op,y,_,z=l.split()
            f[z]=(x,y,op)
    def m(p,n): return f.get(f.get(p,('','',None))[2] and p)
    def make(p,n): return f.get(p,())
    def wire(p,n): return f.get(p,())
    def mk(p,n): return p+str(n).zfill(2)
    def verify_z(w,n):
        if (t:=f.get(w)) and t[2]=='XOR':
            x,y,_=t
            if n==0: return sorted([x,y])==['x00','y00']
            return (verify_x(x,n) and carry(y,n)) or (verify_x(y,n) and carry(x,n))
        return False
    def verify_x(w,n):
        if (t:=f.get(w)) and t[2]=='XOR':
            return sorted(t[:2])==[mk('x',n),mk('y',n)]
        return False
    def direct(w,n):
        if (t:=f.get(w)) and t[2]=='AND':
            return sorted(t[:2])==[mk('x',n),mk('y',n)]
        return False
    def rec(w,n):
        if (t:=f.get(w)) and t[2]=='AND':
            x,y,_=t
            return (verify_x(x,n) and carry(y,n)) or (verify_x(y,n) and carry(x,n))
        return False
    def carry(w,n):
        if (t:=f.get(w)):
            x,y,op=t
            if n==1: return op=='AND' and sorted([x,y])==['x00','y00']
            if op=='OR':
                return (direct(x,n-1) and rec(y,n-1)) or (direct(y,n-1) and rec(x,n-1))
        return False
    def ok(n): return verify_z(mk('z',n),n)
    def prog():
        i=0
        while ok(i): i+=1
        return i
    keys=list(f)
    swaps=[]
    for _ in range(4):
        bas=prog()
        for i in range(len(keys)):
            for j in range(i+1,len(keys)):
                x,y=keys[i],keys[j]
                f[x],f[y]=f[y],f[x]
                if prog()>bas:
                    swaps+= [x,y]
                    break
                f[x],f[y]=f[y],f[x]
            else: continue
            break
    return ','.join(sorted(swaps))

lines = sys.stdin.read().splitlines(True)
print(part1(lines),part2(lines))