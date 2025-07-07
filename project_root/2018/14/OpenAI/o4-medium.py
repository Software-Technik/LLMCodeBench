import sys
def main():
    p=sys.argv[1]
    with open(p) as f:
        s=f.readline().strip()
    target=int(s); tlen=len(s); td=[ord(c)-48 for c in s]
    scores=bytearray([3,7]); e1,e2=0,1; goal=target+10
    while len(scores)<goal:
        sm=scores[e1]+scores[e2]
        if sm>=10:
            scores.append(sm//10); scores.append(sm%10)
        else:
            scores.append(sm)
        e1=(e1+scores[e1]+1)%len(scores)
        e2=(e2+scores[e2]+1)%len(scores)
    out1=''.join(str(c) for c in scores[target:goal])
    pi=[0]*tlen; j=0
    for i in range(1,tlen):
        while j and td[i]!=td[j]:
            j=pi[j-1]
        if td[i]==td[j]:
            j+=1
        pi[i]=j
    scores.clear(); scores.extend((3,7)); e1,e2=0,1; k=0; n=2; found=None
    if tlen<=2:
        ok=True
        for i in range(tlen):
            if scores[i]!=td[i]:
                ok=False;break
        if ok:
            found=0
    while found is None:
        sm=scores[e1]+scores[e2]
        if sm>=10:
            for d in (sm//10,sm%10):
                while k and d!=td[k]:
                    k=pi[k-1]
                if d==td[k]:
                    k+=1
                n+=1
                if k==tlen:
                    found=n-tlen; break
                scores.append(d)
            if found is not None:
                break
        else:
            d=sm
            while k and d!=td[k]:
                k=pi[k-1]
            if d==td[k]:
                k+=1
            n+=1
            if k==tlen:
                found=n-tlen; break
            scores.append(d)
        e1=(e1+scores[e1]+1)%n
        e2=(e2+scores[e2]+1)%n
    sys.stdout.write(out1+' '+str(found))
if __name__=="__main__":
    main()