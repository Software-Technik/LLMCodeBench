import sys
def parse(data):
    triples=[]
    names=set()
    for line in data:
        parts=line.split()
        if not parts:continue
        a=parts[0]
        b=parts[10][:-1]
        val=int(parts[3])*(1 if parts[2]=='gain' else -1)
        names.add(a);names.add(b)
        triples.append((a,b,val))
    return triples,names
def max_happiness(triples,names):
    index={name:i for i,name in enumerate(names)}
    n=len(names)
    h=[[0]*n for _ in range(n)]
    for a,b,val in triples:
        h[index[a]][index[b]]=val
    w=[[0]*n for _ in range(n)]
    for i in range(n):
        hi=h[i]
        for j in range(n):
            w[i][j]=hi[j]+h[j][i]
    FULL=1<<n
    NEG=-10**18
    dp=[[NEG]*n for _ in range(FULL)]
    dp[1][0]=0
    for mask in range(FULL):
        if not (mask&1):continue
        row=dp[mask]
        for u in range(n):
            if not (mask>>u&1):continue
            cur=row[u]
            if cur==NEG:continue
            for v in range(1,n):
                if mask>>v&1:continue
                nm=mask|1<<v
                val=cur+w[u][v]
                if val>dp[nm][v]:
                    dp[nm][v]=val
    full=(1<<n)-1
    res=NEG
    last=dp[full]
    for u in range(1,n):
        val=last[u]+w[u][0]
        if val>res:res=val
    return res
data=[line.strip() for line in open(sys.argv[1])]
triples,names=parse(data)
res1=max_happiness(triples,names)
triples2=list(triples)
for name in names:
    triples2.append((name,'me',0));triples2.append(('me',name,0))
names2=list(names)+['me']
res2=max_happiness(triples2,names2)
sys.stdout.write(f"{res1}\n{res2}\n")