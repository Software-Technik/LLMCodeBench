import sys
def run(ops,args,n):
    acc=0; idx=0; vis=[False]*n
    while idx<n and not vis[idx]:
        vis[idx]=True
        o=ops[idx]; a=args[idx]
        if o==0: acc+=a; idx+=1
        elif o==1: idx+=a
        else: idx+=1
    return idx==n, acc
def main():
    data=open(sys.argv[1]).read().splitlines()
    n=len(data)
    ops=[0]*n; args=[0]*n
    for i,l in enumerate(data):
        args[i]=int(l[4:])
        c=l[0]
        ops[i]=0 if c=='a' else 1 if c=='j' else 2
    _,part1=run(ops,args,n)
    for i,o in enumerate(ops):
        if o==0: continue
        ops[i]=3-o
        term,acc=run(ops,args,n)
        ops[i]=o
        if term:
            print(part1, acc)
            return
if __name__=='__main__':
    main()