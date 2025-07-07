import sys,re

mapping={'x':0,'m':1,'a':2,'s':3}

def parse_workflows(lines):
    w={}
    for line in lines:
        name,conds=line.split('{',1)
        conds=conds[:-1]
        rules=[]
        for r in conds.split(','):
            if '<' in r:
                c,rest=r.split('<',1)
                v,nxt=rest.split(':',1)
                rules.append(('<',mapping[c],int(v),nxt))
            elif '>' in r:
                c,rest=r.split('>',1)
                v,nxt=rest.split(':',1)
                rules.append(('>',mapping[c],int(v),nxt))
            else:
                rules.append(('=',None,None,r))
        w[name]=rules
    return w

data=open(sys.argv[1]).read()
wt,pt=data.split('\n\n',1)
workflows=parse_workflows(wt.splitlines())
pat=re.compile(r'([a-z]+)=([0-9]+)')
parts=[]
for line in pt.splitlines():
    vals=[0,0,0,0]
    for c,v in pat.findall(line):
        vals[mapping[c]]=int(v)
    parts.append(vals)

total1=0
for vals in parts:
    wf='in'
    while wf not in ('A','R'):
        for op,cidx,v,nxt in workflows[wf]:
            if op=='<' and vals[cidx]<v or op=='>' and vals[cidx]>v or op=='=':
                wf=nxt
                break
    if wf=='A':
        total1+=sum(vals)

def rec(wf,ranges):
    if wf=='A':
        res=1
        for iv in ranges:
            s=0
            for a,b in iv:
                s+=b-a+1
            res*=s
        return res
    if wf=='R':
        return 0
    tot=0
    for op,cidx,v,nxt in workflows[wf]:
        if op=='<':
            sat=[]
            fail=[]
            for a,b in ranges[cidx]:
                if b<v:
                    sat.append((a,b))
                elif a<v:
                    sat.append((a,v-1))
                    fail.append((v,b))
                else:
                    fail.append((a,b))
            if sat:
                nr=list(ranges); nr[cidx]=sat
                tot+=rec(nxt,tuple(nr))
            if not fail:
                return tot
            nr=list(ranges); nr[cidx]=fail
            ranges=tuple(nr)
        elif op=='>':
            sat=[]
            fail=[]
            for a,b in ranges[cidx]:
                if a>v:
                    sat.append((a,b))
                elif b>v:
                    sat.append((v+1,b))
                    fail.append((a,v))
                else:
                    fail.append((a,b))
            if sat:
                nr=list(ranges); nr[cidx]=sat
                tot+=rec(nxt,tuple(nr))
            if not fail:
                return tot
            nr=list(ranges); nr[cidx]=fail
            ranges=tuple(nr)
        else:
            return rec(nxt,ranges)
    return tot

init=tuple([[(1,4000)] for _ in range(4)])
total2=rec('in',init)
sys.stdout.write(f"{total1} {total2}")