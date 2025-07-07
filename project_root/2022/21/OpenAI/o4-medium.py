import sys
data=open(sys.argv[1]).read().splitlines()
ops={}
for line in data:
    k,v=line.split(': ')
    if v.isdigit(): ops[k]=int(v)
    else:
        a,o,b=v.split()
        ops[k]=(a,o,b)
memo1={}
def eval1(k):
    if k in memo1: return memo1[k]
    v=ops[k]
    if isinstance(v,int): ans=v
    else:
        a,o,b=v; x=eval1(a); y=eval1(b)
        if o=='+': ans=x+y
        elif o=='-': ans=x-y
        elif o=='*': ans=x*y
        else: ans=x//y
    memo1[k]=ans; return ans
has_h_cache={}
def has_h(k):
    if k in has_h_cache: return has_h_cache[k]
    if k=='humn': return has_h_cache.setdefault(k,True)
    v=ops[k]
    if isinstance(v,int): return has_h_cache.setdefault(k,False)
    a,_,b=v; res=has_h(a) or has_h(b)
    has_h_cache[k]=res; return res
memo2={}
def evaluate(k):
    if k in memo2: return memo2[k]
    v=ops[k]
    if isinstance(v,int): ans=v
    else:
        a,o,b=v; x=evaluate(a); y=evaluate(b)
        if o=='+': ans=x+y
        elif o=='-': ans=x-y
        elif o=='*': ans=x*y
        else: ans=x//y
    memo2[k]=ans; return ans
def solve(k,target):
    if k=='humn': return target
    a,o,b=ops[k]
    if has_h(a):
        other=evaluate(b)
        if o=='+': nt=target-other
        elif o=='-': nt=target+other
        elif o=='*': nt=target//other
        else: nt=target*other
        return solve(a,nt)
    else:
        other=evaluate(a)
        if o=='+': nt=target-other
        elif o=='-': nt=other-target
        elif o=='*': nt=target//other
        else: nt=other//target
        return solve(b,nt)
p1=eval1('root')
a,_,b=ops['root']
if has_h(a):
    p2=solve(a,evaluate(b))
else:
    p2=solve(b,evaluate(a))
print(p1)
print(p2)