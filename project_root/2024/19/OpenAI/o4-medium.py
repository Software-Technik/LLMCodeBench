import sys
def part1(groups,lengths,designs):
    ans=0
    for d in designs:
        n=len(d); dp=[False]*(n+1); dp[0]=True
        for i in range(1,n+1):
            for l in lengths:
                if l>i: break
                if dp[i-l] and d[i-l:i] in groups[l]:
                    dp[i]=True; break
        if dp[n]: ans+=1
    return ans

def part2(groups,lengths,designs):
    ans=0
    for d in designs:
        n=len(d); dp=[0]*(n+1); dp[0]=1
        for i in range(1,n+1):
            s=0
            for l in lengths:
                if l>i: break
                if d[i-l:i] in groups[l]:
                    s+=dp[i-l]
            dp[i]=s
        ans+=dp[n]
    return ans

def main():
    lines=open(sys.argv[1]).read().splitlines()
    units=lines[0].split(", ")
    groups={}
    for u in units: groups.setdefault(len(u),set()).add(u)
    lengths=sorted(groups)
    designs=lines[2:]
    print(part1(groups,lengths,designs),part2(groups,lengths,designs))

if __name__=="__main__":
    main()