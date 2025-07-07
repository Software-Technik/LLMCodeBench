import sys

def read_input(path):
    with open(path) as f:
        line=f.readline().strip().split()[2]
        f.readline()
        rules=set()
        for l in f:
            l=l.strip()
            if not l: break
            if l[9]=='#':
                m=0
                for c in l[:5]:
                    m=(m<<1)|(c=='#')
                rules.add(m)
    state={i for i,c in enumerate(line) if c=='#'}
    return state, rules

def simulate(state, rules, generations, detect=False):
    last_score=sum(state)
    last_diff=None
    stable=0
    for gen in range(1, generations+1):
        new=set()
        lo,hi=min(state),max(state)
        for p in range(lo-2,hi+3):
            m=0
            for d in (-2,-1,0,1,2):
                m=(m<<1)|(p+d in state)
            if m in rules: new.add(p)
        state=new
        if detect:
            s=sum(state)
            diff=s-last_score
            if diff==last_diff:
                stable+=1
                if stable>=100:
                    rem=generations-gen
                    return s+diff*rem
            else:
                stable=0
            last_score=s
            last_diff=diff
        else:
            last_score=sum(state)
    return last_score

s,r=read_input(sys.argv[1])
p1=simulate(set(s),r,20)
p2=simulate(set(s),r,50000000000,detect=True)
print(p1,p2)