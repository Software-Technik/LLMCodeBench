import sys

def part1(lines):
    assign={}
    gates={}
    switch=False
    for line in lines:
        if not line:
            switch=True
            continue
        if not switch:
            k,v=line.split(':')
            assign[k]=int(v)
        else:
            a,op,b,_,c=line.split()
            gates[c]=(a,b,op)
    memo=assign.copy()
    def dfs(w):
        if w in memo: return memo[w]
        a,b,op=gates[w]
        aval = memo[a] if a in memo else dfs(a)
        bval = memo[b] if b in memo else dfs(b)
        if op=='AND': res=aval&bval
        elif op=='OR': res=aval|bval
        else: res=aval^bval
        memo[w]=res
        return res
    for w in gates:
        dfs(w)
    zs=[int(k[1:]) for k in memo if k.startswith('z')]
    if not zs: return 0
    maxz=max(zs)
    dec=0
    for i in range(maxz, -1, -1):
        dec=(dec<<1)|memo.get(f'z{i}',0)
    return dec

def part2(lines):
    f={}
    for line in lines:
        if '->' in line:
            a,op,b,_,c=line.split()
            f[c]=(a,b,op)
    mk=lambda p,n: f"{p}{str(n).zfill(2)}"
    def verify_z(w,i):
        t=f.get(w)
        if not t or t[2]!='XOR': return False
        x,y,_=t
        if i==0:
            return {x,y}=={'x00','y00'}
        return (verify_xor(x,i) and verify_cb(y,i)) or (verify_xor(y,i) and verify_cb(x,i))
    def verify_xor(w,i):
        t=f.get(w)
        if not t or t[2]!='XOR': return False
        x,y,_=t
        return {x,y}=={mk('x',i),mk('y',i)}
    def verify_cb(w,i):
        t=f.get(w)
        if not t: return False
        x,y,op=t
        if i==1:
            return op=='AND' and {x,y}=={'x00','y00'}
        if op!='OR': return False
        return (verify_dc(x,i-1) and verify_rc(y,i-1)) or (verify_dc(y,i-1) and verify_rc(x,i-1))
    def verify_dc(w,i):
        t=f.get(w)
        if not t or t[2]!='AND': return False
        x,y,_=t
        return {x,y}=={mk('x',i),mk('y',i)}
    def verify_rc(w,i):
        t=f.get(w)
        if not t or t[2]!='AND': return False
        x,y,_=t
        return (verify_xor(x,i) and verify_cb(y,i)) or (verify_xor(y,i) and verify_cb(x,i))
    def verify(i): return verify_z(mk('z',i),i)
    def progress():
        i=0
        while verify(i): i+=1
        return i
    swaps=[]
    keys=list(f)
    for _ in range(4):
        base=progress()
        done=False
        for i in range(len(keys)):
            for j in range(i+1,len(keys)):
                x,y=keys[i],keys[j]
                f[x],f[y]=f[y],f[x]
                if progress()>base:
                    swaps.extend([x,y])
                    done=True
                    break
                f[x],f[y]=f[y],f[x]
            if done: break
    return ",".join(sorted(swaps))

if __name__=='__main__':
    data=open(sys.argv[1]).read().splitlines()
    print(part1(data),part2(data))