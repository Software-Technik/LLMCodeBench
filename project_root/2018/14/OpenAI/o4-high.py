import sys
def main():
    data=open(sys.argv[1]).read().strip()
    n=int(data)
    pat=[ord(c)-48 for c in data]
    m=len(pat)
    pi=[0]*m
    j=0
    for i in range(1,m):
        while j and pat[i]!=pat[j]: j=pi[j-1]
        if pat[i]==pat[j]: j+=1
        pi[i]=j
    s=bytearray((3,7))
    elf1=0; elf2=1
    k=0; part1=None; part2=None
    for idx,d in enumerate(s):
        while k and d!=pat[k]: k=pi[k-1]
        if d==pat[k]: k+=1
        if k==m:
            part2=idx+1-m
            k=pi[k-1]
            break
    while part1 is None or part2 is None:
        p1=s[elf1]; p2=s[elf2]
        tot=p1+p2
        if tot>=10:
            digits=(tot//10, tot%10)
        else:
            digits=(tot,)
        for d in digits:
            s.append(d)
            idx=len(s)-1
            if part1 is None and idx>=n+9:
                part1=''.join(chr(x+48) for x in s[n:n+10])
            if part2 is None:
                while k and d!=pat[k]: k=pi[k-1]
                if d==pat[k]: k+=1
                if k==m:
                    part2=idx+1-m
                    k=pi[k-1]
        elf1=(elf1+1+p1)%len(s)
        elf2=(elf2+1+p2)%len(s)
    sys.stdout.write(f"{part1} {part2}")
if __name__=='__main__':
    main()